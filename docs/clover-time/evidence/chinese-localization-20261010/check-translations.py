import hashlib,json,re,subprocess
from pathlib import Path
import yaml
root=Path.cwd(); out=root/'.tmp/clover-time-chinese-localization-20261010'
base=root/'src/content/wiki'; rows=[]
def parse(p):
 parts=p.read_text().split('---',2)
 return yaml.safe_load(parts[1]),parts[2]
for source in sorted((base/'en').rglob('*.mdx')):
 rel=source.relative_to(base/'en'); target=base/'zh'/rel
 en,eb=parse(source); zh,zb=parse(target)
 assert set(en)==set(zh),rel
 for key in ('category','image','date','lastModified','draft','tags','codes','gameVersion'):
  assert en.get(key)==zh.get(key),(rel,key)
 assert len(zh['title'])<=80 and 40<=len(zh['description'])<=165 and len(zh['summary'])<=400,rel
 assert len(zh['faq'])==len(en['faq'])==5,rel
 assert all(re.search('[\u4e00-\u9fff]',f[k]) for f in zh['faq'] for k in ('question','answer')),rel
 assert re.search('[\u4e00-\u9fff]',zh['summary']),rel
 assert len(re.findall(r'^## ',eb,re.M))==len(re.findall(r'^## ',zb,re.M)),rel
 imgs=lambda b:re.findall(r'!\[[^\]]*\]\(([^)]+)\)',b)
 assert imgs(eb)==imgs(zb),rel
 links=lambda b:re.findall(r'(?<!!)\[[^\]]+\]\((/[^)]+)\)',b)
 assert links(eb)==[s.removeprefix('/zh') for s in links(zb)],rel
 for e,z in zip(en.get('gallery',[]),zh.get('gallery',[])):
  assert e['image']==z['image'] and re.search('[\u4e00-\u9fff]',z['alt']) and re.search('[\u4e00-\u9fff]',z['caption']),rel
 committed=subprocess.check_output(['git','show','HEAD:'+str(source.relative_to(root))])
 assert source.read_bytes()==committed,rel
 rows.append(dict(path=rel.as_posix(),title=zh['title'],description=zh['description'],summary=zh['summary'],faq=zh['faq'],gallery=zh.get('gallery',[]),h2=len(re.findall(r'^## ',zb,re.M)),source_sha256=hashlib.sha256(committed).hexdigest(),translation_sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
assert len(rows)==len(list((base/'zh').rglob('*.mdx')))==10
result={'articles':rows,'translated_articles':len(rows),'faq_total':sum(len(r['faq']) for r in rows),'gallery_total':sum(len(r['gallery']) for r in rows),'h2_total':sum(r['h2'] for r in rows),'english_source_unchanged':True}
(out/'translations.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='articles'},ensure_ascii=False))
