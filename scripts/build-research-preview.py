#!/usr/bin/env python3
"""Build a noindex review export without changing source draft flags.

This is for the dedicated, noindex Pages preview, never the formal export.
The isolated copy uses existing Astro frontmatter support to render drafts;
it does not certify their facts or alter framework filtering.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tomllib


def main():
    project = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, help="New directory under project .tmp/")
    args = parser.parse_args()
    output = (project / args.output_dir).resolve()
    if not output.is_relative_to(project / ".tmp") or output.exists():
        raise SystemExit("Choose a new output directory under this project's .tmp/.")
    output.mkdir(parents=True)
    checkout = output / "checkout"
    checkout.mkdir()
    # Only build inputs: never copy .git, credentials, environment files or
    # dependency declarations from another project.
    inputs = ("src", "public", "docs", "scripts", "astro.config.ts",
              "tsconfig.json", "tailwind.config.mjs", "package.json", "pnpm-lock.yaml",
              "pnpm-workspace.yaml", "wrangler.toml")
    for name in inputs:
        source = project / name
        target = checkout / name
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            shutil.copy2(source, target)
    for name in (".indexnow-key", ".nvmrc"):
        if (project / name).is_file():
            shutil.copy2(project / name, checkout / name)
    (checkout / "node_modules").symlink_to(project / "node_modules", target_is_directory=True)

    articles = []
    for source in sorted((project / "src/content/wiki").rglob("*.mdx")):
        text = source.read_text()
        if not re.search(r"^draft:\s*true\s*$", text, re.M):
            raise SystemExit(f"Expected a research draft: {source}")
        original_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        review = re.sub(r"^draft:\s*true\s*$", "draft: false\nnoindex: true", text, count=1, flags=re.M)
        (checkout / source.relative_to(project)).write_text(review)
        # Render each real locale source in place. Missing translations keep
        # Astro's existing detail fallback and list-empty behavior; never
        # manufacture a translated source by copying the English body.
        content_path = source.relative_to(project / "src/content/wiki")
        locale = content_path.parts[0]
        prefix = "" if locale == "en" else "/" + locale
        route = prefix + "/" + Path(*content_path.parts[1:]).with_suffix("").as_posix() + "/"
        articles.append({"source": str(source.relative_to(project)), "route": route, "locale": locale,
                         "source_sha256": original_hash, "source_draft": True,
                         "review_only": True})
    if sum(article["locale"] == "en" for article in articles) != 10:
        raise SystemExit("Expected exactly ten English research source files.")

    # Review-only article entrances must not become broken links in the
    # ordinary formal export, which still excludes all source drafts.
    for locale in ("en", "zh"):
        path = checkout / "src/locales" / (locale + ".json")
        ui = json.loads(path.read_text())
        ui["home"]["popular"]["title"] = ("Explore the Wiki" if locale == "en"
                                             else "攻略与资料")
        links = []
        for article in articles:
            if article["locale"] != locale:
                continue
            text = (project / article["source"]).read_text()
            match = re.search(r'^title:\s*"([^"]+)"', text, re.M)
            links.append({"label": match.group(1) if match else article["route"],
                          # Homepage components add the locale prefix themselves.
                          "href": article["route"] if locale == "en" else article["route"][len("/" + locale):]})
        ui["home"]["popular"]["quickLinks"] = links
        path.write_text(json.dumps(ui, ensure_ascii=False, indent=2) + "\n")

    env = os.environ.copy()
    env.update(tomllib.loads((project / "wrangler.toml").read_text())["vars"])
    commands = []
    # Dependencies were frozen-installed and verified in the real checkout.
    # Prevent pnpm 11's automatic install from purging a shared symlink when
    # it sees this isolated review directory as a new workspace.
    pnpm = ("pnpm", "--config.verify-deps-before-run=false")
    for command in (pnpm + ("check-config",), pnpm + ("check-content",),
                    pnpm + ("check-i18n", "--strict-ui"),
                    pnpm + ("build:static",), pnpm + ("check-links",)):
        log_path = output / ("-".join(command) + ".log")
        with log_path.open("w") as log:
            result = subprocess.run(command, cwd=checkout, env=env, stdout=log, stderr=subprocess.STDOUT)
        commands.append({"command": list(command), "exit_code": result.returncode,
                         "log": str(log_path.relative_to(project))})
        print(json.dumps(commands[-1]), flush=True)
        if result.returncode:
            raise SystemExit(f"Failed: {' '.join(command)}; inspect {log_path}")

    upload = output / "upload"
    built = checkout / "dist"
    shutil.copytree(built, upload, ignore=lambda path, names: ["ads"] if Path(path) == built else [])
    if "X-Robots-Tag: noindex, nofollow" not in (upload / "_headers").read_text():
        raise SystemExit("Preview-wide noindex header is required.")
    sitemap = "".join(p.read_text() for p in upload.glob("sitemap*.xml"))
    for article in articles:
        html = (upload / article["route"].strip("/") / "index.html").read_text()
        if not re.search(r'name="robots"[^>]*noindex', html):
            raise SystemExit(f"Missing review noindex: {article['route']}")
        if env["SITE_URL"] + article["route"] in sitemap:
            raise SystemExit(f"Research detail leaked into sitemap: {article['route']}")
        source = project / article["source"]
        if hashlib.sha256(source.read_bytes()).hexdigest() != article["source_sha256"]:
            raise SystemExit("Source changed while building; start a fresh review build.")
    manifest = [{"path": str(p.relative_to(upload)), "bytes": p.stat().st_size,
                 "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                for p in sorted(upload.rglob("*")) if p.is_file()]
    result = {"mode": "research-preview", "formal_acceptance": "0/10",
              "locale_articles": {locale: sum(a["locale"] == locale for a in articles)
                                  for locale in ("en", "zh")},
              "upload_directory": str(upload.relative_to(project)),
              "articles": articles, "commands": commands, "files": manifest}
    (output / "manifest.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"upload_directory": result["upload_directory"],
                      "articles": len(articles), "files": len(manifest)}), flush=True)


if __name__ == "__main__":
    main()
