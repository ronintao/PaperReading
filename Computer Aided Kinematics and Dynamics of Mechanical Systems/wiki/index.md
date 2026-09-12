---
type: index
title: "Computer Aided Kinematics and Dynamics of Mechanical Systems, Volume I: Basic Methods"
wiki_language: zh-CN
last_updated: 2026-09-12
---

# 论文解读导航

## 主论文
- [computer-aided-kinematics-and-dynamics](computer-aided-kinematics-and-dynamics.md) (E. J. Haug, 1989, Allyn and Bacon)

## 术语对照
- [术语中英对照表 (Glossary)](glossary.md) — 统一全套笔记译名（joint=关节、configuration=构型 等）；新笔记须遵循

## Related 论文解读
（暂无）

## Topic 专题

### 章节精读笔记（小节级）
- [3.1 Basic Concepts in Planar Kinematics](3.1-basic-concepts-in-planar-kinematics.md) — 全书方法论奠基：笛卡尔广义坐标 q=[x,y,φ]、完整约束 Φ(q,t)=0、自由度 DOF=nc−nh、驱动约束、位置/速度/加速度三段式统一求解(共用雅可比 Φ_q)、单摆/曲柄滑块全套推导、斜滑块奇异构型反例(约束必须蕴含铰几何)
- [3.2 Constraints Between a Body and Ground (Absolute Constraints)](3.2-absolute-constraints.md) — 体-地约束库：绝对距离 Φ^ad(Eq 3.2.1)+绝对位置 Φ^ax/Φ^ay(Eqs 3.2.3-4)+绝对角度 Φ^aφ(Eq 3.2.6)四种约束，逐条推导雅可比(链式+B_i=dA/dφ)、ν=0、γ 逐项时间二阶求导+物理向心加速度诠释、C₃>0 单方程记账条件、单摆用两条位置约束的等价表述、滑块 y=0+φ=0 得到沿 x 轴 1 DOF 的叠加建模
- [3.5 Driving Constraints](3.5-driving-constraints.md) — 驱动约束库：绝对/相对坐标驱动+相对距离驱动+转动关节转角驱动+平移-距离驱动的方程与雅可比、Φ^d = Φ(q) − C(t) 分离形式共用同一 Φ_q、双体曲柄滑块+四杆机构+挖掘机双液压缸+挖掘机混合驱动+起重机吊臂五个完整例题(速度方程逐步求解、发现书中 φ̇₃ 系数与 B_i 转置的排版遗漏)、速度/加速度右端 ν^d=Ċ、γ^d=γ+C̈及 Table 3.5.1 汇总
- [3.6 Position, Velocity, and Acceleration Analysis](3.6-position-velocity-acceleration-analysis.md) — 三段统一框架：约束装配 Φ(q,t)=0(方阵)、隐函数定理(解存在唯一性)、Newton-Raphson(二阶收敛)+装配最小化判可装配、速度方程 Φ_q q̇=−Φ_t、加速度方程 Φ_q q̈=γ(逐项链式推导)、冗余约束(相容/不相容)、双摆完整数值算例(发现书中 γ₄ 符号笔误)、时间网格+二阶泰勒预测
- [3.7 Singular Configurations](3.7-singular-configurations.md) — 奇异构型专节：锁死/分岔两种病态、两体曲柄滑块闭式解 q=cosωt∓√(cos²ωt+ℓ²−1)(判别式定锁死/分岔)、锁死判据 Φ_q=0且Φ_t≠0⇒q̇→∞、雅可比行列式 |Φ_q|=−ℓsinφ₂、速度方程+择一定理+虚位移(行列式变号判分岔)、设计变更 Φ_q δq=−Φ_b δb(多解/无解)、五杆平行四边形冗余约束(秩亏代数证明)
- [4.4 Linear Equation Solution and Matrix Factorization](4.4-linear-equation-solution-matrix-factorization.md) — 线性求解工具：高斯消元(前向消元+回代)、行选主元/全选主元(主元为零或过小⇒舍入误差)、非方阵前向消元判定矩阵秩与变量划分(非独立 u/独立 v，§4.6基础)、L–U 分解 A=LU(Crout 方法原地递归)
- [4.5 Newton–Raphson Method for Nonlinear Equations](4.5-newton-raphson-method-nonlinear-equations.md) — 非线性方程 Φ(q)=0 求解：一阶泰勒线性化+迭代、单变量公式 q⁽ⁱ⁺¹⁾=q⁽ⁱ⁾−Φ/Φ_q(4.5.5)、二阶收敛(4.5.6)、四图示警(拐点振荡/多解依赖初值/极值点发散)、n 元解线性方程 Φ_q Δq=−Φ(4.5.8)再 q⁽ⁱ⁺¹⁾=q⁽ⁱ⁾+Δq(把§4.4线性求解器接入位置分析)
- [6.1 Equations of Motion of a Planar Rigid Body](6.1-equations-of-motion-planar-rigid-body.md) — 单刚体动力学起点：微元牛顿方程→虚功消内力(刚体内力虚功为零)→达朗贝尔原理(6.1.4)、广义坐标展开变分方程(6.1.11)、质心坐标化简(B^T B=I)→牛顿-欧拉方程 mr̈=F, J'φ̈=n(6.1.19)、质心式(6.1.20)/平行轴定理 J''=J'+m|ρ''|²(6.1.22)/对称轴含质心、组合体叠加(6.1.23-25)，例6.1.1拖拉机+例6.1.2组合摆(J'=1.966)
- [7.1 Organization of Computations](7.1-organization-of-computations.md) — 第7章开篇+7.1节：动力学分析三模式(平衡/逆动力学/动力学)、DAE"1981年才被认识不能当ODE处理"、DADS三段式(前处理器/动力学分析程序/后处理器,Fig.7.1.1)、分析程序三层(ANALYSIS/JUNCTION/MODULES,Fig.7.1.2)、五阶段详细计算流(Fig.7.1.3)、平衡=动态沉降/总势能最小化、动力学=解加速度→积分位置速度、逆动力学=解运动学+装配运动方程求乘子(无公式,纯计算组织)
- [7.3 Algorithms for Solving Differential–Algebraic Equations](7.3-algorithms-for-solving-dae.md) — DAE四算法：二阶DAE降为一阶IVP(丢失位置/速度约束→漂移)、广义坐标分块法(积分独立坐标v+Newton-Raphson强制校正依赖坐标u,可靠但慢)、直接积分法(无视漂移,最快)、Baumgarte约束稳定化(加速度约束加PI反馈 Φ̈+2αΦ̇+β²Φ=0→γ̂,Eq.7.3.8)、混合算法(常态稳定化/超差回拉/奇异退化,DADS采用)、初值问题存在性定理(仅局部解)
- [7.4 Numerical Integration of First-Order Initial-Value Problems](7.4-numerical-integration-first-order-ivp.md) — 一阶IVP数值积分：多项式插值地基(Taylor单点/多阶导 vs Newton后向差分多点/函数值,插值误差7.4.8)、Adams-Bashforth显式预测器(Eq.7.4.11,系数γ_i与h无关证明,k=1即Euler,自启动升阶,截断误差~h^{k+1})、Adams-Moulton隐式校正器(Eq.7.4.15,纳入f_{n+1}^p精度高一阶~h^{k+2})、PECE(k阶预测+k+1阶校正最佳配对,截断误差自适应调h/k,倒车类比Fig.7.4.2)、逐例手算e^t(例7.4.1-7.4.5)
- [9.1 Vectors in Space](9.1-vectors-in-space.md) — 空间向量代数地基：几何向量(模/单位/加法平行四边形)、笛卡尔分量+方向余弦、标量积 a·b=aᵀb(9.1.11)判正交/算投影、空间独有的向量积 c=ãb(9.1.16/9.1.22)、波浪号算子 ã(9.1.21)把叉积变矩阵乘、双tilde恒等式 ãb̃=baᵀ−(aᵀb)I(9.1.28)及(9.1.29-32)全套性质逐条推导、静止系向量微分(9.1.33)、定长向量速度⊥位置(9.1.39)、匀速圆周运动向心加速度 r̈=−ω²r(例9.1.7-9.1.9)、三点定义参考系(例9.1.6)
- [9.5 Driving Constraints](9.5-driving-constraints.md) — 空间驱动约束库：把 §9.4 定常约束里的常量换成 C(t) 得到 4 类驱动——绝对驱动 Φ^kd=x_i^P−C_k(t)(Eq 9.5.1，3 条)、距离驱动 Φ^ssd=d_ijᵀd_ij−C(t)²(Eq 9.5.2)、相对平移驱动 Φ^td=h_iᵀd_ij−C(t)(Eq 9.5.3，附于移动副/柱铰/螺旋副/支柱)、相对转动驱动 Φ^rotd=θ+2nπ−C(t)(Eq 9.5.4，附于转动副/柱铰/螺旋副)；时间冻结变分⇒雅可比与定常约束**完全相同**、只在 ν=Ċ、γ=C̈ 右端加显式时间项，与 §9.6 求解框架零成本对接
- [9.6 Position, Velocity, and Acceleration Analysis](9.6-position-velocity-acceleration-analysis.md) — 空间三段统一框架：单体广义坐标 q_i=[r_i;p_i]∈ℝ⁷、Euler 参数归一化 pᵀp−1=0 补齐 7 参数-6 DOF 差(Eq 9.6.3)、合成方程 Φ=[Φ^K;Φ^D;Φ^p]=0 共 7nb 方程(Eq 9.6.5)、位置雅可比 Φ_p=2Φ_π'G 装配(Eq 9.6.6-8)+关键恒等式 Φ_i,π'^p=pᵀGᵀ=0(Eq 9.6.9)⇒归一化速度/加速度方程恒零可剔除；速度方程系数矩阵≠位置雅可比(差 2G 因子,须分别验非奇异)、ν^K=0、ν^D 逐类 Ċ；加速度方程系数矩阵**复用**速度方程(LU 分解只做一次)、右端 γ 用 Ȧ=Aω̃' 三步法(全 d1 完整推导+d2/球副/球-球/绝对/点约束/螺旋 γ 结果)、驱动加 C̈ 项(Eqs 9.6.29-32)
- [10.1 Modeling and Analysis Techniques](10.1-modeling-and-analysis-techniques.md) — 空间建模方法论开篇：唯一本质差别=约束冗余；例 10.1.1 空间曲柄滑块 nc=28/nh=30→DOF=−2、n_red=30−(28−1)=3、rank Φ_q=27；三条冗余溯源(平行轴自动传递 2 条 + 共面使 C 点 z 约束恒满足 1 条)、制造缺陷测试(装偏 A 轴→C 轴失配不能装配⇒调 2 参数，加离面 offset⇒第 3 个冗余度)、反面教材(移动副→绝对 x/z 约束使计数变对但仍不可装配；转动副→圆柱副可装配却放出体 3 绕轴自转的额外 DOF)、结论"只改方程数量不行，必须改关节类型"
- [10.2 Kinematic Analysis of a Spatial Slider-Crank Mechanism](10.2-kinematic-analysis-spatial-slider-crank.md) — §10.1 结论的示范：关节参考三点组(P 定关节中心/PQ 定 z'' 轴/PR 定 x'' 轴，R 可任选)定义关节几何；模型 nc=28、nh=5(转动副 A)+3(球副 B)+3(转-柱 C)+5(移动副 D)+1(距离)+6(地面)+4(归一化)=27⇒DOF=1，与 §10.1 病态模型对照(30→27、−2→+1，恰减 3 条冗余)；装配表 10.2.6/10.2.7 逐条数值验算(归一化=1、球副两体残差 4e−4、连杆质心=B/C 中点、|BC|=0.29999=ℓ、d_32∥h_3 夹角 0.13°、距离=1.0000)；驱动 Φ^rotd=θ+2nπ−2πt=0(ω_0=2π⇒1 转/秒)；**补齐原书跳过的几何**：滑轨=过原点 x 轴、曲柄轴∥x 过 A(0,0.1,0.12)、r=0.08 ⇒ ρ²=0.0308+0.016cosθ+0.0192sinθ、x_slider=√(ℓ²−ρ²)，锁死阈值 ℓ_min=ρ_max=√(0.1²+0.12²)+0.08=0.2362 m(与书中逐位吻合)；近奇异放大 ẋ∝(ℓ²−ρ²)^(−1/2)、ẍ∝(ℓ²−ρ²)^(−3/2)，三档 ℓ=0.3/0.27/0.24 m 的峰谷值与峰值速度比 1:1.23:1.69 对图 1:1.21:1.76 印证，ℓ=0.24(距阈值 1.6%)加速度峰值≈11 m/s²(基准≈2.8)
- [10.3 Kinematic Analysis of a Spatial Four-Bar Mechanism](10.3-kinematic-analysis-spatial-four-bar.md) — "等效建模"验证：同一空间四杆(A 转动副 5/D 转动副 5/B 万向节 4/C 球副 3)两套模型——模型 1(4 体 nc=28、nh=5+5+4+3+6+4=27)、模型 2(连杆不做体改球-球复合关节 1 方程，3 体 nc=21、nh=5+5+1+6+3=20)，DOF 均=1；配套推导：消去连杆⇒未知量 −7(6 GC+1 归一化)、方程 −8(万向节 4+球副 3+归一化 1)再补 1 条距离约束⇒方程净 −7、ΔDOF=0(严格等价)；关节数据读法(A 两体 PQ=x̂⇒绕全局 x 转、D h_3=A_3x̂=−ŷ、B 曲柄叉轴(0.750,−0.662,0)⊥曲柄轴+连杆叉轴=局部 z⊥杆轴、C 连杆(0,−6.1,0)与摇杆(0,−3.7,0))；装配表 10.3.5/10.3.6 独立复算：4 个共点残差 3.2e−4/8.7e−5/1.4e−4/1.5e−4 m、转动副轴线平行度 8e−9/1.3e−9、杆长 AB=2.0000/BC=12.2042(≈12.19)/CD=7.3948/AD=9.3941，构型 A(0,0,0)/B(0,0,2)/C(−7.506,−8.500,6.511)/D(−4,−8.5,0)；驱动 θ=πt(ω_0=π⇒周期 2 s)⇒解析解 z_B=2cos(πt)；图 10.3.3–10.3.5：摇杆 z 每转两次起伏 z∈[2.63,3.72] m、ż∈[−2.8,4.0] m/s 且两图互补，t=0 起点 2.0 与 3.22 分别等于 z_B(0)、z_3(0)=3.2553，模型 2 结果完全一致；**发现印刷数据唯一不自洽处**：万向节 h_1·h_2=−0.6808≠0(两叉轴 133°)，若以关节数据为准则连杆②姿态应为 A_2=[h_1,−g_1,f_1](p_2≈(0.9187,−0.1759,0.0664,−0.3474))，若以表 10.3.6 为准则 Q_2=P_2+(−0.681,0,−0.733)，不影响其余结论

- [10.4 Kinematic Analysis of an Air Compressor](10.4-kinematic-analysis-air-compressor.md) — 第 10 章收官：斜盘式六缸压缩机（9 体：机架①/转子②/斜盘③/活塞④–⑨）；模型 nc=9×7=63、nh=2×5(A,B 转动副)+6×5(C–H 平移副)+6×1(球-球距离)+1(盘上 O 点 x 位置绝对约束)+6(地面)+9(归一化)=62⇒DOF=1；读表技巧(Q=P+(0,1,0)、R=P+(1,0,0)⇒0.3660=cos30°−0.5 编码偏置角 α=30°、−0.1732+1 类的 0.8268/1.1732、六个球心与缸孔沿 R₀=0.2 m 圆周每 60° 均布 ψ_k=30/90/150/210/270/330°、缸孔平面 y=−1.0)；**x 位置约束不可省**的 DOF 论证(去掉则 DOF=2，多出盘绕法线的自转 β，驱动锁不住)；装配表 10.4.5 独立复算：**发现盘 e₀ 印刷值 1.96597 应为 0.96597**(|p|²=3.93189→0.99989、χ=29.98°=偏置角)、B 共点残差 1.1e−3 m、两轴夹角 0.0222°、六杆长误差≤1e−3 m(0.2%L)、活塞(x,z) 与缸孔吻合到 1e−5——全表精度 ~1e−3；驱动 600 rpm⇒ω=2π×10=62.832 rad/s⇒θ=62.832t(Eq 9.5.4，T=0.1 s)；**补齐原书跳过的解析解**：A₃=A_y(θ)A_x(−α)A_y(β)、盘心固定于(0,−0.5,0)、盘法线绕 ŷ 画 30° 圆锥、槽约束解出 β(θ)=270°−g(θ)、g=arctan(−cotθ/cosα) 且 x_O≡0(θ=180° 处两支须按连续性跟踪)、活塞位移 y_k=−1+R₀sinα·sin(ψ_k−270°+g)−ε(|ε|≤0.003 m) ⇒ **行程精确 =2R₀sinα**(0.13681/0.20000/0.25712 m)、速度/加速度的正弦基准 ωR₀sinα、ω²R₀sinα 被畸变因子 g′=cosα/(1−sin²αsin²θ)∈[cosα,1/cosα] 放大(峰值 v=4.57/7.26/10.54 m/s 即正弦的 1.06/1.16/1.30 倍，峰值 a=241/372/630 m/s²)⇒ 原书"40° 最极端"的定量解释；六缸 60° 相位使一阶惯性力自平衡

- [11.1 Equations of Motion of a Rigid Body](11.1-equations-of-motion-of-a-rigid-body.md) — 空间动力学起点（与 §6.1 平面版逐项对应）：微元牛顿方程(11.1.1)→虚位移加权消内力(**对称化 11.1.3 三步**：半个自己+换哑变量、交换积分次序、代入牛顿第三定律；距离约束变分 11.1.4；内力共线 11.1.5 ⇒ **内力虚功恒零** 11.1.6，并记下原书警告"共线不是第三定律的推论"——电磁场/非均匀引力场中内力须当外力)→d'Alembert 虚功方程 11.1.7；代入 δr^P=δr−As̃'^P δπ'(11.1.8，用 δπ̃=Aδπ̃'Aᵀ 与 ãb=−b̃a) 与 r̈^P=r̈+Ȧs'^P=r̈+Aω̇̃'s'^P+Aω̃'ω̃'s'^P(11.1.9，由 Ȧ=Aω̃' 再求导) ⇒ 展开成**七项 11.1.11**(附七项去向表：m / 质心交叉项×2 / J' / 陀螺项 / F / n')；质心随体系 ∫s'dm=0 使两交叉项消失，**第四积分用 ω̇̃'s'=−s̃'ω̇' 一步化为 J'ω̇'**(11.1.16，并补出 J' 矩阵式的来源 s̃s̃=s sᵀ−(sᵀs)I ⇒ −s̃s̃=…，对角元 (y')²+(z')²)、**第五积分用 ãb̃=b̃ã+baᵀ−abᵀ(9.1.31) 化为 ω̃'J'ω'**(11.1.18，两个附加项因 s'ᵀ(s'×ω')=0 恒零) ⇒ 变分 Newton–Euler 11.1.19 + Newton–Euler 11.1.20(并说明 ω' 是准坐标、不可直接积分 ⇒ 必须上 Euler 参数，Prob 11.1.3)；**例 11.1.1** 球面约束 Φ=(r+Ah')ᵀ(r+Ah')−1=0 的四行变分 + 乘子 λ ⇒ 约束力沿球面法线 2λ(r+Ah')，转动式 J'ω̇'+2h̃'Aᵀr λ=n'−ω̃'J'ω'；**一点固定**：r=c、ṙ=r̈=0、δr=0(11.1.21) ⇒ ②③⑥项因含 δr、r̈ 而消失(与 ∫s''dm≠0 无关，含 ∫s''dm 的两项都被 δr/ r̈ 杀掉) ⇒ δπ''ᵀ[J''ω̇''+ω̃''J''ω''−n'']=0(11.1.22) ⇒ **欧拉方程** 11.1.23；**例 11.1.2** 绕 y 轴摆：ω''=[0,φ̇,0](11.1.24)、J''ω̇''=φ̈·J''第2列、ω̃''J''ω''=ω''×(J''ω'')=[J_{z''y''}φ̇²,0,−J_{x''y''}φ̇²]ᵀ(11.1.25)、F''=AᵀF=mg[sinφ,0,−cosφ]、n''=ρ̃''F''=mg[−ρ_{y''}cosφ, ρ_{z''}sinφ+ρ_{x''}cosφ, −ρ_{y''}sinφ] ⇒ **J_{y''y''}φ̈=n_{y''}**(11.1.26，"只有 y'' 惯性矩进运动方程"的原因=δπ'' 只有 φ 分量)；反力矩 T''=[T_{x''},0,T_{z''}](11.1.27)、T_{x''}=J_{z''y''}φ̇²+J_{x''y''}φ̈−n_{x''}、T_{z''}=−J_{x''y''}φ̇²+J_{z''y''}φ̈−n_{z''}(11.1.28) ⇒ **惯性积的可见后果=关节动态反力矩**；与 §6.1 逐项对照表(虚功 6.1.4↔11.1.7、变分方程 6.1.11↔11.1.19、Newton–Euler 6.1.19↔11.1.20 多陀螺项、标量 J'↔矩阵 J'、平行轴 6.1.22↔§11.2、ω' 可积分↔准坐标)+ 习题 11.1.1–11.1.3 对应

### 逐章精读笔记
- [Ch.1 Elements of Computer-Aided Kinematics and Dynamics](ch1-elements-of-cakd.md) — 导论：学科范围、工程实例、传统方法vs计算方法、两种坐标方法对比、全书导读
- [Ch.2 Planar Vectors, Matrices, and Differential Calculus](ch2-planar-vectors-matrices-calculus.md) — 数学基础：几何→代数向量、矩阵代数、坐标变换矩阵A/B/R、矩阵微积分记号Φ_q、运动体上点的速度/加速度公式
- [Ch.3 Planar Cartesian Kinematics](ch3-planar-cartesian-kinematics.md) — 核心方法论：平面运动副约束方程库、齿轮/凸轮高副、驱动约束、位置(N-R)/速度/加速度统一求解、奇异构型(lock-up/bifurcation)
- [Ch.4 Numerical Methods in Kinematics](ch4-numerical-methods-kinematics.md) — 数值实现：DADS三层架构、Jacobian稀疏评估、装配最小化(共轭梯度)、高斯消元/LU分解、Newton-Raphson(收敛性分析)、冗余约束自动检测与消除
- [Ch.5 Planar Kinematic Modeling and Analysis](ch5-planar-kinematic-modeling.md) — 五大应用案例：曲柄滑块/四连杆/快回/齿轮-滑块/气门挺杆，建模配方(Recipe)、复合铰简化、装配陷阱、锁死/分叉奇异性、加速度对参数的极端敏感性
- [Ch.6 Dynamics of Planar Systems](ch6-planar-dynamics.md) — 从运动学到动力学的跨越：虚功原理消除内力、广义力(弹簧-阻尼器-作动器)、拉格朗日乘子→DAE(Eq.6.3.18)、逆动力学(运动学确定系统)、最小总势能平衡、约束反力公式(Eqs.6.6.8-6.6.9)
- [Ch.7 Numerical Methods in Dynamics](ch7-numerical-methods-dynamics.md) — DAE数值求解：DADS动力学程序架构、坐标分区DAE→ODE约化与存在性证明、四种DAE算法(坐标分区/直接积分/Baumgarte稳定化/混合算法)、Adams-Bashforth预测器+Adams-Moulton校正器PECE积分、自适应步长阶次控制、最小势能平衡分析
- [Ch.8 Planar Dynamic Modeling and Analysis](ch8-planar-dynamic-modeling.md) — Part One收官：曲柄滑块(压缩机)飞轮惯量参数研究与失速能量分析、快回机构(牛头刨床)飞轮-循环频率反直觉关系、螺旋弹簧涌浪波与碰撞振颤(单侧弹簧/阻尼器)、气门挺杆弹簧设计准则(负反力=分离失效)
- [Ch.9 Spatial Cartesian Kinematics](ch9-spatial-cartesian-kinematics.md) — Part Two 起点：空间向量+tilde 算子、方向余弦矩阵 A、角速度 ω/ω'、Euler 参数（无奇异姿态广义坐标）、6 类基本运动副+7 类复合关节+4 类驱动约束、位置/速度/加速度三段统一求解（系数矩阵复用）
- [Ch.10 Spatial Kinematic Modeling and Analysis](ch10-spatial-kinematic-modeling.md) — 空间建模核心：约束冗余识别（制造缺陷测试）、空间曲柄滑块（球铰+转动圆柱副消冗余、锁死临界）、空间四连杆（两种等效模型验证）、空气压缩机（9体/62约束/偏置角参数研究）
- [Ch.11 Dynamics of Spatial Systems](ch11-spatial-dynamics.md) — 空间动力学核心：变分Newton-Euler方程（陀螺项ω̃'J'ω'）、惯性属性（主轴/平行轴定理/复合体）、两种约束DAE形式（Newton-Euler一阶混合Eq.11.3.11 vs Euler参数二阶Eq.11.3.29）、TSDA/RSDA力元广义力、关节反力公式（Eq.11.5.6）、DADS混合积分算法
- [Ch.12 Spatial Dynamic Modeling and Analysis](ch12-spatial-dynamic-modeling.md) — 全书终章：空间曲柄滑块（近奇异力矩突变/保守系统周期性）、空间四连杆（多平衡解/等效模型比较）、空气压缩机（9体气压力特性/启动能量阈值）、车辆动力学（8体麦弗逊悬架/轮胎侧偏模型/变道Roll稳定杆效果/55mph圆弧轮胎极限）、调速器（稳态分析/力矩反馈/k-C参数灵敏度/稳定性边界）


