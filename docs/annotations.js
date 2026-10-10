/* Brain Novel · private highlights and notes.
   Compatible with prior brainNovelAnnotationsV1 records. */
(()=>{'use strict';
 const m=location.pathname.match(/ch(\d{2})\.html$/);if(!m)return;
 const ch=Number(m[1]),article=document.querySelector('article.prose');if(!article)return;
 const KEY='brainNovelAnnotationsV1';
 let db={};try{db=JSON.parse(localStorage.getItem(KEY)||'{}')}catch{db={}}
 if(!db||typeof db!=='object'||Array.isArray(db))db={};
 const save=()=>{try{localStorage.setItem(KEY,JSON.stringify(db))}catch{alert('浏览器存储空间不足，请先导出笔记备份。')}};
 const $=(selector,root=document)=>root.querySelector(selector);
 const el=(t,cls,txt)=>{const n=document.createElement(t);if(cls)n.className=cls;if(txt!==undefined)n.textContent=txt;return n};
 const notes=(n=ch)=>{const k='ch'+n;return db[k]||(db[k]=[])};
 const paras=Array.from(article.querySelectorAll(':scope > p[data-para-index]'));
 function normalColor(c){return ['yellow','green','blue'].includes(c)?c:'yellow'}
 function stripMarks(){article.querySelectorAll('mark.reader-mark').forEach(mark=>mark.replaceWith(...mark.childNodes));paras.forEach(p=>p.normalize())}
 function anchor(note){const p=paras[note.p];if(!p)return null;
  const content=p.textContent,quote=note.quote;
  if(content.slice(note.start,note.end)===quote)return {p,start:note.start,end:note.end};
  const near=content.indexOf(quote,Math.max(0,note.start-60));const start=near<0?content.indexOf(quote):near;
  if(start<0)return null;return {p,start,end:start+quote.length};
 }
 function applyMark(note){const hit=anchor(note);if(!hit)return;
  const {p,start,end}=hit;const w=document.createTreeWalker(p,NodeFilter.SHOW_TEXT);let node;let cursor=0;const parts=[];
  while((node=w.nextNode())){const begin=cursor;cursor+=node.length;if(cursor<=start||begin>=end)continue;if(node.parentElement?.closest('mark.reader-mark'))continue;parts.push({node,a:Math.max(0,start-begin),b:Math.min(node.length,end-begin)})}
  for(const {node,a,b} of parts.reverse()){
   if(b<=a)continue;if(b<node.length)node.splitText(b);
   const text=a>0?node.splitText(a):node;
   const mark=el('mark','reader-mark');mark.dataset.noteId=note.id;mark.dataset.color=normalColor(note.color);
   text.parentNode.replaceChild(mark,text);mark.append(text);
  }
 }
 function rebuild(){stripMarks();for(const n of notes()){if(n&&Number.isInteger(n.p)&&typeof n.quote==='string'&&n.quote.length)applyMark(n)}}
 const tools=el('div','annotation-float');tools.setAttribute('role','toolbar');tools.setAttribute('aria-label','选中文字后的操作');
 for(const [mode,label] of [['yellow','黄线'],['green','绿线'],['blue','蓝线'],['note','记笔记']]){const b=el('button','',label);b.type='button';b.dataset.action=mode;tools.append(b)}
 document.body.append(tools);
 let selected=null;
 function offsetIn(p,node,offset){const r=document.createRange();r.selectNodeContents(p);try{r.setEnd(node,offset)}catch{return 0}return r.toString().length}
 function capture(){const sel=window.getSelection();if(!sel||sel.isCollapsed||!sel.rangeCount){tools.style.display='none';return}
  const r=sel.getRangeAt(0),a=r.startContainer.nodeType===Node.ELEMENT_NODE?r.startContainer:r.startContainer.parentElement;
  const b=r.endContainer.nodeType===Node.ELEMENT_NODE?r.endContainer:r.endContainer.parentElement;
  const p=a?.closest?.('p[data-para-index]');if(!p||p!==b?.closest?.('p[data-para-index]')||!article.contains(p)){tools.style.display='none';return}
  const start=offsetIn(p,r.startContainer,r.startOffset),end=offsetIn(p,r.endContainer,r.endOffset),quote=p.textContent.slice(start,end);
  if(end<=start||quote.trim().length<2||quote.length>1000){tools.style.display='none';return}
  selected={p:Number(p.dataset.paraIndex),start,end,quote};
  const rect=r.getBoundingClientRect();tools.style.display='flex';tools.style.left=Math.max(10,Math.min(innerWidth-tools.offsetWidth-10,rect.left))+'px';
  tools.style.top=Math.max(10,Math.min(innerHeight-55,rect.top-49))+'px';
 }
 document.addEventListener('mouseup',()=>setTimeout(capture,0));
 document.addEventListener('touchend',()=>setTimeout(capture,220));
 document.addEventListener('keyup',e=>{if(e.shiftKey||e.key==='ArrowRight'||e.key==='ArrowLeft')capture()});
 document.addEventListener('pointerdown',e=>{if(!tools.contains(e.target))tools.style.display='none'});
 tools.addEventListener('mousedown',e=>e.preventDefault());
 tools.addEventListener('click',e=>{
  const mode=e.target.dataset.action;if(!mode||!selected)return;
  const value=selected,overlap=notes().some(x=>x.p===value.p&&x.start<value.end&&x.end>value.start);
  if(overlap){alert('这段文字已有划线，请先在笔记面板中编辑或删除原来的划线。');return}
  const note={...value,id:'note-'+Date.now()+'-'+Math.random().toString(36).slice(2,7),body:'',color:mode==='note'?'yellow':mode,created:new Date().toISOString()};
  notes().push(note);save();window.getSelection()?.removeAllRanges();tools.style.display='none';selected=null;rebuild();
  if(mode==='note'){openNotes();renderNotes();editNote(note)}
 });
 // Notes drawer and actions
 const panel=el('aside','reader-notes-panel');panel.hidden=true;panel.setAttribute('aria-label','我的划线与笔记');
 const header=el('div','reader-notes-top');header.append(el('strong','reader-notes-title','划线与笔记'));
 const close=el('button','reader-drawer-close','关闭');close.type='button';close.onclick=()=>window.BrainNovelReader?.closeAll();header.append(close);panel.append(header);
 const help=el('p','reader-notes-help','划线与笔记保存在此浏览器中。更换设备前请导出备份。');panel.append(help);
 const scope=el('div','reader-notes-actions');
 const now=el('button','','本章'),all=el('button','','全书');scope.append(now,all);panel.append(scope);
 const listing=el('div','reader-notes-list');panel.append(listing);
 const controls=el('div','reader-notes-actions');
 const exportMd=el('button','','导出 Markdown');const exportJson=el('button','','备份 JSON');const importJson=el('button','','导入备份');
 const file=el('input');file.type='file';file.accept='.json,application/json';file.hidden=true;
 controls.append(exportMd,exportJson,importJson,file);panel.append(controls);
 document.body.append(panel);
 let scopeMode='current';
 function openNotes(){tools.style.display='none';window.BrainNovelReader?.openDrawer(panel);renderNotes()}
 document.addEventListener('brain-novel:notes',openNotes);
 now.onclick=()=>{scopeMode='current';renderNotes()};all.onclick=()=>{scopeMode='all';renderNotes()};
 function sortedNotes(){const list=scopeMode==='current'?notes().map(n=>({ch,n})):Object.keys(db).filter(k=>/^ch(?:[1-9]|1\d|2[0-4])$/.test(k)).flatMap(k=>(db[k]||[]).map(n=>({ch:Number(k.slice(2)),n})));return list.sort((a,b)=>a.ch-b.ch||a.n.p-b.n.p||a.n.start-b.n.start)}
 function editNote(n){renderNotes();const item=listing.querySelector(`[data-note-id="${CSS.escape(n.id)}"]`);if(!item)return;
  const controls=item.querySelector('.reader-notes-actions');const input=el('textarea');input.rows=4;input.placeholder='写下此刻的思考……';input.style.cssText='width:100%;resize:vertical;border:1px solid var(--line);border-radius:6px;padding:10px;background:var(--surface);color:var(--ink);font:13px/1.7 var(--sans);margin-top:10px';input.value=n.body||'';
  const saveButton=el('button','','保存笔记');saveButton.onclick=()=>{n.body=input.value.trim();save();renderNotes()};
  const cancel=el('button','','取消');cancel.onclick=renderNotes;
  controls.before(input);controls.replaceChildren(saveButton,cancel);input.focus();item.scrollIntoView({block:'nearest'});
 }
 function renderNotes(){listing.replaceChildren();const records=sortedNotes();now.setAttribute('aria-pressed',String(scopeMode==='current'));all.setAttribute('aria-pressed',String(scopeMode==='all'));
  if(!records.length){listing.append(el('p','reader-note-empty','还没有笔记。选中正文中的文字，就可以划线或写下感想。'));return}
  for(const {ch:which,n} of records){if(typeof n?.id!=='string'||typeof n.quote!=='string')continue;
   const item=el('div','reader-notes-item');item.dataset.noteId=n.id;
   item.append(el('div','reader-notes-meta',`第${which}章 · ${new Date(n.created||Date.now()).toLocaleDateString('zh-CN')}`));
   const quote=el('blockquote','',n.quote);quote.dataset.color=normalColor(n.color);item.append(quote);
   if(n.body)item.append(el('p','',n.body));
   const buttons=el('div','reader-notes-actions');
   const locate=el('button','','回到原文');locate.onclick=()=>{
    if(which!==ch){location.href=`ch${String(which).padStart(2,'0')}.html#${encodeURIComponent(n.id)}`;return}
    window.BrainNovelReader?.closeAll();const mark=article.querySelector(`mark[data-note-id="${CSS.escape(n.id)}"]`);(mark||paras[n.p])?.scrollIntoView({behavior:'smooth',block:'center'});
   };
   const edit=el('button','','编辑');edit.onclick=()=>editNote(n);
   const del=el('button','','删除');del.onclick=()=>{if(!confirm('确认删除这条划线和笔记？'))return;db['ch'+which]=(db['ch'+which]||[]).filter(x=>x.id!==n.id);save();rebuild();renderNotes()};
   buttons.append(locate,edit,del);item.append(buttons);listing.append(item)
  }
 }
 article.addEventListener('click',e=>{const mark=e.target.closest('mark.reader-mark');if(!mark)return;openNotes();const item=listing.querySelector(`[data-note-id="${CSS.escape(mark.dataset.noteId)}"]`);item?.scrollIntoView({block:'center'})});
 function download(text,name,mime){const blob=new Blob([text],{type:mime}),url=URL.createObjectURL(blob),a=el('a');a.href=url;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000)}
 exportJson.onclick=()=>download(JSON.stringify({format:'brain-novel-notes-v1',notes:db},null,2),'一心问道_阅读笔记备份.json','application/json');
 exportMd.onclick=()=>{const out=['# 《在我们理解大脑之前》阅读笔记',''];for(const {ch:n,n:x} of sortedNotes()){out.push(`## 第${n}章`,'',`> ${x.quote.replaceAll('\n','\n> ')}`,'',x.body||'（仅划线）','')}download(out.join('\n'),'一心问道_阅读笔记.md','text/markdown')};
 importJson.onclick=()=>file.click();
 file.onchange=async()=>{try{const raw=await file.files[0].text();if(raw.length>5_000_000)throw new Error('文件过大');const v=JSON.parse(raw);if(v.format!=='brain-novel-notes-v1'||!v.notes||typeof v.notes!=='object')throw new Error('笔记备份格式不匹配');
  for(const [k,arr] of Object.entries(v.notes)){if(!/^ch(?:[1-9]|1\d|2[0-4])$/.test(k)||!Array.isArray(arr))continue;
   const good=arr.filter(x=>x&&typeof x.id==='string'&&x.id.length<=140&&typeof x.quote==='string'&&x.quote.length<2000&&Number.isInteger(x.p)&&Number.isInteger(x.start)&&Number.isInteger(x.end)&&x.start>=0&&x.end>x.start).slice(0,2000);
   db[k]=[...(db[k]||[]),...good.filter(x=>!(db[k]||[]).some(y=>y.id===x.id))]
  }save();rebuild();renderNotes();alert('笔记备份导入成功')
 }catch(e){alert('导入失败：'+e.message)}file.value=''};
 rebuild();
 if(location.hash.startsWith('#note-')){setTimeout(()=>article.querySelector(`mark[data-note-id="${CSS.escape(decodeURIComponent(location.hash.slice(1)))}"]`)?.scrollIntoView({block:'center'}),200)}
})();
