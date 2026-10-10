import json
from pathlib import Path
from playwright.sync_api import sync_playwright
out=Path(__file__).resolve().parent;checks=[]
for line in (out/'local-browser.log').read_text().splitlines():
 if line.startswith('{'):
  try:checks.append(json.loads(line))
  except json.JSONDecodeError:pass
assert len(checks)==45
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page();page.goto('http://127.0.0.1:4186/zh/guides/grimoire-tier-list/',wait_until='networkidle')
 page.locator('header summary').filter(has_text='中文').first.click()
 page.get_by_role('link',name='English',exact=True).click()
 page.wait_for_url('http://127.0.0.1:4186/guides/grimoire-tier-list/')
 assert page.locator('html').get_attribute('lang')=='en'
 page.locator('header summary').filter(has_text='English').first.click()
 page.get_by_role('link',name='中文',exact=True).click()
 page.wait_for_url('http://127.0.0.1:4186/zh/guides/grimoire-tier-list/')
 assert page.locator('h1').inner_text()=='Clover Time 魔导书强度榜：PvE 定位与稀有度'
 assert 'noindex' in page.locator('meta[name="robots"]').get_attribute('content')
 assert page.locator('link[hreflang="en"],link[hreflang="zh"]').count()==0
 page.screenshot(path=str(out/'local-language-switch.png'))
 b.close()
checks.append({'language_roundtrip':True,'noindex_preserved':True,'selector_retest':True})
(out/'local-browser.json').write_text(json.dumps({'origin':'http://127.0.0.1:4186','passed':len(checks),'checks':checks},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':len(checks),'language_roundtrip':True}))
