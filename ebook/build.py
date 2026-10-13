#!/usr/bin/env python3
"""Build the complete illustrated ebook from verified QMD text + published image positions."""
from pathlib import Path
from bs4 import BeautifulSoup
from weasyprint import HTML
import re, subprocess, json, hashlib, html
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs'/'downloads'; OUT.mkdir(exist_ok=True)
font=ROOT/'ebook/fonts/NotoSerifCJKsc-Regular.otf'
if not font.exists(): raise SystemExit('Install NotoSerifCJKsc-Regular.otf in ebook/fonts first; see ebook/README.md')
parts=[(1,'第一部','大脑是什么'),(6,'第二部','大脑开始组织世界'),(9,'第三部','世界怎样抵达我'),(12,'第四部','身体开始行动'),(15,'第五部','过去如何留在身体里'),(19,'第六部','我们怎样成为自己')]
norm=lambda t:re.sub(r'[^\w\u4e00-\u9fff]','',t).casefold()
chapters=[]; toc=[]; manifest=[]
# High-resolution JPEG print copies avoid embedding large lossless RGB buffers.
print_cache=ROOT/'ebook/print-cache'; print_cache.mkdir(exist_ok=True)
def print_image(path):
 if '/plates/' not in str(path): return path
 target=print_cache/(path.stem+'-'+hashlib.sha256(path.read_bytes()).hexdigest()[:12]+'-1600-q90.jpg')
 if not target.exists():
  subprocess.run(['convert','-limit','thread','1',str(path),'-resize','1600x1000>','-sampling-factor','4:4:4','-quality','90',str(target)],check=True)
 assert target.stat().st_size>1024, target
 return target
for i in range(1,25):
 qmd=ROOT/f'ch{i:02}.qmd'; page=ROOT/f'docs/ch{i:02}.html'
 s=BeautifulSoup(page.read_text(),'html.parser'); article=s.select_one('article.prose'); notes=s.select_one('section.footnotes')
 plain=subprocess.run(['pandoc','-f','markdown','-t','plain'],input=qmd.read_text(),text=True,capture_output=True,check=True).stdout
 n=norm(plain)
 source_html=subprocess.run(['pandoc','-f','markdown','-t','html'],input=qmd.read_text(),text=True,capture_output=True,check=True).stdout
 source=BeautifulSoup(source_html,'html.parser'); published=norm(s.select_one('main').get_text())
 for element in source.select('p,li'):
  if element.select('img'): continue
  if '原稿的实验示意图正在进行公开传播权利核验' in element.get_text(): continue
  assert norm(element.get_text()) in published, f'QMD content absent from HTML: ch{i} {element.get_text()[:80]}'
 for p in article.find_all('p',recursive=False):
  assert norm(p.get_text()) in n, f'QMD/HTML mismatch: ch{i} {p.get_text()[:80]}'
 # Give every reference a chapter-local destination and preserve its existing number.
 refs=notes.select('ol.refs > li')
 for ref in refs:
  match=re.match(r'\[(\d+\.\d+)\]',ref.get_text())
  if match: ref['id']='ref-'+match[1]
 for p in article.select('p'):
  pstr=str(p)
  pstr=re.sub(r'\[(\d+\.\d+)\]',lambda m:f'<a class="citation" href="#ref-{m[1]}">[{m[1]}]</a>',pstr)
  p.replace_with(BeautifulSoup(pstr,'html.parser'))
 for f in article.select('figure'):
  prev=f.find_previous_sibling()
  if prev and prev.name=='p': prev['class']=['before-figure']
  for img in f.select('img'):
   img['src']=print_image(ROOT/'docs'/img['src']).as_uri()
   for key in ['width','height','loading','decoding']: img.attrs.pop(key,None)
  for summary in f.select('summary'):summary.decompose()
  for link in f.select('a.figure-image-link'):link.unwrap()
  for d in f.select('details'): d.unwrap()
  f['id']=f'ch{i:02}-'+f.get('id','figure')
 for x in notes.select('[style]'):del x['style']
 title=qmd.read_text().splitlines()[0].lstrip('# ').strip(); sub=s.select_one('.subtitle').get_text()
 for start,label,name in parts:
  if start==i:
   chapters.append(f'<section class="part" id="part-{start}"><p>{label}</p><h1>{name}</h1></section>')
   toc.append(f'<li class="toc-part toc-part-{start}"><a href="#part-{start}">{label}　{name}</a></li>')
 toc.append(f'<li><a href="#ch{i:02}">{title}</a></li>')
 chapters.append(f'<section class="chapter" id="ch{i:02}"><h1>{title}</h1><p class="subtitle">{html.escape(sub)}</p>{article}{notes}</section>')
 manifest.append(dict(chapter=i,title=title,paragraphs=len(article.select('p')),images=len(article.select('img')),references=len(refs),qmd_sha256=hashlib.sha256(qmd.read_bytes()).hexdigest()))
css='''
@font-face {font-family:BookSerif;src:url("FONT");}
@page {size:160mm 240mm;margin:19mm 17mm 19mm; @top-center {content:"在我们理解大脑之前";font:8pt BookSerif;color:#666;} @bottom-center {content:counter(page);font:9pt BookSerif;color:#555;}}
@page cover {margin:0;@top-center{content:none;}@bottom-center{content:none;}}
@page front {@top-center{content:none;}}
*{box-sizing:border-box}body{font-family:BookSerif,serif;font-size:10.8pt;line-height:1.85;color:#222;margin:0}
a{color:inherit;text-decoration:none}p{text-align:justify;orphans:3;widows:3;margin:0 0 2.4mm;text-indent:2em;overflow-wrap:break-word}
h1,h2{line-height:1.5;font-weight:normal;break-after:avoid}h1{font-size:21pt;margin:0 0 8mm;bookmark-level:1}h2{font-size:12pt;margin:7mm 0 3mm;bookmark-level:none}
.cover{page:cover;break-after:page;width:160mm;height:240mm;display:flex;align-items:center;justify-content:center;background:#eeeae3}.cover img{width:160mm;height:240mm;object-fit:contain}
.front{page:front;break-before:page;break-after:page}.title-page{text-align:center;padding-top:36mm}.title-page p{text-align:center;text-indent:0}.title-page h1{font-size:28pt;margin-bottom:10mm;bookmark-level:none}.author{margin-top:45mm;font-size:13pt}
.copyright{font-size:9.5pt;padding-top:15mm}.copyright p{text-indent:0;margin-bottom:6mm}.copyright h1,.toc h1{bookmark-level:none}
.toc ul{list-style:none;padding:0;margin:0;font-size:10pt;line-height:1.8}.toc li{margin:0 0 1mm}.toc a{display:block}.toc a:after{content:leader('.') target-counter(attr(href),page)}.toc-part-12{break-before:page}.toc-part{margin-top:3mm!important;font-size:11pt;color:#555;break-after:avoid}
.part{break-before:page;break-after:page;text-align:center;padding-top:49mm}.part p{text-indent:0;text-align:center;font-size:13pt;color:#777;letter-spacing:3pt}.part h1{font-size:24pt;margin-top:9mm;bookmark-level:1}
.chapter{break-before:page}.chapter>h1{font-size:20pt;padding-top:7mm;bookmark-level:2}.subtitle{font-size:10pt;color:#666;text-align:left;text-indent:0;margin-bottom:11mm;break-after:avoid}.chapter-rule,.overline{display:none}
figure{margin:4mm 0 5mm;break-inside:avoid;line-height:1.45;text-align:center}figure img{max-width:100%;max-height:80mm;object-fit:contain;display:block;margin:auto}figcaption{font-size:8.2pt;color:#46555d;text-align:left;margin-top:2mm}figcaption span{display:block}.before-figure{break-after:avoid}
hr{border:none;border-top:0.5pt solid #ccc;margin:6mm 35mm;break-after:avoid}.citation{font-size:8pt;vertical-align:super}
.footnotes{font-size:9pt;border-top:0.5pt solid #ccc;margin-top:8mm;padding-top:2mm}.footnotes p{text-indent:0;line-height:1.7}.refs{list-style:none;padding:0;font-size:8.5pt;line-height:1.65}.refs li{margin:0 0 2.5mm;break-inside:avoid;overflow-wrap:anywhere}
'''.replace('FONT',font.as_uri())
cover=(ROOT/'docs/assets/cover.webp').as_uri()
front=f'''<section class="cover"><img src="{cover}" alt="本书封面"></section>
<section class="front title-page"><h1>在我们理解大脑之前</h1><p>一个博士生穿越百年神经科学</p><p class="author">一心问道　著</p><p>六部 · 二十四章 · 完整图文电子书</p><p>2026年10月</p></section>
<section class="front copyright"><h1>版权与阅读说明</h1><p>© 2026 一心问道。作品著作权归相应权利人所有。保留所有权利。</p><p>本版为作者授权公开下载的完整图文电子书，供个人阅读。公开下载不代表开放第三方转载、改编、再发行或商业使用授权。本书尚无正式出版 ISBN。</p><p>本书以真实神经科学史为背景。部分人物对话、相遇与生活情节属于文学创作，并非历史记录。各章保留史实与创作说明及参考文献。</p><p>本版封面采用暖白、浅蓝与柔金色的神经元意象插画，于2026年10月13日更新；正文81幅插图于同日统一重绘与排版，保持原有段落位置、实验关系和资料说明。部分为科学史资料重绘或示意图，不应视为原始历史照片。</p><p>电子书依据仓库2026年10月12日主分支的二十四章定稿制作；正文与 Quarto 源文件核对，插图沿用公开阅读页面的原始段落位置。本版校正明确的叙事矛盾、重复与用语问题，精简少量议论，保留情节、章节与参考文献。</p><p>作者：一心问道<br>版本：编辑修订图文版 · 2026-10-12（封面与插图更新：2026-10-13）<br>在线阅读：<a href="https://zbyloveyj.github.io/brain-novel/">zbyloveyj.github.io/brain-novel/</a></p></section>
<section class="front toc"><h1>目录</h1><ul>{''.join(toc)}</ul></section>'''
doc='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>在我们理解大脑之前</title><meta name="author" content="一心问道"><style>'+css+'</style></head><body>'+front+''.join(chapters)+'</body></html>'
(ROOT/'ebook/book.html').write_text(doc)
HTML(string=doc,base_url=str(ROOT)).write_pdf(OUT/'brain-novel-complete.pdf',pdf_tags=True,optimize_images=True,jpeg_quality=90)
(ROOT/'ebook/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps({'chapters':len(manifest),'images':sum(x['images'] for x in manifest),'references':sum(x['references'] for x in manifest),'output':str(OUT/'brain-novel-complete.pdf')},ensure_ascii=False))
