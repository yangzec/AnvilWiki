import hashlib,json,os,shutil,subprocess,tomllib
from pathlib import Path
root=Path.cwd(); task=root/'.tmp/clover-time-chinese-localization-20261010'
fork=task/'boundary-checkout'; fork.mkdir()
inputs=('src','public','docs','scripts','astro.config.ts','tsconfig.json','tailwind.config.mjs','package.json','pnpm-lock.yaml','pnpm-workspace.yaml','wrangler.toml','.indexnow-key','.nvmrc')
for name in inputs:
 src=root/name;dst=fork/name
 if src.is_dir():shutil.copytree(src,dst)
 elif src.exists():shutil.copy2(src,dst)
(fork/'node_modules').symlink_to(root/'node_modules',target_is_directory=True)
# Remove only our disposable fixture copy to simulate an untranslated article.
(fork/'src/content/wiki/zh/items/poison.mdx').unlink()
before={str(p.relative_to(fork)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (fork/'src/content/wiki').rglob('*.mdx')}
env=os.environ.copy();env.update(tomllib.loads((fork/'wrangler.toml').read_text())['vars']);env['npm_config_verify_deps_before_run']='false'
cmd=['pnpm','--config.verify-deps-before-run=false','check-i18n','--include-drafts','--strict']
r=subprocess.run(cmd,cwd=fork,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
(task/'missing-translation-i18n.log').write_text(r.stdout)
assert r.returncode==1 and 'Articles: 9/10' in r.stdout and 'zh/items/poison' in r.stdout
with (task/'missing-translation-build.log').open('w') as log:
 subprocess.run(['python3','scripts/build-research-preview.py','--output-dir','.tmp/missing-translation-preview'],cwd=fork,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
export=fork/'.tmp/missing-translation-preview'; manifest=json.loads((export/'manifest.json').read_text())
assert manifest['locale_articles']=={'en':10,'zh':9}
assert not (export/'checkout/src/content/wiki/zh/items/poison.mdx').exists()
html=(export/'upload/zh/items/poison/index.html').read_text()
assert 'Clover Time Poison Guide: Mist, Explosion' in html and 'name="robots" content="noindex' in html
home=(export/'upload/zh/index.html').read_text()
assert '/zh/zh/' not in home
assert 'href="/zh/items/poison/"' not in home
sitemap=''.join(p.read_text() for p in (export/'upload').glob('sitemap*.xml'))
assert 'https://clovertime.world/zh/items/poison/' not in sitemap
with (task/'production-policy.log').open('w') as log:
 subprocess.run(['pnpm','--config.verify-deps-before-run=false','exec','astro','build'],cwd=fork,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
for p in (fork/'src/content/wiki/en').rglob('*.mdx'):
 rel=p.relative_to(fork/'src/content/wiki/en').with_suffix('')
 for prefix in ('','zh'):
  assert not (fork/'dist'/prefix/rel/'index.html').exists(),(prefix,rel)
after={str(p.relative_to(fork)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (fork/'src/content/wiki').rglob('*.mdx')}
assert before==after
result={'strict_draft_coverage_detects_missing_translation':True,'preview_uses_real_translations':True,'missing_translation_uses_english_detail_fallback':True,'missing_translation_not_advertised_on_home':True,'no_synthetic_chinese_source':True,'fallback_noindex_and_sitemap_exclusion':True,'production_excludes_all_draft_article_urls':True,'source_hashes_unchanged':True,'preview_locale_articles':manifest['locale_articles']}
(task/'build-boundaries.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
