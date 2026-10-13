#!/usr/bin/env python3
"""Reproducible book-plate design. All curves are explicitly educational examples.

Original reading positions and explanations are recorded in original-inventory.json.
Scientific diagrams are authored as vectors; the neuron forest is an artistic plate.
"""
from pathlib import Path
import json, math, textwrap, subprocess, re, sys, html
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse, Rectangle, Arc
from matplotlib.colors import LinearSegmentedColormap

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/assets/plates'; OUT.mkdir(parents=True,exist_ok=True)
FONT=ROOT/'ebook/fonts/NotoSerifCJKsc-Regular.otf'
fm.fontManager.addfont(str(FONT))
plt.rcParams.update({'font.family':fm.FontProperties(fname=FONT).get_name(),'font.size':18,'svg.fonttype':'path','axes.unicode_minus':False,'savefig.facecolor':'#fbf8f1'})
INK='#193d50'; BLUE='#315f77'; COPPER='#ac693c'; TEAL='#628c83'; GOLD='#c4a365'; PLUM='#86718b'; MUTED='#69777c'; LINE='#d9d5c9'; PAPER='#fbf8f1'; TINT='#edf2f1'; SAND='#f2e6d6'
COL=[BLUE,COPPER,TEAL,PLUM,GOLD]
inventory=json.loads((ROOT/'illustrations/original-inventory.json').read_text())
META={int(Path(it['path']).stem.split('-')[-1]):it for it in inventory}
TEXT=[];CHECK=[];ALL=[]
SELECT=set(map(int,sys.argv[1:])) if len(sys.argv)>1 else set(range(2,83))

def txt(ax,x,y,s,size=18,color=INK,ha='center',va='center',**kw):
    s=s.replace('Na⁺',r'Na$^{+}$').replace('K⁺',r'K$^{+}$')
    t=ax.text(x,y,s,fontsize=size,color=color,ha=ha,va=va,linespacing=1.6,**kw);TEXT.append(t);return t
def line(ax,a,b,color=LINE,lw=1.4,**kw):ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=lw,**kw)
def arrow(ax,a,b,color=BLUE,style='->',rad=0,dashed=False):
    p=FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=16,lw=1.65,color=color,connectionstyle=f'arc3,rad={rad}',linestyle=dashed if isinstance(dashed,str) else '--' if dashed else '-',shrinkA=1,shrinkB=1);ax.add_patch(p)
def node(ax,x,y,w,h,s,accent=False,size=18):
    p=FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.02,rounding_size=1.2',fc=SAND if accent else '#fffefa',ec='#c69b76' if accent else '#9caeb4',lw=1.25);ax.add_patch(p)
    t=txt(ax,x,y,s,size=size);CHECK.append((t,p));return (x,y,w,h)
def tag(ax,x,y,s,color=COPPER,size=15):txt(ax,x,y,s,size=size,color=color)
def frame(n,title,foot,kind='科学示意'):
    global TEXT,CHECK
    TEXT=[];CHECK=[]
    fig=plt.figure(figsize=(12.8,8),facecolor=PAPER);ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,100),ylim=(0,100));ax.axis('off')
    it=META[n]
    txt(ax,5,94,f"{it['ch']:02d} / {it['n']:02d}    {kind}",size=12,color=COPPER,ha='left')
    txt(ax,95,94,'在我们理解大脑之前',size=12,color=MUTED,ha='right')
    txt(ax,5,85,title,size=26,ha='left');line(ax,(5,77),(95,77));line(ax,(5,77),(12,77),COPPER,2.6)
    line(ax,(5,12),(95,12))
    txt(ax,5,7,foot,size=13,color=MUTED,ha='left')
    return fig,ax
def save(fig,n):
    if n not in SELECT:
        plt.close(fig);return
    fig.canvas.draw();renderer=fig.canvas.get_renderer();w,h=fig.canvas.get_width_height()
    problems=[]
    for t in TEXT:
        b=t.get_window_extent(renderer)
        if b.x0<12 or b.y0<10 or b.x1>w-12 or b.y1>h-10:problems.append('outside: '+t.get_text())
    for t,p in CHECK:
        b=t.get_window_extent(renderer);box=p.get_window_extent(renderer)
        if b.width>box.width-8 or b.height>box.height-5:problems.append('node overflow: '+t.get_text())
    ALL.append({'figure':n,'chapter':META[n]['ch'],'text':[t.get_text() for t in TEXT],'layout_issues':problems})
    dest=OUT/f'figure-{n:03d}'
    fig.savefig(str(dest)+'.svg',metadata={'Date':None,'Creator':'Brain Novel / editorial illustration edition'})
    svg=Path(str(dest)+'.svg');data=svg.read_text();meta='<title>'+html.escape(TEXT[2].get_text())+'</title><desc>'+html.escape('；'.join(t.get_text() for t in TEXT))+'</desc>'
    svg.write_text(re.sub(r'(<svg\s[^>]*>)',lambda m:m[1]+'\n'+meta,data,count=1,flags=re.S))
    temp=OUT/f'_figure-{n:03d}.png';fig.savefig(temp,dpi=200)
    webp=Path(str(dest)+'.webp')
    for attempt in range(3):
        subprocess.run(['convert','-limit','thread','1',str(temp),'-quality','94',str(webp)],check=True)
        if webp.stat().st_size>1024:break
    assert webp.stat().st_size>1024, webp
    temp.unlink();plt.close(fig)

def timeline(n,title,events,foot):
    fig,ax=frame(n,title,foot,'科学史 · 时间线')
    if len(events)<=4:
        # Three or four readable columns; no text placed beyond either end of the line.
        xs=np.linspace(17,83,len(events));line(ax,(xs[0],58),(xs[-1],58),BLUE,2)
        for j,((year,name,desc),x) in enumerate(zip(events,xs)):
            ax.scatter([x],[58],s=110,color=COPPER if j==len(events)-1 else BLUE,zorder=4,edgecolor=PAPER,lw=2)
            txt(ax,x,66,year,25,color=COPPER);txt(ax,x,49,name,17)
            txt(ax,x,35,desc,15,color=MUTED)
    else:
        for j,(year,name,desc) in enumerate(events):
            x=20+(j%3)*30;y=61-(j//3)*29
            node(ax,x,y,27,22,name+'\n'+desc,size=15,accent=j==len(events)-1);tag(ax,x,y+13,year,size=17)
    save(fig,n)
def table(n,title,headers,rows,foot,widths=None):
    fig,ax=frame(n,title,foot,'比较与证据')
    widths=np.array(widths if widths else [1]*len(headers));widths=90*widths/sum(widths);xs=np.r_[5,5+np.cumsum(widths)]
    top=70;rh=min(10.5,52/(len(rows)+1))
    ax.add_patch(Rectangle((5,top-rh),90,rh,color=INK))
    for j,h in enumerate(headers):txt(ax,(xs[j]+xs[j+1])/2,top-rh/2,h,16,color=PAPER)
    for i,row in enumerate(rows):
        y=top-rh*(i+2)
        ax.add_patch(Rectangle((5,y),90,rh,fc='#f0eee6' if i%2==0 else '#fffdf7',ec='none'))
        for j,v in enumerate(row):txt(ax,(xs[j]+xs[j+1])/2,y+rh/2,v,16,color=COPPER if v=='✓' else INK)
        line(ax,(5,y),(95,y),LINE,.7)
    save(fig,n)
def chain(n,title,labels,foot,sub=None):
    fig,ax=frame(n,title,foot,'过程与联系');xs=np.linspace(16,84,len(labels));w=min(22,76/len(labels));y=47
    for j,(x,l) in enumerate(zip(xs,labels)):
        node(ax,x,y,w,19,l,accent=j==len(labels)-1,size=17)
        if j:arrow(ax,(xs[j-1]+w/2+1,y),(x-w/2-1,y))
        tag(ax,x,64,f'{j+1:02d}',size=13)
        if sub:txt(ax,x,29,sub[j],15,color=MUTED)
    save(fig,n)
def paired_rows(n,title,pairs,foot):
    fig,ax=frame(n,title,foot,'问题与测量');ys=np.linspace(65,24,len(pairs))
    for j,((left,right),y) in enumerate(zip(pairs,ys)):
        node(ax,23,y,29,10,left,accent=j==0,size=18);arrow(ax,(39,y),(47,y));txt(ax,51,y,right,18,ha='left')
    save(fig,n)
def plot_frame(n,title,foot,xlabel,ylabel):
    fig,ax=frame(n,title,foot,'教学曲线 · 非原始数据')
    p=fig.add_axes([.14,.265,.77,.42],facecolor=PAPER)
    for k in ['top','right']:p.spines[k].set_visible(False)
    for k in ['left','bottom']:p.spines[k].set_color('#8f9ca0');p.spines[k].set_linewidth(1)
    p.tick_params(colors=MUTED,labelsize=13,length=4,pad=8)
    p.set_xlabel(xlabel,fontsize=15,labelpad=12,color=INK);p.set_ylabel(ylabel,fontsize=15,labelpad=10,color=INK)
    p.grid(axis='y',color=LINE,lw=.6,alpha=.65);p.set_axisbelow(True)
    return fig,ax,p
def legend(p,ncol=2):p.legend(frameon=False,fontsize=13,loc='lower left',bbox_to_anchor=(0,1.025),ncol=ncol,handlelength=2.6,columnspacing=2)
def finish_plot(fig,p,n):
    # Include axes text in the bounds audit.
    TEXT.extend([p.xaxis.label,p.yaxis.label,*p.get_xticklabels(),*p.get_yticklabels(),*p.texts]);save(fig,n)

def main():
    # Artistic interpretation of separate cells; no anatomical or measurement claims.
    fig,ax=frame(2,'神经元的“黑色森林”','Cajal 绘图语言的艺术性重绘；非历史原图，非解剖比例图。','科学史 · 意象插页')
    im=plt.imread(ROOT/'illustrations/neuron-forest.png');a=fig.add_axes([.1,.17,.8,.58]);a.imshow(im);a.axis('off');txt(ax,50,15.5,'相互靠近，并不等于彼此连续。',16,color=COPPER);save(fig,2)
    timeline(3,'1906 · 同一奖台上的两种解释',[
        ('10 DEC','颁奖典礼','Golgi 与 Cajal\n共同获奖'),('11 DEC','Golgi 诺奖演讲','网状连续结构\n与细胞之间的联系'),('12 DEC','Cajal 诺奖演讲','独立的细胞单元\n与神经元之间的边界')], '同获奖项，不意味着对神经系统的解释已经一致。')
    timeline(4,'从黑色反应到神经元学说',[
        ('1873','Golgi · 黑色反应','少数神经元被完整染黑\n逐细胞追踪成为可能'),('1888','Cajal · 形态观察','鸟类神经中枢的观察\n支持独立细胞单元'),('1906','共同获诺贝尔奖','共享同一奖台\n仍持不同理论解释')], '技术可以由一个人发明，证据却可能超出发明者原先的解释。')
    timeline(5,'从整合反射到单纤维脉冲',[
        ('1906','Sherrington','系统讨论反射、抑制\n与神经系统整合'),('1926','Adrian','稳定记录单根感觉纤维\n联系刺激与放电频率'),('1932','共同获诺贝尔奖','从整体整合到单元活动\n共同研究神经元功能')], '把复杂系统压缩为可测量的现象，再将局部规律放回整体。')
    fig,ax=frame(6,'1932 · 从反射到脉冲','Sherrington 与 Adrian：关于神经元功能的发现。','科学史 · 研究现场')
    x=np.linspace(8,92,1500);y=np.full_like(x,48.)
    for c in [16,32,48,64,80]:y+=17*np.exp(-((x-c)/.55)**2)-5*np.exp(-((x-c-1.5)/1.2)**2)
    ax.plot(x,y,color=BLUE,lw=2.2);line(ax,(8,48),(92,48),LINE,.7);tag(ax,50,69,'被放大的微小活动，成为可以记录的信号。',size=18)
    node(ax,50,29,77,15,'单纤维脉冲记录  ×  神经系统整合',accent=True,size=22);save(fig,6)
    timeline(8,'Vagusstoff · 一个尚未命名的物质',[
        ('1921','Loewi','蛙心灌流实验\n支持可扩散的中介物质'),('1930s','Dale 等','乙酰胆碱与化学传递\n证据逐步扩展'),('1936','共同获诺贝尔奖','Dale 与 Loewi\n神经冲动的化学传递')], '把不可见的机制，变成可以转移、比较与重复的效应。')
    timeline(10,'巨轴突与可计算的动作电位',[
        ('1939','细胞内记录','乌贼巨轴突中\n记录动作电位'),('1952','Hodgkin–Huxley','把 Na⁺ / K⁺ 电流\n写成动力学模型'),('1963','诺贝尔奖','Eccles、Hodgkin\n与 Huxley 共享奖项')], '机制模型不仅描述曲线，也需预测改变条件以后会发生什么。')
    timeline(12,'从卧室实验室到神经生长因子',[
        ('1938','都灵','离开正常学术岗位\n在家建立实验单元'),('1951','小鼠肉瘤效应','肿瘤诱导鸡胚\n感觉与交感神经生长'),('1954','NGF 证据链','Cohen、Levi-Montalcini\n与 Hamburger 推进鉴定'),('1986','诺贝尔奖','Levi-Montalcini\n与 Cohen 共同获奖')], '研究未知因子时，可靠而灵敏的功能测定同样重要。')
    timeline(14,'把世界旋转 180°',[
        ('1943','旋转视野实验','打乱空间关系\n观察再生后的行为'),('1944','视神经再生','再生不等于重新学习\n任意的一套连接'),('1963','化学亲和假说','将有序连接\n写成可检验的解释')], '关键是让竞争性解释，在改变条件后给出不同预测。')
    timeline(15,'从病灶到皮层地图',[
        ('1861','Broca','Tan 病例：语言产生\n与左额叶病灶'),('1874','Wernicke','语言理解受损\n提示可分离的过程'),('1909','Brodmann','细胞构筑差异\n形成经典皮层分区'),('1937','Penfield / Boldrey','清醒手术中的电刺激\n描绘运动与感觉')], '定位回答“在哪里”，也引出“在其中发生什么”的问题。')
    timeline(16,'功能定位：四种相互补充的证据',[
        ('1861','Broca · 病灶病例','损伤—语言产生'),('1874','Wernicke · 功能分解','理解—表达的分离'),('1909','Brodmann · 组织结构','细胞构筑—皮层分区'),('1930s–50s','Penfield · 直接刺激','刺激—可观察反应')], '单一证据不能建立完整定位解释，需要不同层次相互检验。')
    timeline(18,'一条斜线改变了视觉研究',[
        ('1959','感受野论文','描绘视觉皮层\n单细胞感受野'),('1962','功能结构','方向、双眼交互\n与功能构筑'),('1963','视觉剥夺','研究关键期\n与经验依赖可塑性'),('1981','诺贝尔奖','Hubel、Wiesel\n与 Sperry 同年获奖')], '异常现象可能提醒我们：需要改变的，是对重要变量的定义。')
    experiments()
    charts()
    comparisons()
    concepts()
    audit=ROOT/'illustrations/render-audit.json'
    prior=json.loads(audit.read_text()) if audit.exists() else []
    merged=[x for x in prior if x['figure'] not in SELECT]+ALL
    audit.write_text(json.dumps(sorted(merged,key=lambda x:x['figure']),ensure_ascii=False,indent=2)+'\n')
    assert {x['figure'] for x in ALL}==SELECT, sorted(SELECT-{x['figure'] for x in ALL})
    bad=[x for x in ALL if x['layout_issues']]
    print(json.dumps({'figures':len(ALL),'layout_issues':[(x['figure'],x['layout_issues']) for x in bad]},ensure_ascii=False))

if __name__=='__main__':
    # The remaining drawing functions are defined in a separate, readable source file.
    exec((ROOT/'illustrations/drawings.py').read_text(),globals())
    main()
