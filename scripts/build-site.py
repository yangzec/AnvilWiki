#!/usr/bin/env python3
"""Build the configured site into dist, retaining the source draft policy.

The protected preview uses an isolated checkout. Production uses Astro's
ordinary draft filter. Both read build variables from wrangler.toml, so a
local build and a CI build cannot silently use different canonical domains.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import tomllib


def main():
    project = Path(__file__).resolve().parent.parent
    config_path = project / "wrangler.toml"
    variables = tomllib.loads(config_path.read_text()).get("vars", {}) if config_path.exists() else {}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("preview", "production"))
    args = parser.parse_args()
    mode = args.mode or variables.get("ANVIL_BUILD_MODE", "production")
    if mode not in ("preview", "production"):
        raise SystemExit("ANVIL_BUILD_MODE must be preview or production.")
    env = os.environ.copy()
    env.update({k: str(v) for k, v in variables.items()})
    env["ANVIL_BUILD_MODE"] = mode
    print(f"[build] Mode: {mode}; SITE_URL: {env.get('SITE_URL', '(site config)')}", flush=True)
    if mode == "production":
        # This does not certify content or remove configured noindex protection.
        subprocess.run(["pnpm", "exec", "astro", "build"], cwd=project, env=env, check=True)
        return

    scratch = project / ".tmp"
    scratch.mkdir(exist_ok=True)
    output = Path(tempfile.mkdtemp(prefix="site-build-", dir=scratch))
    # The review builder requires a fresh output path and validates the finished
    # artifact before dist is replaced. A failed build leaves existing dist intact.
    output.rmdir()
    subprocess.run(["python3", "scripts/build-research-preview.py", "--output-dir",
                    str(output.relative_to(project))], cwd=project, env=env, check=True)
    manifest = json.loads((output / "manifest.json").read_text())
    staged = output / "dist-ready"
    shutil.copytree(output / "upload", staged)
    dist = project / "dist"
    old = output / "previous-dist"
    if dist.exists():
        dist.rename(old)
    try:
        staged.rename(dist)
    except Exception:
        if old.exists():
            old.rename(dist)
        raise
    if old.exists():
        shutil.rmtree(old)
    print(f"[build] Protected preview: {len(manifest['articles'])} articles exported to dist; "
          "source draft flags unchanged.", flush=True)


if __name__ == "__main__":
    main()
