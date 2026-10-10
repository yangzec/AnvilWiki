/**
 * i18n smoke test — regression guard for the "hardcoded locale" bug class.
 *
 * In v1.1.0 five getStaticPaths implementations inlined `['ja']` while the
 * CLI accepted any locale list — forks adding a 3rd language got site-wide
 * 404s. This test greps the route/i18n sources for hardcoded locale arrays
 * so the bug class can't silently return.
 *
 * The route sweep WALKS src/pages/[locale]/ instead of whitelisting files:
 * a brand-new locale route file joins the assertions automatically — new
 * files were exactly the ones that used to skip locale derivation.
 */
import { describe, expect, it } from 'vitest';
import * as fs from 'node:fs';
import * as path from 'node:path';
import { spawnSync } from 'node:child_process';
import { getUi } from '~/i18n/ui';
import { locales, defaultLocale } from '~/i18n/routing';

const ROOT = path.resolve(__dirname, '..');
const LOCALE_ROUTES_DIR = path.join(ROOT, 'src/pages/[locale]');

function localeRouteFiles(): string[] {
  const files: string[] = [];
  const walk = (dir: string) => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(full);
      else if (entry.name.endsWith('.astro')) files.push(full);
    }
  };
  walk(LOCALE_ROUTES_DIR);
  return files.sort();
}

// The route files above, plus the locale-derivation helper module itself.
const SWEEP_FILES = [...localeRouteFiles(), path.join(ROOT, 'src/i18n/content.ts')];

describe('i18n: no hardcoded locale arrays', () => {
  it('the route walk actually finds the locale route files (no silent empty scan)', () => {
    // index + faq + [...slug] + [legal] + recent + tags/index + tags/[tag].
    expect(localeRouteFiles().length).toBeGreaterThanOrEqual(7);
  });

  for (const file of SWEEP_FILES) {
    const rel = path.relative(ROOT, file);
    it(`${rel} derives locales from routing.ts (no inline ['xx'] arrays)`, () => {
      const src = fs.readFileSync(file, 'utf8');
      // Matches ['ja'], ['en'], ['ja','zh'] etc. — but NOT `locales` identifiers.
      const hardcoded = src.match(/\[\s*['"][a-z]{2}['"]\s*(,\s*['"][a-z]{2}['"]\s*)*\]/g);
      expect(hardcoded ?? [], `found hardcoded locale array in ${rel}: ${hardcoded?.join(', ')}`).toHaveLength(0);
    });
  }

  it('routing.ts locales array is parseable and non-empty', () => {
    const src = fs.readFileSync(path.resolve(ROOT, 'src/i18n/routing.ts'), 'utf8');
    const m = src.match(/export const locales = \[([^\]]+)\] as const;/);
    expect(m).toBeTruthy();
    const list = Array.from(m![1].matchAll(/['"]([^'"]+)['"]/g)).map((x) => x[1]);
    expect(list.length).toBeGreaterThan(0);
    expect(list).toContain('en');
  });
});

describe('i18n: getUi results are deeply frozen (read-only by contract AND at runtime)', () => {
  // getUi caches merged objects and deepMerge shares nested references with
  // the en module table — one caller mutating its copy would silently poison
  // every other locale's view. ui.ts deep-freezes all results so mutation
  // throws (strict-mode modules) instead.
  it('every locale flavor is deeply frozen (en, cached merge, unknown-locale copy)', () => {
    const ja = getUi(locales.find((l) => l !== defaultLocale) ?? defaultLocale);
    expect(Object.isFrozen(ja)).toBe(true);
    expect(Object.isFrozen(ja.home)).toBe(true);
    expect(Object.isFrozen(getUi('en').shared)).toBe(true);
    const unknown = getUi('zz');
    expect(Object.isFrozen(unknown)).toBe(true);
  });

  it('mutating a cached locale result throws (no silent cross-locale poisoning)', () => {
    const ja = getUi(locales.find((l) => l !== defaultLocale) ?? defaultLocale);
    expect(() => {
      (ja as Record<string, unknown>).nav = 'poison';
    }).toThrow();
    // Nesting that came from the en table through the merge must be frozen too.
    expect(() => {
      (ja.shared as Record<string, unknown>).wikiNavAria = 'poison';
    }).toThrow();
  });
});

describe('i18n: draft translation coverage can be checked explicitly', () => {
  function report(translated: boolean, includeDrafts: boolean) {
    const root = fs.mkdtempSync(path.join(ROOT, '.tmp/i18n-coverage-'));
    try {
      fs.mkdirSync(path.join(root, 'src/i18n'), { recursive: true });
      fs.writeFileSync(path.join(root, 'src/i18n/routing.ts'),
        "export const locales = ['en', 'zh'] as const;\nexport const defaultLocale = 'en';\n");
      fs.mkdirSync(path.join(root, 'src/locales'), { recursive: true });
      for (const locale of ['en', 'zh']) {
        fs.writeFileSync(path.join(root, `src/locales/${locale}.json`), '{"nav":{"home":"Home"}}');
        fs.mkdirSync(path.join(root, `src/content/wiki/${locale}/guides`), { recursive: true });
      }
      const draft = '---\ntitle: "Example"\ndraft: true\n---\n';
      fs.writeFileSync(path.join(root, 'src/content/wiki/en/guides/example.mdx'), draft);
      if (translated) fs.writeFileSync(path.join(root, 'src/content/wiki/zh/guides/example.mdx'), draft);
      return spawnSync(process.execPath, [
        '--import', path.join(ROOT, 'node_modules/tsx/dist/loader.mjs'),
        path.join(ROOT, 'scripts/check-i18n.ts'), '--strict',
        ...(includeDrafts ? ['--include-drafts'] : []),
      ], { cwd: root, encoding: 'utf8' });
    } finally {
      fs.rmSync(root, { recursive: true, force: true });
    }
  }

  it('keeps the default published-only policy for untranslated drafts', () => {
    const result = report(false, false);
    expect(result.status, result.stderr).toBe(0);
    expect(result.stdout).toContain('Articles: 0/0');
  });

  it('fails strict authoring coverage when a draft translation is missing', () => {
    const result = report(false, true);
    expect(result.status, result.stderr).toBe(1);
    expect(result.stdout).toContain('Articles: 0/1');
    expect(result.stdout).toContain('missing:  zh/guides/example');
  });

  it('counts translated drafts instead of reporting an empty 0/0', () => {
    const result = report(true, true);
    expect(result.status, result.stderr).toBe(0);
    expect(result.stdout).toContain('Articles: 1/1 translated (100%)');
  });
});
