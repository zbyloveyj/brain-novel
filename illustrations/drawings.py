"""Content-specific vector plates; imported by render.py."""

def experiments():
    fig,ax=frame(7,'Loewi · 让效应随灌流液转移','教学性重绘；保留刺激、灌流液转移与第二颗心的反应关系。','实验逻辑')
    for x,k in [(25,'第一颗蛙心'),(76,'第二颗蛙心')]:
        txt(ax,x,68,k,20);ax.add_patch(FancyBboxPatch((x-12,34),24,25,boxstyle='round,pad=0,rounding_size=1',fc='#fffefa',ec=BLUE,lw=2))
        ax.add_patch(Rectangle((x-11.8,34.2),23.6,9,fc='#e0ebe8',ec='none'));line(ax,(x-11,43),(x+11,43),TEAL,1.2)
        ax.add_patch(Ellipse((x,48),7,13,fc=SAND,ec=COPPER,lw=2));line(ax,(x-1,54),(x-5,64),COPPER,2)
    tag(ax,23,73,'刺激迷走神经',size=16);arrow(ax,(39,48),(62,48),COPPER);txt(ax,50,55,'转移灌流液',16)
    for x,c,l in [(25,BLUE,'心率减慢'),(76,COPPER,'第二颗心也减慢')]:
        t=np.linspace(x-12,x+12,400);v=np.zeros_like(t)
        for center in [x-9,x-3,x+6]:v+=4*np.exp(-((t-center)/.22)**2)
        ax.plot(t,26+v,color=c,lw=1.5);txt(ax,x,20,l,17)
    save(fig,7)
    fig,ax=frame(9,'巨轴突 · 从记录曲线走向离子机制','教学示意；1939 年的细胞内记录显示，冲动期间膜电位可出现超射。','实验与机制')
    ax.add_patch(Ellipse((27,47),25,31,fc=TINT,ec=BLUE,lw=2));ax.add_patch(Ellipse((27,47),17,31,fc='#fffefa',ec='#b5c5c8',lw=1.1))
    arrow(ax,(9,68),(26,47),COPPER);txt(ax,24,71,'玻璃微电极',16);line(ax,(27,47),(44,47),COPPER,2);txt(ax,27,25,'乌贼巨轴突 ≈ 0.5 mm',16)
    p=fig.add_axes([.57,.32,.34,.34],facecolor=PAPER);x=np.linspace(0,1,350);v=-60+103*np.exp(-((x-.30)/.08)**2)-13*np.exp(-((x-.62)/.14)**2)
    p.plot(x,v,color=COPPER,lw=2.6);p.axhline(0,color=TEAL,lw=1,ls='--');p.set(ylim=(-85,55),xticks=[],yticks=[-60,0,40]);p.tick_params(labelsize=13);p.spines[['top','right','bottom']].set_visible(False);p.spines['left'].set_color(LINE)
    tag(ax,74,71,'膜电位越过 0 mV',size=17);txt(ax,72,24,'Na⁺ 内流 → K⁺ 外流',17);txt(ax,94,62,'mV',13,color=MUTED);save(fig,9)
    fig,ax=frame(11,'NGF · 把生长变成可比较的读出','先建立灵敏的功能测定，再追问活性物质是什么。','实验逻辑')
    rng=np.random.default_rng(11)
    for x,count,length,label in [(26,15,8,'对照：较短突起'),(76,40,17,'加入含 NGF 的提取物')]:
        for a in np.linspace(0,2*np.pi,count,endpoint=False):
            r=length*rng.uniform(.7,1);line(ax,(x+3*np.cos(a),48+4*np.sin(a)),(x+r*np.cos(a),48+r*np.sin(a)),COL[int(a*3)%3],1.1)
        ax.add_patch(Ellipse((x,48),9,12,fc='#fffefa',ec=BLUE,lw=2));txt(ax,x,23,label,17)
    arrow(ax,(43,48),(55,48),COPPER);txt(ax,50,66,'可扩散的生长因子',18,color=COPPER);save(fig,11)
    fig,ax=frame(13,'Sperry · 旋转视野，检验连接','图示仅保留旋转、再生与有序连接的实验逻辑，非完整视路。','实验逻辑')
    for y in [61,34]:
        ax.add_patch(Ellipse((25,y),20,17,fc='#fffefa',ec=BLUE,lw=1.7));ax.scatter([20,30],[y+3 if y==61 else y-3]*2,color=BLUE,s=60)
    arrow(ax,(40,60),(40,35),COPPER,rad=-.35);tag(ax,49,48,'180°',size=20);tag(ax,25,72,'旋转眼球',size=17);arrow(ax,(13,31),(8,25));txt(ax,26,20,'向相反方向扑击',16)
    for x in [67,90]:
        ax.add_patch(FancyBboxPatch((x-4,30),8,36,boxstyle='round,pad=0,rounding_size=2',fc=TINT,ec=BLUE,lw=1.5))
    for y in [35,46,57,63]:
        ax.scatter([67,90],[y,y],s=35,color=COPPER);line(ax,(68,y),(89,y),BLUE,1.3)
    txt(ax,67,23,'视网膜',16);txt(ax,90,23,'视顶盖',16);txt(ax,78,72,'视神经再生',17);save(fig,13)
    fig,ax=frame(17,'同一神经元，偏好不同方向的边缘','方向选择性的教学示意；脉冲数为人工安排，不是原始记录。','刺激与反应')
    for j,(ang,nspike) in enumerate([(0,4),(45,17),(90,6),(135,2)]):
        x=16+j*23;node(ax,x,56,18,23,'',accent=j==1)
        a=np.deg2rad(ang);line(ax,(x-6*np.cos(a),56+9*np.sin(a)),(x+6*np.cos(a),56-9*np.sin(a)),INK,3)
        txt(ax,x,38,f'{ang}°',17);line(ax,(x-8,26),(x+8,26),LINE)
        for t in np.linspace(x-7,x+7,nspike):line(ax,(t,26),(t,31),COPPER if j==1 else BLUE,1)
        txt(ax,x,20,'强反应' if j==1 else '弱反应',16,color=COPPER if j==1 else MUTED)
    save(fig,17)
    fig,ax=frame(24,'分散的来源，可以汇聚到共同位置','三种假设受体类别；示意投射关系，不是完整嗅球结构。','连接与身份')
    txt(ax,21,70,'嗅上皮',21);txt(ax,75,70,'嗅球',21)
    for j,y in enumerate(np.linspace(62,23,6)):
        k=[0,1,0,2,1,2][j];color=COL[k];ax.scatter([25],[y],s=110,color=color,marker=['o','s','^'][k]);txt(ax,16,y,f'细胞 {j+1}',15)
        target=[59,43,27][k];arrow(ax,(28,y),(69,target),color,dashed=['-','--',':'][k])
    for k,y in enumerate([59,43,27]):
        ax.scatter([73],[y],s=360,color=COL[k],marker=['o','s','^'][k]);txt(ax,85,y,f'类型 {k+1}\n汇聚节点',16)
    save(fig,24)
    fig,ax=frame(27,'表达筛选 · 逐层追踪响应','材料分组为教学示意；候选功能仍需独立验证。','实验逻辑')
    for x,y,w,h,s,a in [(50,65,24,10,'文库材料',False),(25,47,24,10,'材料组 A',False),(73,47,24,10,'材料组 B',True),(60,28,17,10,'B1',False),(85,28,17,10,'B2',True)]:node(ax,x,y,w,h,s,a)
    arrow(ax,(46,59),(28,53));arrow(ax,(54,59),(69,53));arrow(ax,(70,41),(62,34));arrow(ax,(77,41),(83,34));txt(ax,24,34,'无响应：先排查条件',15,color=MUTED);txt(ax,73,39,'有响应，继续分开',13,color=COPPER);txt(ax,60,19,'无响应',15);txt(ax,85,19,'单个候选',15,color=COPPER);save(fig,27)
    fig,ax=frame(47,'镜描 · 视觉与动作关系发生改变','教学性路径图；非原装置比例复刻，不作为临床测验标准。','任务与反馈')
    line(ax,(51,21),(51,67),COPPER,2);txt(ax,51,71,'镜面',17,color=COPPER)
    theta=np.linspace(np.pi/2,np.pi/2+2*np.pi,11);rr=np.array([10,4.6]*5+[10]);x=rr*np.cos(theta);y=rr*np.sin(theta)
    for center,c in [(25,BLUE),(78,TEAL)]:
        ax.plot(center+x,46+y,color=c,lw=2);ax.plot(center+x*.82,46+y*.82,color=COPPER,lw=1.1,alpha=.8)
    txt(ax,25,65,'不能直接看手',16);txt(ax,25,29,'纸上星形路径',16);txt(ax,78,65,'所见镜面反馈',16);txt(ax,78,29,'根据反馈调整',16);arrow(ax,(26,22),(24,38),BLUE);txt(ax,25,18,'手的动作',14);save(fig,47)
    fig,ax=frame(54,'共享一个胞体，局部突触仍可不同','分叉培养模型的比较逻辑；非完整神经元形态或记忆存储模型。','局部与整体')
    ax.add_patch(Ellipse((18,46),13,17,fc=TINT,ec=BLUE,lw=1.8));ax.add_patch(Circle((18,46),2,fc=BLUE));line(ax,(24,46),(45,46),BLUE,2)
    for y,c in [(64,COPPER),(29,TEAL)]:
        line(ax,(45,46),(70,y),c,2);line(ax,(70,y),(80,y),c,2);ax.add_patch(Ellipse((86,y),9,12,fc='#fffefa',ec=c,lw=1.6))
    arrow(ax,(55,70),(66,64),COPPER);txt(ax,46,73,'分支 A：局部处理',16,color=COPPER);txt(ax,56,22,'分支 B：未作相同处理',16,color=TEAL);txt(ax,18,30,'感觉神经元',16);txt(ax,86,53,'运动细胞 A',15);txt(ax,86,19,'运动细胞 B',15);txt(ax,48,39,'局部过程与细胞核过程协作',14,color=MUTED);save(fig,54)
    fig,ax=frame(56,'周期性的空间活动', '人工三角格点等值线；不是行走轨迹，也不是原始实验记录。','空间示意')
    p=fig.add_axes([.27,.245,.46,.45],facecolor=PAPER);xx,yy=np.meshgrid(np.linspace(0,5,350),np.linspace(0,4,300));z=np.zeros_like(xx)
    for row in range(-1,7):
        for col in range(-1,7):z+=np.exp(-((xx-col-(row%2)*.5)**2+(yy-row*.866)**2)/.06)
    p.contour(xx,yy,z,levels=[.18,.42,.7],colors=[TEAL,GOLD,BLUE],linewidths=1.5);p.set_aspect('equal');p.set(xticks=[],yticks=[]);p.set_xlabel('场地横向位置（示意）',fontsize=15,labelpad=10);p.set_ylabel('场地纵向位置（示意）',fontsize=15,labelpad=10)
    for s in p.spines.values():s.set_color(LINE)
    save(fig,56)
    fig,ax=frame(57,'把环境改变与活动改变分别记录','圆圈表示假想活动区域，粗线表示被操纵的线索；结果不代表普遍模式。','空间与条件')
    for x,xx,yy,k in [(27,24,38,'原环境'),(75,80,52,'改变线索后')]:
        ax.add_patch(Rectangle((x-15,28),30,33,fc='#fffefa',ec=BLUE,lw=2));ax.add_patch(Ellipse((xx,yy),8,10,fill=False,ec=COPPER,lw=2));txt(ax,x,68,k,20)
    line(ax,(12,61),(21,61),INK,5);line(ax,(90,54),(90,61),INK,5);arrow(ax,(46,45),(56,45),COPPER);save(fig,57)
    fig,ax=frame(59,'蜂舞 · 在两种坐标中表达方向','角度仅作示意，非实测数据；气味、距离与后续搜索仍参与行为。','参照与转换')
    for x,left,right in [(27,'太阳方向','食物方向'),(76,'向上','摇摆段')]:
        arrow(ax,(x,27),(x,65));arrow(ax,(x,27),(x+14,55),COPPER);ax.add_patch(Arc((x,27),16,20,theta1=47,theta2=90,ec=COPPER,lw=1.2));txt(ax,x+4,41,'θ',22,color=COPPER);txt(ax,x,70,left,16);txt(ax,x+14,60,right,16)
    txt(ax,27,20,'蜂箱外：相对太阳',18);txt(ax,76,20,'巢脾上：相对竖直',18);arrow(ax,(46,47),(58,47));txt(ax,52,55,'关系转换',14);save(fig,59)
    fig,ax=frame(60,'地标移动，搜索位置怎样改变', '三角形为人为地标，虚线为假想搜索区域；布局不还原某次实际试验。','实验逻辑')
    for x,label in [(27,'原地标位置'),(76,'移动后的地标')]:
        txt(ax,x,68,label,20);ax.scatter([x-10,x+10,x-10,x+10],[52,52,32,32],s=180,marker='^',facecolors=PAPER,edgecolors=BLUE,lw=1.8);ax.add_patch(Ellipse((x,42),16,20,fc='none',ec=COPPER,lw=1.7,ls='--'))
    ax.scatter([27,68],[42,42],s=45,color=INK);arrow(ax,(46,42),(56,42));txt(ax,27,22,'巢口保持原处',17);txt(ax,76,22,'搜索随地标偏移',17);save(fig,60)
    fig,ax=frame(67,'从空间分布到投影信息','人工几何模型；多个方向的空间编码信息共同参与图像重建。','测量与重建')
    ax.add_patch(Rectangle((10,26),27,36,fc='#fffefa',ec=BLUE,lw=1.5));ax.add_patch(Ellipse((20,40),7,10,fc=TINT,ec=BLUE,lw=1.7));ax.add_patch(Ellipse((28,52),11,15,fc=SAND,ec=COPPER,lw=1.7));txt(ax,24,69,'人工几何模型',19);arrow(ax,(41,44),(52,44))
    x=np.linspace(59,93,350);v=16*np.exp(-((x-68)/3)**2)+23*np.exp(-((x-84)/4.2)**2);line(ax,(57,28),(95,28),LINE);ax.plot(x,28+v,color=BLUE,lw=2.4);txt(ax,76,69,'一个方向的投影示意',19);save(fig,67)

def comparisons():
    table(23,'筛选依据，也需要接受检验',['候选','家族性','结构相容','嗅上皮表达'],[
        ['A','✓','—','—'],['B','✓','✓','—'],['C','—','✓','✓'],['D','✓','✓','✓'],['E','—','—','✓'],['F','✓','—','✓']], 'A–F 为虚构候选；D 满足设定条件，仍不是功能证明。')
    table(30,'不同读数，不宜直接互相替代',['研究层次','通道电流','动物动作','本人报告'],[
        ['表达细胞实验','✓','—','—'],['动物行为研究','—','✓','—'],['人的感觉测试','—','—','✓']], '此表为通常直接测得对象的示意；跨尺度联系需要额外证据。',[1.4,1,1,1])
    table(32,'观察状态，也要记录时间与恢复',['观察维度','干预前','干预期间','干预后'],[
        ['运动与姿势','记录基线','记录变化','是否恢复'],['呼吸与瞳孔','记录基线','是否协同变化','持续多久'],['解释边界','未测不等于无','行为不等于体验','复查与重复']], '概念性观察表，未填入历史实验数据；多种反应共同限定解释。')
    table(36,'救援、化学测量与转化回答不同问题',['问题','观察 / 操作','不能独自证明'],[
        ['前体能否恢复行为','比较不同前体效果','全部疾病机制'],['化学含量怎样变化','测定、空白与身份核对','实时释放与受体响应'],['人的疾病是否相关','组织证据与临床研究','症状改善就是根治']], '证据比较表，不是临床疗效数据。',[1,1.1,1.05])
    table(53,'证明长期改变，不能只看当时',['比较条件','短时观察','较晚观察','基础状态'],[
        ['短暂调节','记录变化','是否维持？','必须检查'],['重复调节','记录变化','是否维持？','必须检查'],['重复＋合成干预','是否保留？','是否受影响？','必须检查']], '需要下一时点与适当对照，并排除系统整体受损。',[1.2,1,1,1])
    table(64,'输入和输出方式，都要写清楚',['短暂视觉输入','口头报告','非语言选择'],[
        ['左侧视野','某些任务中困难','左手可提供另一通路'],['右侧视野','常较易命名','仍需具体任务验证']], '仅概括部分经典任务；不是所有患者的能力表。',[1,1.1,1.4])

def concepts():
    fig,ax=frame(31,'需要与行动，构成反馈关系','简化概念图；感官线索也可提前参与，不是单向发令。','反馈与调节')
    for x,l in [(19,'身体内部状态\n水分、能量等'),(50,'神经系统整合\n内部信号与环境线索'),(81,'行为与自主调节\n寻找、饮食、循环等')]:node(ax,x,59,27,17,l,size=16)
    arrow(ax,(33,59),(35,59));arrow(ax,(64,59),(67,59));node(ax,50,29,43,15,'行动的后果\n身体条件与外部环境改变',True,size=18);arrow(ax,(79,49),(72,30),rad=-.15);arrow(ax,(27,29),(18,49),rad=-.25);save(fig,31)
    fig,ax=frame(34,'更精细的干预，让问题更具体','分辨率提高，不意味着所有机制解释自动成立。','干预与解释')
    node(ax,27,60,37,17,'区域干预\n改变哪些可观察结果？');node(ax,75,60,37,17,'细胞类型干预\n谁在何种条件下参与？',True)
    node(ax,27,30,37,17,'替代解释\n纤维、状态、动作能力',size=17);node(ax,75,30,37,17,'证据限制\n充分性、必要性、特异性',size=17);arrow(ax,(47,60),(55,60));arrow(ax,(27,50),(27,40));arrow(ax,(75,50),(75,40));save(fig,34)
    fig,ax=frame(35,'多巴胺 · 中间位置不等于次要功能','简化的儿茶酚胺合成关系；不是用药流程。','生化路径')
    labels=['酪氨酸','DOPA','多巴胺','去甲肾上腺素'];xs=[15,38,61,85]
    for j,(x,l) in enumerate(zip(xs,labels)):
        node(ax,x,53,20,13,l,accent=j==2,size=18)
        if j:arrow(ax,(xs[j-1]+11,53),(x-11,53))
    arrow(ax,(38,29),(38,45),COPPER);txt(ax,38,23,'前体补充',17);txt(ax,76,37,'末段仅在具有相应酶\n的细胞中发生',16,color=MUTED);save(fig,35)
    chain(38,'把多巴胺研究拆成四个测量层次',['组织含量\n有多少？','时空释放\n何时、何地？','细胞响应\n受体及胞内过程','行为表现\n做了什么？'],'每一段联系都需相应证据；静态含量、瞬时信号与心理概念不能直接互换。')
    cycle(40,'分子计时，依赖反馈与时间顺序',['基因转录\n与 RNA 产生','蛋白产生\n积累与修饰','复合物\n与核内调节','抑制减弱\n下一周期开始'],'简化环路；不表示 PER 直接结合自身基因并单独关闭转录。','反馈、延迟与降解')
    timeline(42,'从异常节律到分子机制',[
        ('1971','遗传改变','与行为周期'),('1984','基因转移','恢复节律'),('1988–1990','PER 与 RNA','随时间变化'),('1994–1998','TIM、核定位','与蛋白稳定性'),('2004','组织节律','实时报告'),('2017','三位研究者','共同获诺贝尔奖')],'时间线择要整理；间距不代表年数，获奖并非实验完成日期。')
    paired_rows(46,'学习研究中的四种提问',[('生理测量','发生了什么变化？'),('关系操纵','哪一种安排改变预期？'),('回路干预','哪些环节参与反应？'),('神经记录','哪些活动与预测有关？')],'这些证据层次相连，也需要各自的测量与检验。')
    vertical(49,'同一病例，解剖解释继续更新',[
        '1957  ·  手术报告与行为测验\n早期的范围描述与功能推断','1997  ·  磁共振成像\n重新观察保留组织与损伤范围','2014  ·  组织切片与三维重建\n在更细尺度修订解剖解释'],'不把 H.M. 简化为“只缺海马”；不同证据提供不同分辨率。')
    paired_rows(50,'先写任务，再写“记忆”',[('即时维持','眼前材料能保持多久？'),('事件回忆','能否回想何时做过？'),('技能学习','练习是否改变后续表现？'),('既有知识','哪些过去的知识仍能使用？')],'材料、间隔、干扰与回答方式，都需要明确交代。')
    fig,ax=frame(51,'动作变化，还需追到传递与回路','部分回路示意；仍需检查感觉适应、肌肉状态、其他回路与测量稳定性。','部分回路')
    xs=[15,39,63,87]
    for j,(x,l) in enumerate(zip(xs,['感觉输入','感觉神经元','运动神经元','鳃的收缩'])):
        node(ax,x,39,20,13,l,accent=j==3,size=18)
        if j:arrow(ax,(xs[j-1]+11,39),(x-11,39))
    node(ax,51,65,28,11,'调节性输入',True);arrow(ax,(51,59),(51,40),COPPER);tag(ax,51,24,'从可见的动作，追问部分连接的变化。',size=18);save(fig,51)
    hub(58,'空间表征，涉及多类变量与细胞群','身体在空间中\n行动',['所在位置','头部方向','边界关系','运动信息'],'箭头为概念参与关系，不是已完整重建的单向回路。')
    quadrants(61,'同一个行为，有不同的“为什么”',[
        ('机制','此刻怎样发生'),('个体发育','一生中怎样形成'),('功能','在环境中有什么后果'),('演化历史','不同谱系怎样变化')],'廷伯根四问的阅读框架；一种答案不能替代其余问题。')
    fig,ax=frame(62,'共享信息，不等于共享一个大脑','个体、信号与环境共同影响行为；不把蜂舞与人类语言当作同一机制。','交流与行为')
    for j,(x,l) in enumerate([(20,'采集者\n取得经验'),(50,'信号\n动作与气味'),(80,'接受者\n改变行动')]):
        node(ax,x,57,25,18,l,accent=j==1)
        if j:arrow(ax,(x-45+28,57),(x-14,57))
    node(ax,50,27,62,12,'环境线索、个体状态与既有经验',size=18);arrow(ax,(27,34),(20,47));arrow(ax,(73,34),(80,47));save(fig,62)
    fig,ax=frame(63,'视野与半球：不是“左眼 / 右眼”','每只眼睛都接收左右两侧视野的信息；经典任务需保持中央注视。','输入与通路')
    node(ax,27,62,34,12,'左侧视野');node(ax,75,62,34,12,'右侧视野',True);node(ax,27,28,34,14,'左半球视觉系统',True);node(ax,75,28,34,14,'右半球视觉系统');arrow(ax,(29,55),(73,36),BLUE);arrow(ax,(73,55),(29,36),COPPER);txt(ax,50,46,'＋',22,color=MUTED);save(fig,63)
    fig,ax=frame(65,'连贯的解释，仍可能缺少证据','阅读“解释器”研究的方法提示；不把错误报告一概等同于故意说谎。','解释与证据')
    for j,(x,l) in enumerate([(20,'已有的\n局部信息'),(50,'形成解释\n补足关系'),(80,'连贯叙述\n不等于证实')]):
        node(ax,x,58,25,18,l,accent=j==2)
        if j:arrow(ax,(x-17,58),(x-14,58))
    node(ax,50,28,61,13,'独立检验：遗漏了哪些信息？',True);arrow(ax,(50,48),(50,36));save(fig,65)
    vertical(66,'从观察到意识命题，还有推断距离',[
        '观察：特定条件下，报告与选择分离','推断：某类信息的传递或可达性受限','更强命题：一个人的意识是否由此分成两个？'],'更强命题仍需论证，不能只凭前一层结果自动解决。',dashed=True)
    cycle(68,'MRI 发展中的不同环节',['核磁共振\n可测得信号','梯度编码\n区分位置','快速采集\n取得时空信息','重建与检查\n形成可解释图像'],'教学性组织，不表示所有研究按一条直线发生。','测量、编码与重建',closed=False)
    fig,ax=frame(70,'共同影响，可以改变观测相关','相关可能包含共同来源；此图不是特定数据集的因果结论。','测量与解释')
    node(ax,50,65,42,12,'头动 / 共同生理波动',True);node(ax,25,30,37,15,'区域甲的测得信号');node(ax,77,30,37,15,'区域乙的测得信号');arrow(ax,(43,58),(27,39));arrow(ax,(57,58),(75,39));arrow(ax,(45,30),(57,30),style='<->',dashed=True);save(fig,70)
    hub(71,'疗效，需要说明由谁、怎样判断','“好一些”\n由谁判断？',['症状与痛苦','日常自主','认知与意愿','关系与照护'],'多个结局可能同向，也可能冲突；不提供个体或手术疗效评分。')
    fig,ax=frame(72,'未知的结局，需要保留为未知','追踪不完整会影响获益与损害的估计；不虚构病例数或成功率。','随访与结局')
    node(ax,50,67,39,11,'最初进入记录的人');node(ax,27,46,38,11,'能获得后续资料');node(ax,75,46,38,11,'后续情况未知',True);arrow(ax,(45,60),(29,52));arrow(ax,(55,60),(73,52));node(ax,27,24,38,12,'改善 / 未改善 / 不良结局',size=16);node(ax,75,24,38,12,'不能自动归入“成功”',True,size=17);arrow(ax,(27,39),(27,31));arrow(ax,(75,39),(75,31),dashed=True);save(fig,72)
    vertical(73,'保护原则，有各自的时代背景',['1947  ·  纽伦堡法典','1977  ·  精神外科报告','1979  ·  贝尔蒙报告','2024  ·  赫尔辛基宣言修订'],'仅列本章使用节点；年代间距不按比例，也非现行法规完整目录。')
    fig,ax=frame(74,'开放性观察与随机比较，推断不同','需结合入组、随访、风险与终点；不是针对特定适应证的结论。','研究设计')
    node(ax,25,65,35,11,'开放性治疗观察');node(ax,25,42,35,16,'治疗后变化\n包含多种可能来源');arrow(ax,(25,58),(25,51));txt(ax,25,23,'有价值，但不能\n独自证实因果',17,color=MUTED)
    node(ax,75,65,35,11,'随机、盲法比较',True);node(ax,64,42,18,11,'干预组');node(ax,87,42,18,11,'对照组');arrow(ax,(72,59),(65,48));arrow(ax,(78,59),(86,48));node(ax,75,21,39,10,'按规定时间与终点比较',size=16);arrow(ax,(65,36),(73,27));arrow(ax,(87,36),(78,27));save(fig,74)
    vertical(76,'主动任务，让某种能力显现',['听见并理解指令','保持注意，完成特定想象','记录中形成可重复区分','谨慎判断是否支持某种能力'],'任何环节受阻都可能影响结果；阴性结果不能自动等同于没有意识。')
    fig,ax=frame(77,'清醒、经验与报告，分别研究','三者相互关联，但不能相互替代；此图不是诊断分型或强弱量表。','概念区分')
    node(ax,26,60,39,17,'清醒状态\n睁眼、睡眠与唤醒');node(ax,77,60,37,17,'经验内容\n正在经历什么',True);node(ax,51,28,42,17,'报告与执行\n能否让外界知道');arrow(ax,(47,60),(57,60),style='<->',dashed=True);arrow(ax,(31,50),(43,38),style='<->',dashed=True);arrow(ax,(72,50),(59,38),style='<->',dashed=True);save(fig,77)
    fig,ax=frame(78,'让理论分歧，落到可检验的预测','回到具体命题、操作化与测量；不能仅比较理论声望。','对抗性检验')
    node(ax,26,66,38,11,'理论甲的具体预测');node(ax,76,66,38,11,'理论乙的具体预测',True);node(ax,51,43,77,12,'事先约定：任务、指标、分析与判断');node(ax,51,21,77,12,'新数据：支持哪些、挑战哪些、还缺什么');arrow(ax,(29,59),(44,50));arrow(ax,(73,59),(58,50));arrow(ax,(51,36),(51,28));save(fig,78)
    paired_rows(79,'同一个大脑，对应不同层次的问题',[('结构','对象怎样组成'),('功能','在什么条件下做什么'),('形成过程','怎样发育、学习与改变'),('人的生活','能力、体验与关系')],'这些层次彼此相连，但并不意味着所有因果联系已经证实。')
    fig,ax=frame(80,'探索和确认，留下可追踪的边界','同一批资料上的选择结果，不能再次称为独立验证。','研究与验证')
    node(ax,26,58,37,20,'探索资料\n发现候选关系');node(ax,77,58,37,20,'独立资料\n检验约定预测',True);arrow(ax,(46,58),(57,58));txt(ax,51,72,'假设与方案',17,color=COPPER);node(ax,51,26,78,13,'分开记录：事先决定 / 后来修改',size=19);arrow(ax,(29,47),(40,34));arrow(ax,(75,47),(61,34));save(fig,80)
    fig,ax=frame(82,'从细胞的信号，回到人的生活','连线表示全书叙事推进，不是大脑唯一的信息流或完成的意识理论。','全书路线')
    loc=[(19,62),(50,62),(81,62),(81,29),(50,29),(19,29)]
    labs=['细胞与信号','感觉与行动','学习与记忆','空间与协作','测量与解释','人的生活']
    for j,((x,y),l) in enumerate(zip(loc,labs)):
        node(ax,x,y,26,15,l,accent=j==5);tag(ax,x,y+12,f'{j+1:02d}',size=13)
    for a,b in [((33,62),(36,62)),((64,62),(67,62)),((81,53),(81,38)),((67,29),(64,29)),((36,29),(33,29))]:arrow(ax,a,b)
    save(fig,82)

def cycle(n,title,labels,foot,center,closed=True):
    fig,ax=frame(n,title,foot,'过程与反馈' if closed else '测量与重建');loc=[(26,62),(76,62),(76,29),(26,29)]
    for j,((x,y),l) in enumerate(zip(loc,labels)):node(ax,x,y,37,17,l,accent=j==2,size=18)
    segments=[((46,62),(55,62)),((76,52),(76,39)),((56,29),(46,29))]
    if closed:segments.append(((26,39),(26,52)))
    for a,b in segments:arrow(ax,a,b)
    txt(ax,51,46,center,16,color=COPPER);save(fig,n)
def vertical(n,title,labels,foot,dashed=False):
    fig,ax=frame(n,title,foot,'证据与推断');ys=np.linspace(65,23,len(labels));h=13 if len(labels)>3 else 17
    for j,(y,l) in enumerate(zip(ys,labels)):
        node(ax,51,y,80,h,l,accent=j==len(labels)-1,size=17)
        if j:arrow(ax,(51,ys[j-1]-h/2-1),(51,y+h/2+1),dashed=dashed and j==len(labels)-1)
    save(fig,n)
def quadrants(n,title,items,foot):
    fig,ax=frame(n,title,foot,'观察框架')
    for j,(heading,desc) in enumerate(items):
        x=27+(j%2)*48;y=61-(j//2)*29;node(ax,x,y,39,22,heading+'\n'+desc,accent=j==0,size=19)
    save(fig,n)
def hub(n,title,center,labels,foot):
    fig,ax=frame(n,title,foot,'概念关系')
    node(ax,51,45,30,20,center,True,size=19)
    for (x,y),l in zip([(22,67),(80,67),(22,23),(80,23)],labels):
        node(ax,x,y,29,11,l,size=18)
        arrow(ax,(x+5 if x<50 else x-5,y-7 if y>45 else y+7),(41 if x<50 else 61,54 if y>45 else 36))
    save(fig,n)

def charts():
    fig,ax,p=plot_frame(19,'同一结构，不同高峰','归一化包络仅说明位置—频率关系；非原始记录，无真实长度或频率标定。','沿基底膜的位置（示意）','相对振幅（各自归一化）')
    x=np.linspace(0,1,500)
    for mu,sd,c,l in [(.18,.1,BLUE,'高频'),(.48,.14,COPPER,'中频'),(.78,.12,TEAL,'低频')]:
        y=np.exp(-((x-mu)/sd)**2/2)/(1+np.exp((x-mu-.08)/.025));y/=y.max();p.plot(x,y,color=c,lw=2.6,label=l)
    p.set(xlim=(0,1),ylim=(0,1.15),xticks=[0,1],xticklabels=['底部','顶端'],yticks=[0,.5,1]);legend(p,3);finish_plot(fig,p,19)
    fig,ax,p=plot_frame(20,'频闪 · 固定相位上的取样','标记为每隔一个完整周期取样的位置；仅解释原理，并非装置实测。','时间 / 振动周期（示意）','相对位移（任意单位）')
    x=np.linspace(0,4,600);p.plot(x,np.sin(x*2*np.pi),color=BLUE,lw=2,label='连续振动')
    for phase,c,m in [(.08,COPPER,'o'),(.25,TEAL,'s'),(.58,PLUM,'^')]:
        t=np.arange(phase,4,1);p.scatter(t,np.sin(t*2*np.pi),s=55,color=c,marker=m,label=f'相位 {phase:g}')
    p.set(xlim=(0,4),ylim=(-1.2,1.2),yticks=[-1,0,1]);legend(p,4);finish_plot(fig,p,20)
    fig,ax,p=plot_frame(21,'活体响应，不只是被动响应','两条曲线各自峰值归一化，不能比较绝对增益；均非原始实验曲线。','相对特征频率（示意）','相对振幅（各自归一化）')
    x=np.linspace(0,2.5,500)
    p.plot(x,np.exp(-((x-1)/.47)**2),color=BLUE,ls='--',lw=2.6,label='较宽的被动响应');p.plot(x,np.exp(-((x-1)/.13)**2),color=COPPER,lw=2.8,label='较尖锐的主动响应');p.set(xlim=(0,2.5),ylim=(0,1.1),yticks=[0,.5,1]);legend(p);finish_plot(fig,p,21)
    fig,ax,p=plot_frame(22,'脉冲计数相同，时间关系不同','两组人工脉冲各十个；用于说明计数可能遗漏时间信息。','刺激周期（示意）','')
    trains=[np.arange(.35,10,.98),np.array([.08,.85,1.25,2.5,3.15,3.47,5.05,6.2,7.65,9.6])]
    for y,t,c in [(1,trains[0],BLUE),(0,trains[1],COPPER)]:p.vlines(t,y-.14,y+.14,color=c,lw=2);p.axhline(y,color=LINE,lw=.6)
    p.set(xlim=(0,10),ylim=(-.45,1.5),yticks=[0,1],yticklabels=['相位分散\n10 个脉冲','近似锁相\n10 个脉冲']);p.tick_params(axis='y',labelsize=12);p.grid(False);finish_plot(fig,p,22)
    fig,ax=frame(25,'组合编码 · 同一行与列都可有响应','矩阵为人工设定；A–E 与 R1–R6 不对应具体化学物质或已命名受体。','教学矩阵 · 非原始数据')
    # Read the original categorical cell colours to recover its teaching matrix.
    # This is data extraction only; the new matrix is plotted natively below.
    from PIL import Image
    original=np.asarray(Image.open(ROOT/'docs/assets/figures/figure-025.webp').convert('RGB'))
    cmap=plt.get_cmap('viridis');palette=np.array([cmap(i/255)[:3] for i in range(256)])*255
    values=[]
    for row in range(6):
        vals=[]
        for col in range(5):
            rgb=original[int(102+(row+.5)*174.7),int(170+(col+.5)*296.6)].astype(float)
            val=np.linalg.norm(palette-rgb,axis=1).argmin()/255
            vals.append(round(val,2))
        values.append(vals)
    z=np.array(values);p=fig.add_axes([.22,.245,.55,.45]);cm=LinearSegmentedColormap.from_list('book',[PAPER,'#e3c8a7',COPPER,INK])
    im=p.imshow(z,vmin=0,vmax=1,cmap=cm,aspect='auto');p.set(xticks=range(5),xticklabels=list('ABCDE'),yticks=range(6),yticklabels=[f'R{i}' for i in range(1,7)]);p.tick_params(length=0,labelsize=14,pad=9)
    p.set_xlabel('假设的刺激',fontsize=15,labelpad=10);p.set_ylabel('假设的受体',fontsize=15,labelpad=12)
    p.set_xticks(np.arange(-.5,5),minor=True);p.set_yticks(np.arange(-.5,6),minor=True);p.grid(which='minor',color=PAPER,lw=3);p.tick_params(which='minor',length=0)
    for s in p.spines.values():s.set_visible(False)
    cb=fig.colorbar(im,cax=fig.add_axes([.81,.245,.015,.45]));cb.set_label('相对响应（人为设定）',fontsize=14,labelpad=14);cb.ax.tick_params(labelsize=12);cb.outline.set_visible(False);save(fig,25)
    fig,ax,p=plot_frame(26,'浓度改变时，受体组合也可能改变','人工剂量—响应曲线；不包含真实 EC50、亲和力或混合物相互作用。','浓度（任意单位；对数坐标）','相对响应（归一化）')
    x=np.logspace(-3,3,500)
    for k,c,l in [(.04,BLUE,'R1'),(1,COPPER,'R2'),(25,TEAL,'R3')]:p.plot(x,x/(x+k),color=c,lw=2.7,label=l)
    p.set_xscale('log');p.set(xlim=(1e-3,1e3),ylim=(0,1.05),xticks=np.logspace(-3,3,7),yticks=[0,.5,1]);legend(p,3);finish_plot(fig,p,26)
    fig,ax,p=plot_frame(28,'温度曲线，不等于疼痛刻度','教学性响应曲线，无真实温度标定、临床安全阈值或实验拟合含义。','温度方向（无真实温度标定）','相对响应（人为示意）')
    x=np.linspace(0,1,400)
    for m,c,st,l in [(.55,BLUE,'-','条件 A'),(.42,COPPER,'--','条件 B')]:p.plot(x,1/(1+np.exp(-(x-m)*16)),color=c,lw=2.6,ls=st,label=l)
    p.set(xlim=(0,1),ylim=(0,1.06),xticks=[0,1],xticklabels=['较低','较高'],yticks=[0,.5,1]);legend(p);finish_plot(fig,p,28)
    fig,ax,p=plot_frame(29,'增加与减少，是不同方向的证据','人工响应例子；不同背景须各设对照，无真实样本或统计含义。','','示意响应（任意单位）')
    p.plot([0,1],[1,.18],color=BLUE,marker='o',ms=8,lw=2,ls='--');p.plot([2.5,3.5],[.04,.88],color=COPPER,marker='s',ms=8,lw=2,ls='--');p.set(xlim=(-.4,3.9),ylim=(0,1.35),xticks=[0,1,2.5,3.5],xticklabels=['原模型\n对照','原模型\n功能损失','异源系统\n空白','异源系统\n候选表达'],yticks=[0,.5,1]);p.tick_params(axis='x',labelsize=12);p.text(.5,1.22,'损失证据',ha='center',color=BLUE,fontsize=15);p.text(3,1.22,'增益证据',ha='center',color=COPPER,fontsize=15);finish_plot(fig,p,29)
    fig,ax,p=plot_frame(33,'线索与体内后果，可以在时间上分开','人为构造的概念曲线；快速响应不等于身体缺口已被纠正。','事件顺序（非实测时间单位）','相对状态（示意）')
    x=np.linspace(0,10,500);p.plot(x,1-.66/(1+np.exp(-(x-2)*6)),color=BLUE,lw=2.5,label='可直接快速改变的活动');p.plot(x,1-.66/(1+np.exp(-(x-7.3)*2)),color=COPPER,lw=2.5,ls='--',label='体内缺口的较慢纠正')
    for xx,l in [(2,'感官线索'),(5,'摄入之后')]:p.axvline(xx,color=LINE,lw=1);p.text(xx+.12,.45,l,rotation=90,fontsize=12,color=MUTED)
    p.set(xlim=(0,10),ylim=(.1,1.16),xticks=[],yticks=[]);legend(p);finish_plot(fig,p,33)
    fig,ax,p=plot_frame(37,'学习可以改变信号与事件的关系','一类经典学习相关响应的教学示意，不能推广为全部多巴胺系统模式。','事件顺序（示意）','相对活动（任意单位）')
    x=np.linspace(0,10,600);p.plot(x,np.exp(-((x-6.8)/.35)**2),color=BLUE,lw=2.6,label='尚未形成稳定预期');p.plot(x,.95*np.exp(-((x-2)/.4)**2)+.06*np.exp(-((x-6.8)/.4)**2),color=COPPER,ls='--',lw=2.6,label='线索已能建立预期');p.set(xlim=(0,10),ylim=(-.04,1.1),xticks=[2,6.8],xticklabels=['线索','结果'],yticks=[])
    for v in [2,6.8]:p.axvline(v,color=LINE,lw=.8)
    legend(p);finish_plot(fig,p,37)
    fig,ax=frame(39,'持续条件下，节律可以不同','各行依次代表不同日子；程序构造的活动示意，没有稳定周期不等于没有活动。','教学活动图 · 非原始数据')
    rng=np.random.default_rng(39)
    for j,(period,l) in enumerate([(24,'近 24 小时'),(19,'近 19 小时'),(28,'近 28 小时'),(None,'无稳定节律')]):
        p=fig.add_axes([.17,.60-j*.11,.59,.085]);p.set(xlim=(0,24),ylim=(-.5,5.5));p.axis('off')
        for day in range(6):
            if period:
                start=(4+day*(period-24))%24;times=np.arange(start,start+3.3,.2)%24
            else:times=np.sort(rng.uniform(0,24,15))
            p.vlines(times,5-day-.32,5-day+.32,color=COL[j%3],lw=1.7)
        txt(ax,81,64-j*11,l,16,ha='left')
    txt(ax,17,17,'0',13);txt(ax,46.5,17,'12',13);txt(ax,76,17,'24 小时',13);line(ax,(17,20),(76,20),LINE);save(fig,39)
    fig,ax,p=plot_frame(41,'同一时刻的差异，也可能来自时相','两条假想曲线的振幅与 24 小时均值相同；非真实临床队列。','时间（小时，示意）','相对量（任意单位）')
    x=np.linspace(0,24,600);p.plot(x,.55+.45*np.sin(2*np.pi*x/24),color=BLUE,lw=2.6,label='相位 A');p.plot(x,.55+.45*np.sin(2*np.pi*(x-5)/24),color=COPPER,ls='--',lw=2.6,label='相位 B');p.axvline(8,color=LINE,lw=1.3);p.text(8.3,.13,'同一时刻采样',rotation=90,fontsize=12,color=MUTED);p.set(xlim=(0,24),ylim=(0,1.1),xticks=[0,6,12,18,24],yticks=[0,.5,1]);legend(p);finish_plot(fig,p,41)
    fig,ax=frame(43,'同一段时间，分别记录三类事件','事件顺序为教学安排；额外线索不能仅在事后从记录中删除。','事件与时间')
    for y,l in [(63,'计划信号'),(45,'食物结果'),(27,'额外线索')]:txt(ax,15,y,l,18);arrow(ax,(28,y),(94,y),color=MUTED)
    for start,c in [(38,BLUE),(65,COPPER)]:ax.plot([start,start,start+5,start+5],[63,70,70,63],color=c,lw=2.4)
    for x,c in [(46,BLUE),(73,COPPER)]:line(ax,(x,45),(x,52),c,2.4);ax.scatter([x],[52],color=c,s=60)
    line(ax,(59,27),(59,34),PLUM,2);ax.scatter([59],[34],color=PLUM,s=60,marker='s');txt(ax,59,19,'未计划的脚步 / 托盘声',15,color=MUTED);save(fig,43)
    fig,ax,p=plot_frame(44,'反应减弱以后，仍要继续观察','人工曲线示意习得、消退与间隔后测试；不代表所有学习的统一过程。','示意试次（13–14 处为时间间隔）','反应强度（任意单位）')
    p.plot(range(1,7),[.16,.35,.53,.73,.85,.94],'-o',color=BLUE,lw=2.4,ms=6,label='习得');p.plot(range(7,13),[.78,.59,.40,.27,.16,.10],'--s',color=COPPER,lw=2.4,ms=6,label='消退');p.plot(range(15,19),[.43,.28,.17,.12],':^',color=TEAL,lw=2.4,ms=7,label='间隔后测试');p.axvspan(12.5,14.5,color=SAND,alpha=.65);p.set(xlim=(.5,18.5),ylim=(0,1.12),xticks=[1,6,7,12,15,18],yticks=[0,.5,1]);legend(p,3);finish_plot(fig,p,44)
    fig,ax,p=plot_frame(45,'配对次数相同，背景未必相同','保留原图教学概率 0.8 / 0 与 0.8 / 0.8；不是历史实验参数。','','结果出现的概率（假想）')
    x=np.arange(2);p.bar(x-.17,[.8,.8],width=.32,color=BLUE,label='有信号时');p.bar(x+.17,[0,.8],width=.32,color='#e5c8a4',edgecolor=COPPER,hatch='///',label='无信号时')
    for xx,v in zip([-.17,.17,.83,1.17],[.8,0,.8,.8]):p.text(xx,v+.05,str(v),ha='center',fontsize=17,color=COPPER)
    p.set(xlim=(-.55,1.55),ylim=(0,1.08),xticks=[0,1],xticklabels=['安排甲','安排乙'],yticks=[0,.4,.8,1]);legend(p);finish_plot(fig,p,45)
    fig,ax,p=plot_frame(48,'学会做与记得做过，分别测量','人工曲线，不是 H.M. 原始成绩；不同任务也不能直接共用同一量表。','连续练习试次','任意单位')
    p.plot(range(1,10),[.90,.75,.59,.55,.42,.36,.33,.28,.23],'-o',color=BLUE,lw=2.6,ms=6)
    for v in [3.5,6.5]:p.axvline(v,color='#c4d1d4',ls=':',lw=1.3)
    p.set(xlim=(.5,9.5),ylim=(0,1.15),xticks=[2,5,8],xticklabels=['第 1 天','第 2 天','第 3 天'],yticks=[0,.5,1]);p.text(5,1.03,'练习表现可跨天改善',ha='center',fontsize=17,color=COPPER);p.text(5,.08,'是否记得练习经历：另用提问 / 测验记录',ha='center',fontsize=13,color=MUTED);finish_plot(fig,p,48)
    fig,ax,p=plot_frame(52,'相近输入，可以伴随不同响应','上下错开便于比较；时间与振幅无实验标定，不能据此判断改变必在突触前。','时间（无真实标定）','')
    x=np.linspace(0,10,600);pulse=np.exp(-((x-2)/.13)**2);epsp=np.maximum(x-2,0)*np.exp(-np.maximum(x-2,0)*1.4);epsp/=epsp.max()
    p.plot(x,2.5+.55*pulse,color=BLUE,lw=2.3,label='输入脉冲');p.plot(x,1.2+.8*epsp,color=COPPER,lw=2.3,label='较大突触后响应');p.plot(x,.2+.32*epsp,color=TEAL,lw=2.3,ls='--',label='较小突触后响应');p.set(xlim=(0,10),ylim=(0,3.2),xticks=[],yticks=[]);legend(p,3);finish_plot(fig,p,52)
    fig,ax,p=plot_frame(55,'脉冲总数多，不一定放电率高','保留原图人工例子：40 / 20 = 2，20 / 5 = 4；实际记录还需检查其他条件。','','单位时间放电次数（示意）')
    p.bar([0,1],[2,4],width=.5,color=[BLUE,COPPER]);p.set(xlim=(-.6,1.6),ylim=(0,5.2),xticks=[0,1],xticklabels=['位置甲\n40 次 / 20 时间单位','位置乙\n20 次 / 5 时间单位'],yticks=[0,1,2,3,4,5]);p.tick_params(axis='x',labelsize=13)
    for x,y in [(0,2),(1,4)]:p.text(x,y+.15,str(y),ha='center',color=COPPER,fontsize=22)
    finish_plot(fig,p,55)
    fig,ax,p=plot_frame(69,'不同时间尺度，不能直接重合','两条人工曲线仅说明时间差异；不是某脑区的真实响应函数或临床阈值。','时间（任意单位）','归一化响应（人工示意）')
    x=np.linspace(0,20,800);neural=((x>2)&(x<3)).astype(float);t=np.maximum(x-3,0);bold=t**3*np.exp(-t/1.6);bold/=bold.max()
    p.plot(x,neural,'--',color=BLUE,lw=2.3,label='假想短时输入');p.plot(x,bold,color=COPPER,lw=2.5,label='延迟的血流相关响应');p.set(xlim=(0,20),ylim=(0,1.15),xticks=[],yticks=[0,.5,1]);legend(p);finish_plot(fig,p,69)
    fig,ax,p=plot_frame(75,'离散跃迁，仍需与噪声和漏电区分','轨迹与噪声由程序构造；非 1976 年原始记录，不规定所有通道的状态数。','时间（任意单位）','电流变化（人工示意）')
    x=np.linspace(0,10,1200);y=np.zeros_like(x)
    for lo,hi in [(1,1.9),(3,3.4),(5,6.5),(7.6,8.6)]:y[(x>lo)&(x<hi)]=1
    y+=np.random.default_rng(75).normal(0,.035,len(x));p.plot(x,y,color=BLUE,lw=1.2);p.axhline(0,color=COPPER,lw=.6,alpha=.4);p.axhline(1,color=COPPER,lw=.6,alpha=.4);p.set(xlim=(0,10),ylim=(-.2,1.3),xticks=[],yticks=[0,1],yticklabels=['水平一','水平二']);finish_plot(fig,p,75)
    fig,ax,p=plot_frame(81,'估计精度，也取决于设计与数据','误差范围为简化公式构造；非真实效应区间，不能用于计算研究所需人数。','样本量变化（无具体人数标定）','假想效应估计与不确定性')
    x=np.arange(6);err=np.array([1,.707,.5,.354,.25,.177]);p.errorbar(x,np.zeros(6),yerr=err,fmt='o-',color=BLUE,ecolor='#89a4b3',elinewidth=2,capsize=7,ms=7,lw=1.8);p.axhline(0,color=COPPER,ls='--',lw=1);p.set(xlim=(-.35,5.35),ylim=(-1.15,1.15),xticks=[0,5],xticklabels=['较少','较多'],yticks=[]);finish_plot(fig,p,81)
