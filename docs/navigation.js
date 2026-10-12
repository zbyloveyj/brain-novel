/* Chapter navigation shared by the landing page and all 24 reading pages. */
(()=>{'use strict';
 const nav=document.querySelector('#chapter-navigation');
 const toggle=document.querySelector('.navigation-toggle');
 const backdrop=document.querySelector('.navigation-backdrop');
 if(!nav||!toggle||!backdrop)return;
 const search=nav.querySelector('input[type="search"]');
 const status=nav.querySelector('.nav-search-status');
 const chapters=[...nav.querySelectorAll('a[data-chapter]')];
 const narrow=matchMedia('(max-width: 959px)');
 let returnFocus=null,previousOverflow='';
 function setOpen(open){
  if(open){returnFocus=document.activeElement;previousOverflow=document.body.style.overflow;document.body.classList.add('navigation-open');document.body.style.overflow='hidden';toggle.setAttribute('aria-expanded','true');backdrop.hidden=false;search.focus({preventScroll:true});requestAnimationFrame(()=>requestAnimationFrame(()=>{if(toggle.getAttribute('aria-expanded')==='true')search.focus({preventScroll:true})}))}
  else{const wasOpen=toggle.getAttribute('aria-expanded')==='true';document.body.classList.remove('navigation-open');toggle.setAttribute('aria-expanded','false');backdrop.hidden=true;if(wasOpen){document.body.style.overflow=previousOverflow;returnFocus?.focus()}}
 }
 toggle.addEventListener('click',()=>setOpen(toggle.getAttribute('aria-expanded')!=='true'));
 backdrop.addEventListener('click',()=>setOpen(false));
 nav.addEventListener('click',e=>{if(e.target.closest('a')&&narrow.matches)setOpen(false)});
 document.addEventListener('keydown',e=>{
  if(toggle.getAttribute('aria-expanded')!=='true')return;
  if(e.key==='Escape'){e.preventDefault();setOpen(false);return}
  if(e.key==='Tab'){
   const focusables=[toggle,...nav.querySelectorAll('input, a[href]')].filter(x=>!x.hidden&&!x.closest('[hidden]'));
   const first=focusables[0],last=focusables[focusables.length-1];
   if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}
   else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}
  }
 });
 narrow.addEventListener('change',e=>{if(!e.matches)setOpen(false)});
 const chinese=['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十','二十一','二十二','二十三','二十四'];
 search.addEventListener('input',()=>{
  const query=search.value.trim().toLowerCase();let count=0;
  chapters.forEach(a=>{const n=Number(a.dataset.chapter);const key=`${a.textContent} 第${n}章 第${chinese[n-1]}章`.toLowerCase();const isNumber=/^\d+$/.test(query);a.hidden=query?isNumber?n!==Number(query):!key.includes(query):false;if(!a.hidden)count++});
  for(const label of nav.querySelectorAll(':scope > .nav-label')){
   if(!/^第.+部/.test(label.textContent))continue;
   let next=label.nextElementSibling,visible=false;
   while(next&&!next.classList.contains('nav-label')){if(next.dataset.chapter&&!next.hidden)visible=true;next=next.nextElementSibling}
   label.hidden=!visible;
  }
  status.hidden=!query;status.textContent=count?`找到 ${count} 个章节`:'没有找到章节，试试题名或 1—24。';
 });
 // Place the selected chapter within the sidebar without moving the article.
 const active=nav.querySelector('a[data-chapter][aria-current="page"],a[data-chapter].active');
 if(active&&!narrow.matches)requestAnimationFrame(()=>{nav.scrollTop=Math.max(0,active.getBoundingClientRect().top-nav.getBoundingClientRect().top+nav.scrollTop-nav.clientHeight/2)});
})();
