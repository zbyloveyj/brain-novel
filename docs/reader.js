/* Brain Novel · quiet, accessible reading controls. All preferences remain on device. */
(()=>{'use strict';
 const title='在我们理解大脑之前';
 const match=location.pathname.match(/ch(\d{2})\.html$/);
 const ch=match?Number(match[1]):0;
 const KEY='brainNovelReaderV3', OLD='brainNovelReaderV2';
 const safeRead=(k)=>{try{return JSON.parse(localStorage.getItem(k)||'{}')}catch{return {}}};
 const old=safeRead(OLD);let state={theme:'light',size:17,leading:'relaxed',font:'serif',bookmarks:{},history:{},...old,...safeRead(KEY)};
 if(!state.bookmarks||typeof state.bookmarks!=='object')state.bookmarks={};
 if(!state.history||typeof state.history!=='object')state.history={};
 const persist=()=>{try{localStorage.setItem(KEY,JSON.stringify(state));localStorage.setItem(OLD,JSON.stringify({theme:state.theme,size:state.size,lastChapter:state.lastChapter,progress:state.progress}))}catch(e){console.warn('Reader preferences could not be stored',e)}};
 const $=(s,root=document)=>root.querySelector(s);
 const el=(t,cls,txt)=>{const node=document.createElement(t);if(cls)node.className=cls;if(txt!==undefined)node.textContent=txt;return node};
 const apply=()=>{
  document.documentElement.dataset.readerTheme=state.theme==='dark'?'dark':'light';
  const v=Math.max(15,Math.min(23,Number(state.size)||17));state.size=v;
  document.documentElement.style.setProperty('--reader-size',v+'px');
  document.documentElement.style.setProperty('--reader-leading',state.leading==='compact'?'1.8':'2.04');
  const article=$('.prose');if(article)article.style.fontFamily=state.font==='sans'?'var(--sans)':'var(--serif)';
 };
 apply();
 const cover=$('.book-hero');
 if(!ch){
  if(cover&&state.lastChapter>=1&&state.lastChapter<=24){
   const a=el('a','continue-reading','继续阅读 · 第'+state.lastChapter+'章 →');
   a.href='ch'+String(state.lastChapter).padStart(2,'0')+'.html?resume=1';
   cover.insertAdjacentElement('afterend',a);
  }
  return;
 }
 if(ch<1||ch>24)return;
 document.body.classList.add('chapter-page');
 const article=$('article.prose');if(!article)return;
 const resumeRequested=new URLSearchParams(location.search).has('resume');
 const savedResume=Math.max(0,Math.min(1,Number(state.history[ch]??state.bookmarks[ch]?.position??0)||0));
 const overlay=el('div','reader-overlay');overlay.hidden=true;document.body.appendChild(overlay);
 let activePanel=null;
 const closeAll=()=>{
  if(activePanel){activePanel.hidden=true;activePanel=null}
  overlay.hidden=true;document.body.style.overflow='';
  const settings=$('.reader-settings');if(settings)settings.hidden=true;
 };
 const openDrawer=(node)=>{closeAll();activePanel=node;node.hidden=false;overlay.hidden=false;document.body.style.overflow='hidden'};
 overlay.addEventListener('click',closeAll);
 document.addEventListener('keydown',e=>{if(e.key==='Escape')closeAll()});
 window.BrainNovelReader={openDrawer,closeAll,chapter:ch};
 const toolbar=el('div','reader-toolbar');toolbar.setAttribute('aria-label','阅读工具');
 const status=el('span','reader-toolbar-label','第'+ch+'章 · 阅读中');toolbar.appendChild(status);
 const tocButton=el('button','','☰ 目录');tocButton.type='button';toolbar.appendChild(tocButton);
 const bookmarkButton=el('button','','☆ 书签');bookmarkButton.type='button';toolbar.appendChild(bookmarkButton);
 const notesButton=el('button','','✎ 笔记');notesButton.type='button';notesButton.dataset.action='notes';toolbar.appendChild(notesButton);
 const settingsAnchor=el('div','reader-popover-anchor'),settingButton=el('button','','Aa 设置');settingButton.type='button';settingsAnchor.append(settingButton);
 const settings=el('div','reader-settings');settings.hidden=true;
 const row=(title,options)=>{const r=el('div','reader-settings-row'),label=el('span','reader-settings-label',title);r.append(label);for(const opt of options){const b=el('button','',opt.text);b.type='button';b.title=opt.title||opt.text;b.setAttribute('aria-label',opt.title||opt.text);b.onclick=()=>{opt.action();refresh()};r.append(b)}return r};
 const refresh=()=>{apply();persist();bookmarkButton.textContent=state.bookmarks[ch]?'★ 已收藏':'☆ 书签';bookmarkButton.setAttribute('aria-pressed',state.bookmarks[ch]?'true':'false')};
 settings.append(row('字号',[{text:'A−',action:()=>state.size--,title:'缩小字号'},{text:'A+',action:()=>state.size++,title:'增大字号'}]));
 settings.append(row('主题',[{text:'日间',action:()=>state.theme='light'},{text:'夜间',action:()=>state.theme='dark'}]));
 settings.append(row('字体',[{text:'宋体',action:()=>state.font='serif'},{text:'黑体',action:()=>state.font='sans'}]));
 settings.append(row('行距',[{text:'标准',action:()=>state.leading='compact'},{text:'宽松',action:()=>state.leading='relaxed'}]));
 settingsAnchor.append(settings);toolbar.append(settingsAnchor);
 settingButton.onclick=()=>{settings.hidden=!settings.hidden;settingButton.setAttribute('aria-expanded',String(!settings.hidden))};
 document.addEventListener('click',e=>{if(!settingsAnchor.contains(e.target))settings.hidden=true});
 const boundary=$('.chapter-rule');boundary?boundary.insertAdjacentElement('afterend',toolbar):article.parentNode.insertBefore(toolbar,article);
 bookmarkButton.onclick=()=>{if(state.bookmarks[ch])delete state.bookmarks[ch];else state.bookmarks[ch]={position:currentPct(),savedAt:new Date().toISOString()};refresh();};refresh();
 const toc=el('section','reader-toc-panel');toc.hidden=true;toc.setAttribute('aria-label','章节目录');
 const head=el('div','reader-drawer-top');head.append(el('strong','',title));const close=el('button','reader-drawer-close','关闭');close.onclick=closeAll;head.append(close);toc.append(head);
 const marks=el('div','reader-bookmarks');toc.append(marks);
 const groups=[$('.sidenav')];
 if(groups[0]){
  groups[0].querySelectorAll(':scope > .nav-label, :scope > a').forEach(node=>{
   if(node.classList.contains('nav-label'))toc.append(el('div','reader-toc-heading',node.textContent));
   else {const a=el('a','',node.textContent);a.href=node.href.replace(location.origin,'');if(node.classList.contains('active'))a.classList.add('active');toc.append(a)}
  });
 }
 document.body.append(toc);
 function currentPct(){const max=document.documentElement.scrollHeight-innerHeight;return max>0?Math.min(1,Math.max(0,scrollY/max)):0}
 function buildBookmarks(){marks.replaceChildren();const entries=Object.entries(state.bookmarks).filter(([x,v])=>Number(x)>=1&&Number(x)<=24&&v);
  if(!entries.length)return;
  const h=el('div','reader-toc-heading','我的书签');marks.append(h);
  entries.sort((a,b)=>+a[0]-+b[0]).forEach(([num,v])=>{const a=el('a','',`第${num}章 · 已收藏`);a.href='ch'+String(num).padStart(2,'0')+'.html?resume=1';marks.append(a)})
 }
 tocButton.onclick=()=>{buildBookmarks();openDrawer(toc)};
 // Public event for the annotation script; it creates its own panel using the same overlay.
 notesButton.onclick=()=>document.dispatchEvent(new CustomEvent('brain-novel:notes'));
 const progress=el('div','reader-progress');progress.setAttribute('aria-hidden','true');document.body.append(progress);
 let scheduled=false;
 function update(){scheduled=false;const p=currentPct();progress.style.width=(p*100).toFixed(1)+'%';status.textContent=`第${ch}章 · 已读 ${Math.round(p*100)}%`;state.lastChapter=ch;state.progress=p;state.history[ch]=p;persist()}
 addEventListener('scroll',()=>{if(!scheduled){scheduled=true;requestAnimationFrame(update)}},{passive:true});
 addEventListener('pagehide',update);
 if(resumeRequested&&savedResume>0.03){
  const restore=()=>requestAnimationFrame(()=>{window.scrollTo({top:Math.max(0,document.documentElement.scrollHeight-innerHeight)*savedResume,behavior:'auto'});update()});
  if(document.fonts?.ready)document.fonts.ready.then(restore);else restore();
 }else update();
 addEventListener('keydown',e=>{if(!e.altKey||e.ctrlKey||e.metaKey)return;if(e.key==='ArrowRight'&&ch<24)location.href='ch'+String(ch+1).padStart(2,'0')+'.html';if(e.key==='ArrowLeft'&&ch>1)location.href='ch'+String(ch-1).padStart(2,'0')+'.html'});
})();
