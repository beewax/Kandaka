from pathlib import Path
import re,json
from playwright.sync_api import sync_playwright
p=Path(__file__).parent
rows=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='chrome',headless=True)
 for f in p.glob('*.en.txt'):
  slug=f.name[:-7]
  en=f.read_text(encoding='utf-8');ar=(p/f'{slug}.ar.txt').read_text(encoding='utf-8')
  assert set(re.findall(r'\[\d+\]',en))==set(re.findall(r'\[\d+\]',ar))
  for lang in ['en','ar']:
   pg=b.new_page(viewport={'width':390 if lang=='ar' else 1280,'height':900})
   pg.goto((p/f'{slug}.{lang}.html').as_uri());pg.wait_for_timeout(100)
   assert pg.locator('h1').count()==1
   assert pg.evaluate('document.documentElement.scrollWidth <= window.innerWidth+1')
   assert pg.evaluate("Array.from(document.images).every(x=>x.complete&&x.naturalWidth>0)")
   assert pg.locator('html').get_attribute('dir')==('rtl' if lang=='ar' else 'ltr')
   if slug in ['trade','hotels']:pg.screenshot(path=str(p/f'preview-{slug}-{lang}.png'))
   rows.append({'slug':slug,'language':lang,'layout_checked':True,'images_loaded':pg.locator('img').count(),'references_match_other_edition':True});pg.close()
 b.close()
(p/'CHECKS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8');print(json.dumps(rows))
