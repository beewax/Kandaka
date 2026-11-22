from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).parent
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='chrome',headless=True)
 for lang in ['en','ar']:
  ar=lang=='ar'
  title='الشحنة نفسها، قيمتان مختلفتان' if ar else 'One shipment, two recorded values'
  labels=['قيمة التصدير','تكلفة النقل','قيمة الاستيراد شاملة النقل'] if ar else ['Export value','Freight cost','Import value including freight']
  foot='مثال افتراضي للشرح، وليس بيانات عن السودان. الفرق هنا تكلفة نقل، لا أموال مفقودة.' if ar else 'Illustrative figures, not Sudan data. Here the difference is freight—not missing money.'
  h=f'''<html lang="{lang}" dir="{'rtl' if ar else 'ltr'}"><meta charset="utf-8"><style>*{{box-sizing:border-box}}body{{margin:0;width:1200px;height:520px;padding:45px;background:#f4eee0;color:#193d45;font:24px/1.6 'Segoe UI',Arial}}h1{{font-size:40px;margin:0 0 35px}}.row{{display:flex;align-items:center;gap:20px}}.box{{background:white;border-top:8px solid #b88b32;border-radius:10px;padding:24px;text-align:center;flex:1;height:220px}}strong{{display:block;font-size:62px}}.sign{{font-size:40px}}p{{font-size:23px;margin-top:30px}}</style><h1>{title}</h1><div class="row">'''
  for i,(v,l) in enumerate(zip(['$100','$10','$110'],labels)):
   if i:h+=f'<span class="sign">{"+" if i==1 else "="}</span>'
   h+=f'<div class="box"><strong dir="ltr">{v}</strong>{l}</div>'
  h+=f'</div><p>{foot}</p></html>'
  pg=b.new_page(viewport={'width':1200,'height':520});pg.set_content(h);pg.screenshot(path=str(p/'images'/f'trade-values-{lang}.png'));pg.close()
 b.close()
