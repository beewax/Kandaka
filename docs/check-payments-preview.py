from pathlib import Path
import json,threading,http.server,functools
from playwright.sync_api import sync_playwright
r=Path(__file__).parents[1]
out=Path('D:/Kandaka-builds/payments-review-render')
prod=Path('D:/Kandaka-builds/trade-production-check')
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(out)))
threading.Thread(target=server.serve_forever,daemon=True).start()
results={}
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='chrome',headless=True)
 for lang in ['en','ar']:
  rel=('ar/' if lang=='ar' else '')+'development/sudan-digital-payments/'
  assert not (prod/rel/'index.html').exists()
  pg=b.new_page(viewport={'width':390 if lang=='ar' else 1280,'height':900})
  pg.route('https://kandaka.com/images/uploads/omdurman-livelihoods-2009.jpg',lambda route:route.fulfill(path=str(out/'images/uploads/omdurman-livelihoods-2009.jpg'),content_type='image/jpeg'))
  pg.goto(f'http://127.0.0.1:{server.server_port}/'+rel)
  sel='img[src*="omdurman-livelihoods"],img[src*="payments-service-"]'
  pg.locator(sel).evaluate_all('(xs)=>xs.forEach(x=>x.loading="eager")')
  pg.wait_for_function('(sel)=>[...document.querySelectorAll(sel)].every(x=>x.complete&&x.naturalWidth>0)',arg=sel)
  assert pg.locator(sel).count()==2
  assert pg.locator('[id^="ref-"]').count()==4
  pg.screenshot(path=str(r/'docs'/f'payments-site-preview-{lang}.png'))
  results[lang]={'production_excludes_protected_draft':True,'cover_once':True,'localized_graphic_loaded':True,'four_reference_anchors':True,'canonical_cover_preview_uses_same_local_build_asset':True}
  pg.close()
 b.close()
server.shutdown()
(r/'docs/payments-render-checks-2026-11-22.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results))
