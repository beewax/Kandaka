from pathlib import Path
import html,json,re,shutil,requests,hashlib
p=Path(__file__).parent;r=p.parents[1];a=p/'images';a.mkdir(exist_ok=True)
items=[
('trade','sudan-ports-classic-approved.png','Port Sudan-inspired conceptual illustration, previously approved for the ports article. Fictional harbour, not a documentary photograph. Proposed reuse only; not approved for this new feature.','رسم مفاهيمي مستلهم من بورتسودان، اعتُمد سابقاً لمقال الموانئ. مشهد متخيل لا صورة وثائقية. اقتراح لإعادة الاستخدام، غير معتمد لهذا المقال.','https://kandaka.com/development/sudan-deep-sea-ports/'),
('payments','omdurman-livelihoods-2009.jpg','Omdurman market, 14 August 2009. Petr Adam Dohnálek, CC BY-SA 3.0 CZ. Historical context only: no digital-payment use is inferred about the people pictured. Unmodified.','سوق أم درمان، ١٤ أغسطس ٢٠٠٩. تصوير بيتر آدم دوناليك، CC BY-SA 3.0 CZ. سياق تاريخي فقط؛ لا تُنسب إلى الأشخاص المصورين ممارسة دفع رقمي. الصورة دون تعديل.','https://commons.wikimedia.org/wiki/File:Bazaro_en_Omdurman_001.jpg'),
('innovation','atbara-railway-workshops-2008.jpg','Atbara railway workshops, 2008. Bertramz, CC BY 3.0. Historical engineering context, not a current research facility. Unmodified.','ورش السكك الحديدية بعطبرة، ٢٠٠٨. تصوير بيرترامز، CC BY 3.0. سياق هندسي تاريخي، لا منشأة بحث راهنة. الصورة دون تعديل.','https://commons.wikimedia.org/wiki/File:Atbara_railway.jpg'),
('wad-ban-naqa','wad-ban-naqa-barque-stand.jpg','Barque stand from Wad Ban Naqa, inventory ÄM 7261, photographed in Berlin on 5 July 2023 by Neoclassicism Enthusiast, CC0 1.0. This is a museum object, not a current site view. Unmodified.','قاعدة مركب شعائري من ود بانقا، رقم ÄM 7261، صُورت ببرلين في ٥ يوليو ٢٠٢٣ بواسطة Neoclassicism Enthusiast، بترخيص CC0 1.0. أثر معروض بمتحف، لا منظر راهن للموقع. دون تعديل.','https://commons.wikimedia.org/wiki/File:Base_for_a_barque_of_the_royal_couple_Natakamani_and_Amanitore,_1-25_AD,_sandstone,_from_Wad_Ban_Naga,_%C3%84M_7261,_in_the_%C3%84gyptisches_Museum_Berlin_(03).jpg'),
('hotels','grand-hotel-courtyard.jpg','Grand Hotel courtyard, Khartoum. Grandhotelsudan, CC BY-SA 4.0. Capture date unconfirmed; uploaded 26 March 2023. An earlier view, not evidence of present conditions or visitor access. Unmodified.','فناء الفندق الكبير بالخرطوم. Grandhotelsudan، CC BY-SA 4.0. تاريخ الالتقاط غير مؤكد؛ رُفعت الصورة في ٢٦ مارس ٢٠٢٣. منظر سابق لا يثبت الحالة الحالية أو إمكان الزيارة. دون تعديل.','https://commons.wikimedia.org/wiki/File:Grand_Hotel_Khartoum_Sudan.jpg')]
remote={
'wad-ban-naqa-barque-stand.jpg':'https://upload.wikimedia.org/wikipedia/commons/9/90/Base_for_a_barque_of_the_royal_couple_Natakamani_and_Amanitore%2C_1-25_AD%2C_sandstone%2C_from_Wad_Ban_Naga%2C_%C3%84M_7261%2C_in_the_%C3%84gyptisches_Museum_Berlin_%2803%29.jpg',
'grand-hotel-courtyard.jpg':'https://upload.wikimedia.org/wikipedia/commons/6/69/Grand_Hotel_Khartoum_Sudan.jpg'}
licenses={'trade':None,'payments':'https://creativecommons.org/licenses/by-sa/3.0/cz/','innovation':'https://creativecommons.org/licenses/by/3.0/','wad-ban-naqa':'https://creativecommons.org/publicdomain/zero/1.0/','hotels':'https://creativecommons.org/licenses/by-sa/4.0/'}
stats=[];index=[]
for slug,img,capen,capar,source in items:
 dest=a/img
 if not dest.exists():
  if img in remote:
   print('Source image pending retrieval:',img)
  else:shutil.copyfile(r/'static/images/uploads'/img,dest)
 item={'slug':slug,'image':img,'source':source,'licence':licenses[slug],'caption_en':capen,'caption_ar':capar,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest() if dest.exists() else None,'image_status':'proposed, requires owner review' if dest.exists() else 'source verified; retrieval blocked HTTP 403/429, pixels not inspected','editions':{}}
 for lang,caption in [('en',capen),('ar',capar)]:
  s=(p/f'{slug}.{lang}.txt').read_text(encoding='utf-8');lines=s.splitlines();title=lines[0]
  content='\n'.join(lines[2:]);paras=[x.strip() for x in content.split('\n\n') if x.strip()]
  def linkify(x):
   return re.sub(r'https?://[^\s<>]+',lambda m:'<a href="'+m[0]+'">'+m[0]+'</a>',html.escape(x))
  blocks=[]
  for para in paras:
   tag='h2' if len(para)<85 and '\n' not in para and not para.startswith('[') else 'p'
   blocks.append(f'<{tag}>'+linkify(para).replace('\n','<br>')+f'</{tag}>')
  page=f'''<!doctype html><html lang="{lang}" dir="{'rtl' if lang=='ar' else 'ltr'}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>body{{max-width:850px;margin:32px auto;padding:0 24px;background:#faf8f2;color:#242424;font:20px/1.8 Georgia,'Segoe UI',serif}}h1{{line-height:1.25}}h2{{font-size:1.25em;margin-top:2em}}img{{max-width:100%;max-height:550px;object-fit:contain}}figcaption{{font-size:15px}}a{{overflow-wrap:anywhere;color:#72521e}}.status{{background:#fff0c2;padding:12px;font:16px/1.6 'Segoe UI',sans-serif}}p{{white-space:normal}}</style><a href="INDEX.html">Review index / فهرس المراجعة</a><h1>{html.escape(title)}</h1><p class="status">{html.escape(lines[1])}<br>Initial manuscript; research and image checks remain. مسودة أولى؛ البحث وفحص الصور لم يكتملَا.</p><figure><img src="images/{img}" alt="{html.escape(caption)}"><figcaption>{html.escape(caption)} <a href="{source}">Source / المصدر</a> {'<a href="'+licenses[slug]+'">Licence / الترخيص</a>' if licenses[slug] else ''}</figcaption></figure>{''.join(blocks)}</html>'''
  if not dest.exists():page=page.replace(f'<img src="images/{img}" alt="{html.escape(caption)}">','<p class="status">Image source identified; preview retrieval pending. عُثر على مصدر الصورة، ومعاينتها لم تكتمل.</p>')
  (p/f'{slug}.{lang}.html').write_text(page,encoding='utf-8');item['editions'][lang]={'words':len(content.split()),'paragraphs':len(paras),'title':title}
 index.append(f'<li><strong>{html.escape(item["editions"]["en"]["title"])}</strong><br><a href="{slug}.en.html">English draft</a> · <a href="{slug}.ar.html">المسودة العربية</a></li>');stats.append(item)
(p/'INDEX.html').write_text('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kandaka five-article review</title><style>body{max-width:900px;margin:40px auto;padding:20px;font:20px/1.7 system-ui;background:#faf8f2}li{margin:25px 0}a{color:#73531c}</style><h1>Kandaka — five first-draft pairs</h1><p>22 November 2026. Research in progress; images proposed, not approved. Not scheduled or published. Each article lists its remaining editorial checks. Planned releases are at least 48 hours apart after review and readiness.</p><p dir="rtl">خمس مسودات أولى باللغتين؛ البحث جارٍ والصور مقترحة غير معتمدة. لم تُحدد مواعيد فعلية ولم يُنشر شيء.</p><ol>'+''.join(index)+'</ol>',encoding='utf-8')
(p/'REVIEW-MANIFEST.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps([{'slug':x['slug'],'en_words':x['editions']['en']['words'],'ar_words':x['editions']['ar']['words']} for x in stats]))
