import json,os,re,sys
from pathlib import Path
from playwright.sync_api import sync_playwright
out=Path(__file__).resolve().parent
online='--online' in sys.argv
origin='https://clovertime.world' if online else 'http://127.0.0.1:4186'
mode='online' if online else 'local'
articles=json.loads((out/'translations.json').read_text())['articles']
class CheckList(list):
 def append(self,value):
  super().append(value)
  print(json.dumps(value,ensure_ascii=False),flush=True)
checks=CheckList()
with sync_playwright() as p:
 opts=dict(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 if online:opts['proxy']={'server':os.environ['HTTPS_PROXY']}
 browser=p.chromium.launch(**opts)
 ctx=browser.new_context(permissions=['clipboard-read','clipboard-write'])
 ctx.add_init_script("localStorage.setItem('aw-cookie-consent','declined')")
 page=ctx.new_page()
 for a in articles:
  route='/zh/'+a['path'].removesuffix('.mdx')+'/'
  for width in (375,1440):
   page.set_viewport_size(dict(width=width,height=900))
   response=page.goto(origin+route,wait_until='networkidle',timeout=45000)
   assert response.status==200,route
   assert page.locator('html').get_attribute('lang')=='zh',route
   assert page.locator('h1').inner_text()==a['title'],route
   assert page.locator('meta[name="description"]').get_attribute('content')==a['description'],route
   assert page.locator('[data-summary-text]').inner_text().strip()==a['summary'],route
   assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'),route
   assert page.locator('link[rel="canonical"]').get_attribute('href')=='https://clovertime.world'+route
   assert 'noindex' in page.locator('meta[name="robots"]').get_attribute('content')
   if online:assert 'noindex' in response.headers.get('x-robots-tag','')
   faq=[]
   for s in page.locator('script[type="application/ld+json"]').all_text_contents():
    obj=json.loads(s)
    entities=obj if isinstance(obj,list) else obj.get('@graph',[obj])
    for e in entities:
     if e.get('@type')=='FAQPage':faq.extend(e['mainEntity'])
   assert len(faq)==5,(route,len(faq))
   for f in a['faq']:
    item=next(x for x in faq if x['name']==f['question'])
    assert item['acceptedAnswer']['text']==f['answer'],route
    summary=page.locator('summary').filter(has_text=f['question']).first
    summary.click()
    assert f['answer'] in summary.locator('..').inner_text(),route
   if a['gallery']:
    thumbs=page.locator('[data-gallery-thumb]')
    assert thumbs.count()==2
    thumbs.first.click()
    page.locator('[data-gallery-lightbox][open]').wait_for()
    page.locator('[data-gallery-full]').evaluate('(i)=>i.decode()')
    assert page.locator('[data-gallery-caption]').inner_text()==a['gallery'][0]['caption']
    page.locator('[data-gallery-next]').click()
    page.locator('[data-gallery-full]').evaluate('(i)=>i.decode()')
    assert page.locator('[data-gallery-caption]').inner_text()==a['gallery'][1]['caption']
    page.keyboard.press('Escape')
   page.evaluate('window.scrollTo(0,document.body.scrollHeight)')
   page.wait_for_timeout(120)
   assert page.locator('img[src]').evaluate_all('(xs)=>xs.every(i=>i.complete&&i.naturalWidth>0)'),route
   assert page.locator('main a[href]').evaluate_all(r'''xs=>xs.filter(x=>new URL(x.href).origin===location.origin).every(x=>{let p=new URL(x.href).pathname;return /\.[a-z0-9]+$/i.test(p)||p.startsWith('/zh/');})'''),route
   assert not re.search(r'研究稿|未确认|待核实|正文使用英文',page.locator('main').inner_text()),route
   if a['path'] in ('guides/beginner-guide.mdx','guides/grimoire-tier-list.mdx'):
    page.evaluate('window.scrollTo(0,0)')
    page.screenshot(path=str(out/f'{mode}-{a["path"].replace("/","-").removesuffix(".mdx")}-{width}.png'))
   checks.append(dict(route=route,width=width,translated=True,faq=5,gallery=len(a['gallery']),no_overflow=True))
  english_route=route.removeprefix('/zh')
  response=page.goto(origin+english_route,wait_until='domcontentloaded')
  assert response.status==200
  assert not re.search('[\u4e00-\u9fff]',page.locator('h1').inner_text())
  checks.append(dict(route=english_route,english_preserved=True))
 for name,title in [('about','关于本站'),('privacy-policy','隐私政策'),('terms-of-service','使用条款'),('copyright','版权说明'),('contact','联系')]:
  page.set_viewport_size(dict(width=375,height=900))
  route='/zh/'+name+'/'
  response=page.goto(origin+route,wait_until='networkidle')
  assert response.status==200
  assert page.locator('h1').inner_text()==title
  assert re.search('[\u4e00-\u9fff]',page.locator('main').inner_text())
  assert '{' not in page.locator('meta[name="description"]').get_attribute('content')
  assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
  if name=='contact':assert page.locator('main a[href="/zh/copyright/"]').count()==1
  checks.append(dict(route=route,legal_localized=True))
 for category in ('codes','guides','items'):
  route='/zh/'+category+'/'
  assert page.goto(origin+route,wait_until='networkidle').status==200
  titles=[a['title'] for a in articles if a['path'].startswith(category+'/')]
  assert all(t in page.locator('main').inner_text() for t in titles)
  checks.append(dict(route=route,translated_titles=len(titles)))
 for width in (375,1440):
  page.set_viewport_size(dict(width=width,height=900))
  assert page.goto(origin+'/zh/',wait_until='networkidle').status==200
  assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
  text=page.locator('main').inner_text()
  assert all(a['title'] in text for a in articles)
  assert not page.locator('a[href^="/zh/zh/"]').count()
  page.screenshot(path=str(out/f'{mode}-home-zh-{width}.png'))
  checks.append(dict(route='/zh/',width=width,translated_quick_links=10))
 for query,target in [('毒雾','/zh/items/poison/'),('魔力水晶碎片','/zh/guides/fishing-fragments/'),('土豆','/zh/guides/beginner-guide/'),('社会阶层','/zh/guides/how-to-reroll/')]:
  page.goto(origin+'/zh/',wait_until='networkidle')
  page.locator('#search-trigger').click()
  page.locator('.pagefind-ui__search-input').fill(query)
  page.wait_for_function('(target)=>[...document.querySelectorAll(".pagefind-ui__result-link")].some(x=>new URL(x.href).pathname===target)',arg=target,timeout=15000)
  assert page.locator('.pagefind-ui__result-link').evaluate_all('xs=>xs.every(x=>new URL(x.href).pathname.startsWith("/zh/"))')
  if query=='魔力水晶碎片':page.screenshot(path=str(out/f'{mode}-chinese-search.png'))
  page.locator(f'.pagefind-ui__result-link[href$="{target}"]').first.click()
  page.wait_for_url('**'+target)
  checks.append(dict(query=query,target=target,search=True))
 page.goto(origin+'/zh/guides/grimoire-tier-list/',wait_until='networkidle')
 expected=page.locator('[data-summary-text]').inner_text().strip()
 page.locator('[data-copy-summary]').click()
 page.wait_for_function("document.querySelector('[data-copy-summary]').title==='已复制！'")
 assert page.evaluate('navigator.clipboard.readText()').strip()==expected
 checks.append(dict(chinese_summary_copy=True))
 page.locator('header summary').filter(has_text='中文').first.click()
 page.get_by_role('link',name='English',exact=True).click()
 page.wait_for_url('**/guides/grimoire-tier-list/')
 assert page.locator('html').get_attribute('lang')=='en'
 page.locator('header summary').filter(has_text='English').first.click()
 page.get_by_role('link',name='中文',exact=True).click()
 page.wait_for_url('**/zh/guides/grimoire-tier-list/')
 assert page.locator('h1').inner_text()==next(a['title'] for a in articles if a['path']=='guides/grimoire-tier-list.mdx')
 checks.append(dict(language_roundtrip=True))
 browser.close()
(out/f'{mode}-browser.json').write_text(json.dumps({'origin':origin,'passed':len(checks),'checks':checks},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'origin':origin,'passed':len(checks)},ensure_ascii=False))
