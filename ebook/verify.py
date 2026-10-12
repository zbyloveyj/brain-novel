"""Validate rendered ebook contents and geometry. Requires PyMuPDF."""
from pathlib import Path
import fitz,re,json,hashlib
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
pdf=root/'docs/downloads/brain-novel-complete.pdf';doc=fitz.open(pdf)
norm=lambda t:re.sub(r'[^\w\u4e00-\u9fff]','',t)
texts=['\n'.join(line for line in p.get_text().splitlines() if line.strip()!='在我们理解大脑之前' and line.strip()!=str(i+1)) for i,p in enumerate(doc)]
full=norm(''.join(texts));missing=[];counts={'chapters':24,'images':0,'references':0,'paragraphs':0}
for i in range(1,25):
 s=BeautifulSoup((root/f'docs/ch{i:02}.html').read_text(),'html.parser')
 counts['images']+=len(s.select('article.prose img'));counts['references']+=len(s.select('ol.refs > li'));counts['paragraphs']+=len(s.select('article.prose > p'))
 for e in s.select('article.prose > p,section.footnotes > p,ol.refs > li,figcaption'):
  for x in e.select('summary'):x.decompose()
  if norm(e.get_text()) not in full:missing.append([i,e.get_text()[:80]])
 bounds=[]
for i,p in enumerate(doc):
 for b in p.get_text('dict')['blocks']:
  x0,y0,x1,y1=b['bbox']
  if x0<-1 or y0<-1 or x1>p.rect.width+1 or y1>p.rect.height+1:bounds.append(i+1)
images=sum(len(p.get_image_info()) for p in doc)
bookmarks=doc.get_toc();assert len(bookmarks)==30
assert not missing,missing
assert not bounds,bounds
assert images==counts['images']+1,(images,counts)
assert not any('\ufffd' in t for t in texts)
# Every numbered chapter begins at its own page and agrees with its bookmark.
for level,title,page in bookmarks:
 if level==2: assert norm(title) in norm(texts[page-1][:200]),(title,page)
result=dict(pages=len(doc),**counts,image_placements=images,bookmarks=len(bookmarks),missing_text_blocks=len(missing),out_of_page_blocks=len(bounds),sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),bytes=pdf.stat().st_size)
(root/'ebook/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
