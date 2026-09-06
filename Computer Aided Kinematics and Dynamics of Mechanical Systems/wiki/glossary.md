---
type: glossary
parent: computer-aided-kinematics-and-dynamics
title: "术语中英对照表 (Terminology Glossary)"
created: 2026-06-09
last_updated: 2026-09-06
---

# 术语中英对照表（Terminology Glossary）

> 本表用于统一 *Computer Aided Kinematics and Dynamics of Mechanical Systems* 全套阅读笔记的中文译名。
> **规则**：撰写笔记时，术语**首次出现**标注英文原文，如"构型（configuration）"；后续仅用中文。
> 新增术语请追加到对应分类并保持字母序。

## 一、基础概念 (Fundamentals)

| English | 中文（统一译名） | 备注 / 不采用的译法 |
|---------|----------------|--------------------|
| body | 物体 / 刚体 | 上下文明确时用"刚体" |
| body-fixed reference frame | 随体参考系 | 不用"体固定坐标系" |
| configuration | **构型** | **不用**"位形" |
| degrees of freedom (DOF) | 自由度 | $\text{DOF}=nc-nh$ |
| generalized coordinates | 广义坐标 | |
| independent / dependent (coordinates) | 独立 / 非独立（坐标） | **不用**"相依"；约束一般非线性，故也不用"线性相关/无关" |
| kinematics | 运动学 | |
| dynamics | 动力学 | |
| kinematic analysis | 运动学分析 | |
| kinematic synthesis | 运动学综合 | |
| mechanism | 机构 | |
| rigid body | 刚体 | |
| structure | 结构 | 只传载、抗动，区别于机构 |

## 二、关节与约束 (Joints & Constraints)

| English | 中文（统一译名） | 备注 / 不采用的译法 |
|---------|----------------|--------------------|
| joint | **关节** | **不用**"铰""运动副"；首次标注 (joint) |
| physical joint | 物理关节 | |
| geometry of the joint | 关节的几何 | |
| revolute joint | 转动关节 | 首次可标 (revolute joint) |
| translational joint | 移动关节 | |
| gear constraint | 齿轮约束 | |
| cam constraint | 凸轮约束 | |
| composite constraint | 复合约束 | |
| constraint equation | 约束方程 | |
| holonomic constraint | 完整约束 | |
| nonholonomic constraint | 非完整约束 | |
| stationary constraint | 定常约束 | 不显含时间 |
| time-dependent constraint | 时变约束 | 显含时间 |
| absolute constraint | 绝对约束 | 体与地面 |
| absolute distance constraint | 绝对距离约束 | $\Phi^{ad}$；点 $P_i$ 到定点 $\mathbf{C}$ 距离 $=C_3>0$；Eq. 3.2.1 |
| absolute position constraint | 绝对位置约束 | $\Phi^{ax},\Phi^{ay}$；点 $P_i$ 的 $x$ 或 $y$ 坐标固定；Eqs. 3.2.3–3.2.4 |
| absolute angular constraint | 绝对角度约束 | $\Phi^{a\phi}$；体 $i$ 转角固定；Eq. 3.2.6 |
| relative constraint | 相对约束 | 体与体 |
| driving constraint | 驱动约束 | |
| kinematically driven | 运动学驱动的 | |
| driver | 驱动器 | |
| absolute driver | 绝对驱动 | 时变绝对约束，输入 $C_k(t)$；Eqs. 3.5.1–3.5.3 |
| relative driver | 相对驱动 | 时变相对约束；Eqs. 3.5.5–3.5.8 |
| relative distance driver | 相对距离驱动 | $\Phi^{rdd}$，$C_4(t)>0$；液压伸缩杆 |
| revolute-rotational driver | 转动关节-转角驱动 | $\Phi^{rrd}$，控制转动关节两体的相对角；旋转执行器 |
| translational-distance driver | 平移-距离驱动 | $\Phi^{tdd}$，控制移动关节的相对平移；数控进给轴 |
| actuator | 执行器 | 液压、电动、伺服等施加驱动量的物理器件 |
| attachment angle | 安装角 | $\theta_i, \theta_j$，执行器在体上的物理安装方向 |
| redundant constraint | 冗余约束 | 雅可比秩亏时出现 |
| consistent redundancy | 相容冗余 | 多余但不矛盾，自动满足 |
| inconsistent redundancy | 不相容冗余 | 多余且矛盾，方程无解 |
| consistent / inconsistent (constraints) | 相容 / 不相容（约束） | 能否物理装配 |

## 三、数学与求解 (Math & Solution)

| English | 中文（统一译名） | 备注 / 不采用的译法 |
|---------|----------------|--------------------|
| Jacobian (matrix) | 雅可比（矩阵） | $\boldsymbol{\Phi}_\mathbf{q}$ |
| singular / nonsingular | 奇异 / 非奇异 | |
| singular configuration | 奇异构型 | |
| constraint degeneracy | 约束失效 | 奇异构型下约束不再限制其自由度；**不用**自造的"约束不蕴含几何" |
| rank-deficient | 秩亏 | 雅可比行向量线性相关 |
| determinant | 行列式 | |
| position equation | 位置方程 | |
| velocity equation | 速度方程 | $\boldsymbol{\Phi}_\mathbf{q}\dot{\mathbf{q}}=\boldsymbol{\nu}$ |
| acceleration equation | 加速度方程 | $\boldsymbol{\Phi}_\mathbf{q}\ddot{\mathbf{q}}=\boldsymbol{\gamma}$ |
| chain rule (of differentiation) | 链式法则 | |
| coefficient matrix | 系数矩阵 | |
| Newton–Raphson | 牛顿-拉夫森 | N-R |
| quadratically convergent | 二阶收敛 | 误差正比于前一次误差平方 |
| implicit function theorem | 隐函数定理 | 保证解存在唯一 |
| position / velocity / acceleration analysis | 位置 / 速度 / 加速度分析 | 三段统一框架 |
| singular configuration | 奇异构型 | 雅可比奇异之构型 |
| lock-up configuration | 锁死构型 | 越过该点约束无解、$\dot{\mathbf{q}}\to\infty$；**不用**"自锁" |
| bifurcation | 分岔 | 运动分叉为多条路径；行列式越过时变号 |
| isolated singular point | 孤立奇异点 | 锁死/分岔点，其两侧有唯一解 |
| theorem of the alternative | 择一定理 | 判定 $\boldsymbol{\Phi}_\mathbf{q}\dot{\mathbf{q}}=-\boldsymbol{\Phi}_t$ 是否有解 |
| virtual displacement | 虚位移 | 时间冻结、满足一阶约束的 $\delta\mathbf{q}$；第 6 章详述 |
| design parameter | 设计参数 | $\mathbf{b}=[b_1,\dots,b_k]^T$，如杆尺寸 |
| time grid | 时间网格 | 仿真在一串时间点上求解 |
| Taylor expansion | 泰勒展开 | 二阶展开作初值预测 |
| differential-algebraic equations (DAE) | 微分-代数方程 | |
| Lagrange multiplier | 拉格朗日乘子 | |
| reference frame | 参考系 | |
| transformation matrix | 变换矩阵 | $\mathbf{A}(\phi)$ |
| rotation / orientation | 转动 / 朝向 | |
| assembly (of a system) | 装配 | 在 $t_0$ 解约束方程求初始构型 |
| objective function | 目标函数 | $\psi$，最小化对象 |
| weighting constant / penalty | 权重常数 / 罚因子 | $r>0$，渐增逼迫约束被满足 |
| least squares | 最小二乘 | 多解时取离 $\mathbf{q}^0$ 最近者 |
| conjugate gradient minimization | 共轭梯度最小化 | 大规模系统装配用 |
| Fletcher–Powell algorithm | Fletcher–Powell 算法 | 拟牛顿，迭代更新 $\mathbf{H}$ |
| gradient | 梯度 | $\psi_\mathbf{q}$，仅需 $\boldsymbol{\Phi}$ 与 $\boldsymbol{\Phi}_\mathbf{q}$ |
| Gaussian elimination | 高斯消元 | 逐个消去变量；前向消元 + 回代 |
| forward elimination | 前向消元 | 化为对角元为 1 的上三角形 |
| back substitution | 回代 | 从末行逐步往上解出各变量 |
| pivot element | 主元 | 第 $j$ 步对角元 $a_{jj}^{(j-1)}$；为零则失败、过小则失稳 |
| row pivoting | 行选主元 | 仅换行，取列内对角及下方绝对值最大元 |
| full pivoting | 全选主元 | 行+列互换；换列则对应变量也互换 |
| round-off error | 舍入误差 | 主元过小时被放大 |
| nonsquare matrix | 非方阵 | $m$ 方程 $n$ 未知数（$m<n$） |
| rank (row rank) | 秩（行秩） | 前向消元后非零行数 $r$ |
| dependent / independent variables | 非独立 / 独立变量 | $\mathbf{u}$ 由 $\mathbf{v}$ 决定；变量被划分 |
| partition (of variables) | 变量划分 | $\mathbf{x}\to(\mathbf{u},\mathbf{v})$；§4.6 冗余约束基础 |
| ill-conditioned | 病态 | 右下零块近零但非舍入零、右端量级大 |
| L–U factorization | L–U 分解 | $\mathbf{A}=\mathbf{LU}$，$\mathbf{L}$ 单位下三角、$\mathbf{U}$ 上三角 |
| Crout's method | Crout 方法 | 原地递归算 $\mathbf{L},\mathbf{U}$（Eq. 4.4.20） |
| auxiliary matrix | 辅助矩阵 | $\mathbf{B}$，合并存放 $\mathbf{L}$ 与 $\mathbf{U}$ 元素 |
| Cramer's rule | Cramer 法则 | 最著名但最低效 |
| inflection point | 拐点 | 二阶导变号点；根在此处 N-R 振荡发散（Fig. 4.5.2） |
| equation / solution error tolerance | 方程 / 解误差容限 | $\varepsilon_e$ 控 $\lvert\Phi\rvert$、$\varepsilon_s$ 控 $\lvert q^{(i)}-q^{(i-1)}\rvert$，二者皆满足才停 |
| Taylor linearization | 泰勒线性化 | 在 $q^{(i)}$ 处一阶展开丢高阶项，化非线性为线性 |
| row rank | 行秩 | 雅可比独立行数；高斯消元后非零行数 |
| full row rank | 行满秩 | 行秩 $=$ 行数；约束彼此独立、无冗余 |
| redundant constraint elimination algorithm | 冗余约束消除算法 | §4.6 的 6 步流程：测秩→剔冗余运动学→报独立坐标→接驱动→剔冗余驱动→查够用 |
| redundant driving constraint | 冗余驱动约束 | Eq. 4.6.8 中 $\boldsymbol{\Phi}^D_{\mathbf{v}'}$ 零行对应者；须移除并替换 |
| restricted (column-only) pivoting | 受限选主元 | 走过运动学约束行时只许列交换，越过后再全选主元，防止误剔运动学约束 |
| DADS (Dynamic Analysis and Design System) | DADS（动态分析与设计系统） | 实现本书理论的大型运动学/动力学代码；平面例见第 5、8 章，空间见第 10、12 章 |
| preprocessor / postprocessor | 前处理器 / 后处理器 | DADS 三大部件之二；前者收集数据、后者显示结果（Fig. 4.1.1） |
| kinematic analysis program | 运动学分析程序 | DADS 三大部件之一；内部含 ANALYSIS/JUNCTION/MODULES 三层（Fig. 4.1.2） |
| dynamic analysis program | 动力学分析程序 | DADS 三大部件之一（动力学侧）；同含 ANALYSIS/JUNCTION/MODULES 三层（Fig. 7.1.2） |
| force element module | 力元模块 | MODULES 层组件；生成运动方程所需的力数据 |
| ANALYSIS / JUNCTION / MODULES | 分析 / 枢纽 / 模块 | 运动学分析程序三层结构：ANALYSIS 控流程、JUNCTION 分派、MODULES 只算各自项 |
| flag | 标志（整型） | ANALYSIS 用其标记当前分析阶段，据以向 JUNCTION 下达组装指令 |
| nonzero entry scheme | 非零条目方案 | 每个关节模块只吐出自己那几个雅可比非零条目及行列指针；§4.2 |
| four modes of kinematic analysis | 运动学分析四种模式 | 装配、位置、速度、加速度；前三/四模式难度递降 |
| assembled configuration | 装配构型 | 满足全部约束的协调构型；装配模式之目标 |
| assembly minimization | 装配最小化 | §3.6；把约束违背量做目标函数极小化，比直接 Newton 更稳健 |
| initial-value problem | 初值问题 | $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},t)$ 加初值 $\mathbf{x}(t_0)=\mathbf{x}^0$（Eq. 7.4.1）；非线性 ODE 仅保证**局部**解 |
| polynomial interpolation | 多项式插值 | 用多项式 $P(t)$ 在若干点与 $f$（及其导数）相等来逼近 $f$；数值积分的地基 |
| Taylor polynomial | 泰勒多项式 | 单点、多阶导数逼近（Eq. 7.4.2）；理论用，不宜作通用积分 |
| Newton backward difference polynomial | Newton 后向差分多项式 | 多点、函数值逼近（Eq. 7.4.4）；Adams 族基础 |
| backward difference | 后向差分 | $\nabla^i f_n$，递推 $\nabla^i f_n=\nabla^{i-1}f_n-\nabla^{i-1}f_{n-1}$ |
| interpolation error | 插值误差 | $f(t)-P_k(t)\approx\frac{f^{(k)}(\xi)}{k!}\prod(t-t_{n-j})$（Eq. 7.4.8）；可用后向差分实时估计 |
| Adams–Bashforth predictor | Adams–Bashforth 预测器 | 显式多步公式 $\mathbf{x}_{n+1}^p=\mathbf{x}_n+h\sum_{i=1}^{k}\gamma_{i-1}\nabla^{i-1}\mathbf{f}_n$（Eq. 7.4.11）；$k=1$ 即 Euler |
| Adams–Moulton corrector | Adams–Moulton 校正器 | 隐式公式 $\mathbf{x}_{n+1}^c=\mathbf{x}_n+h\sum_{i=1}^{k+1}\gamma_{i-1}^*\nabla^{i-1}\mathbf{f}_{n+1}^p$（Eq. 7.4.15）；比预测器高一阶 |
| explicit / implicit method | 显式 / 隐式方法 | 显式：$\mathbf{x}_{n+1}$ 只在左端由已知量定；隐式：两端都含 $\mathbf{x}_{n+1}$ |
| Euler method | Euler 法 | $\mathbf{x}_{n+1}=\mathbf{x}_n+h\mathbf{f}_n$；$k=1$ 的 Adams–Bashforth |
| local truncation error | 局部截断误差 | 用插值多项式逼近导数所致；预测器 $\sim h^{k+1}$（Eq. 7.4.13），校正器 $\sim h^{k+2}$（Eq. 7.4.16） |
| self-starting algorithm | 自启动算法 | 从 $k=1$ 逐步升阶，仅需微分方程与初值 |
| PECE method | PECE 方法 | Predict–Evaluate–Correct–Evaluate，每步两次 $\mathbf{f}$ 求值；$k$ 阶预测 + $(k+1)$ 阶校正为最佳配对 |

## 四、机构实例 (Mechanism Examples)

| English | 中文（统一译名） | 备注 |
|---------|----------------|------|
| simple pendulum | 单摆 | |
| slider–crank (mechanism) | 曲柄滑块（机构） | |
| crank | 曲柄 | |
| coupler | 耦合体 / 连杆 | |
| linkage | 连杆机构 | |
| four-bar (linkage) | 四连杆（机构） | |
| parallelogram four-bar | 平行四边形四连杆 | 等长两对杆；分岔典型例 |
| quick-return | 快回（机构） | |
| cam-follower | 凸轮-挺杆 | |
| slider | 滑块 | |
| slide axis | 滑轨 | |
| compressor | 压缩机 | 曲柄滑块的一种应用（§8.2）；滑块在压缩腔内往复 |
| flywheel | 飞轮 | 大转动惯量储能件；平抑角速度波动、渡过高阻力半循环（§8.2） |
| shaper | 牛头刨床 | 快回机构的金属切削应用（§8.3, Fig 1.1.8） |

## 五、动力学 (Dynamics)

| English | 中文（统一译名） | 备注 / 不采用的译法 |
|---------|----------------|--------------------|
| equations of motion | 运动方程 | |
| three modes of dynamic analysis | 动力学分析三模式 | 平衡 / 逆动力学 / 动力学（§7.1） |
| equilibrium analysis | 平衡分析 | 求外力下静止构型；经动态沉降或总势能最小化 |
| dynamic analysis | 动力学分析 | 给定力，积分混合 DAE 求随时间运动 |
| inverse dynamic analysis | 逆动力学分析 | 运动由运动学定死，反求所需拉格朗日乘子与力/力矩 |
| dynamic settling | 动态沉降 | 用动力学积分让系统自然稳定到平衡；平衡分析两法之一 |
| variational equations of motion | 变分运动方程 | 虚功形式，$\delta\mathbf{q}^T[\dots]=0$ |
| virtual work | 虚功 | $\delta W$ |
| principle of virtual work | 虚功原理 | 即达朗贝尔原理 |
| D'Alembert's principle | 达朗贝尔原理 | 惯性力虚功 = 外力虚功 |
| internal / external force | 内力 / 外力 | 内力沿两点连线，虚功为零 |
| centroid / center of mass | 质心 | 首次可标 (centroid)；$\int_m\mathbf{s}'^P dm=\mathbf{0}$ |
| centroidal reference frame | 质心参考系 | 原点在质心的随体系 $x'\text{-}y'$ |
| polar moment of inertia | 极转动惯量 | $J'$；**统一用**"极转动惯量"，不混用"极惯性矩" |
| parallel axis theorem | 平行轴定理 | $J''=J'+m\lvert\boldsymbol{\rho}''\rvert^2$ |
| composite body / component | 组合体 / 部件 | 由标准形状子部件拼成 |
| void | 空洞 | 计算惯性时按负质量处理 |
| resultant force / torque | 合力 / 合力矩 | $\mathbf{F}$、$n$ |
| Newton–Euler equations | 牛顿-欧拉方程 | $m\ddot{\mathbf{r}}=\mathbf{F}$，$J'\ddot{\phi}=n$ |
| generalized force | 广义力 | $\mathbf{Q}$，与广义坐标 $\mathbf{q}$ 配对 |
| equilibrium | 平衡 | $\ddot{\mathbf{q}}=\dot{\mathbf{q}}=\mathbf{0}$；外力下保持静止 |
| equilibrium equations | 平衡方程 | $\boldsymbol{\Phi}_\mathbf{q}^T\boldsymbol{\lambda}=\mathbf{Q}^A$（Eq. 6.5.2）；稳定/不稳定平衡皆满足 |
| stable / unstable equilibrium | 稳定 / 不稳定平衡 | 扰动后回落为稳定；倒立为不稳定 |
| conservative system | 保守系统 | 力可由势能导出，功与路径无关 |
| principle of minimum total potential energy | 总势能最小原理 | 稳定平衡 $\Leftrightarrow$ 总势能取严格局部极小 |
| total potential energy (TPE) | 总势能 | $TPE=SE-W(F)$（Eq. 6.5.3） |
| strain energy | 应变能 | $SE$；线性弹簧 $\tfrac12 k(\ell-\ell_0)^2$（Eq. 6.5.4） |
| torsional / rotational spring | 扭转弹簧 | 常数 $k_\theta$，储能 $\tfrac12 k_\theta(\theta-\theta_0)^2$ |
| double pendulum | 双摆 | 两杆铰接；例 6.5.2 |
| constraint reaction force | 约束反力 | 打断约束 $k$ 后作用于两体的力；$\mathbf{F}_i''^k=-\mathbf{C}_i^T\mathbf{A}_i^T\boldsymbol{\Phi}_{\mathbf{r}_i}^{kT}\boldsymbol{\lambda}^k$（Eq. 6.6.8） |
| joint reaction torque | 关节反力矩 | $T_i''^k$（Eq. 6.6.9）；转动关节为 0，移动关节一般非零 |
| body-fixed joint frame | 关节随体系 | $x''\text{-}y''$，原点在关节作用点 $P$；反力/反力矩在此系中输出 |
| system equilibrium equations | 系统平衡方程 | $\boldsymbol\Phi_{\mathbf q}^T\boldsymbol\lambda=\mathbf Q^A,\ \boldsymbol\Phi=\mathbf 0$（Eq. 7.5.2）；对 $\mathbf q,\boldsymbol\lambda$ 非线性，稳定/不稳定平衡皆满足，故直接求解不推荐 |
| dynamic settling | 动态沉降 | 积分运动方程至 $\dot{\mathbf q}=\ddot{\mathbf q}=\mathbf 0$；最普适，可加人为阻尼加速；多平衡态时唯一有效法 |
| minimum total potential energy | 总势能最小 | 仅保守系统；稳定平衡 $\Leftrightarrow V(\mathbf q_e)<V(\mathbf q)$（Eq. 7.5.3）在 $\boldsymbol\Phi=\mathbf 0$ 上 |
| work function | 功函数 | $W$；力做功的位置函数，势能取其负 $V=-W$（常力 Eq. 7.5.6–7.5.7） |
| potential energy of a force | 力的势能 | 常力 $V_{\mathbf F}=-\mathbf F^T\mathbf r^P$；平移元件 $V_f$（Eq. 7.5.11）；扭转元件 $V_\tau$（Eq. 7.5.12） |
| gradient of total potential energy | 总势能梯度 | $V_{\mathbf q}^T=-\mathbf Q^A$（Eq. 7.5.14）；等于广义外力的相反数，故建方程时现成可用 |
| constrained / unconstrained minimization | 约束 / 无约束极小化 | 平衡 = 在 $\boldsymbol\Phi=\mathbf 0$ 上极小化 $V$；经坐标划分转为对独立坐标 $\mathbf v$ 的无约束极小化 $V(\mathbf v)$（Eq. 7.5.22） |
| generalized coordinate partitioning | 广义坐标划分 | $\mathbf q=[\mathbf u^T,\mathbf v^T]^T$，$\mathbf u$ 非独立、$\mathbf v$ 独立；$\boldsymbol\Phi_{\mathbf u}$ 取非奇异（§7.2） |
| influence coefficient matrix | 影响系数矩阵 | $\mathbf H=-\boldsymbol\Phi_{\mathbf u}^{-1}\boldsymbol\Phi_{\mathbf v}$（Eq. 7.5.17），$\mathrm d\mathbf u=\mathbf H\,\mathrm d\mathbf v$；逐列解 $\boldsymbol\Phi_{\mathbf u}\mathbf H^{(i)}=-\boldsymbol\Phi_{\mathbf v}^{(i)}$ |
| inertia properties | 惯性性质 | 各刚体的质量与极转动惯量；动力学建模四步之一（§8.1） |
| composite joints / massless links | 复合关节 / 无质量连杆 | 把两基本约束合成一个以简化模型；代价是忽略连杆质量特性（§8.1） |
| lumped mass approximation | 集中质量近似 | 把连杆质量分配为端点集中质量以改善近似；非精确等价于真实质量分布（§8.1） |
| qualitative understanding | 定性理解 | 凭经验判断动力学结果合理性、指导设计的直觉；工具正确不能替代（§8.1） |
| parameter study | 参数研究 | 系统改变尺寸/质量/力，观察对动力学响应的影响（§8.2–§8.5 贯穿手法） |
| gas force | 气体力 | 压缩气体对滑块的阻力 $F_c$；单向、依速度门控（仅 $\dot x_3>0$ 作用，Eq. 8.2.1） |
| compression / intake stroke | 压缩 / 进气冲程 | 滑块向右压气（$\dot x_3>0$）/ 向左吸气（$\dot x_3\le0$，无气体力） |
| steady-state motion | 稳态运动 | 一周期内输入功=耗散功，机构进入周期性运行（§8.2 选驱动力矩 41,450 N·m 之依据） |
| driving torque | 驱动力矩 | 维持给定运动所需的力矩；逆动力学由拉格朗日乘子给出（Fig 8.2.4a） |
| quick-return mechanism | 快回机构 | 工作行程慢而有力、回程快的机构；牛头刨床用之（§8.3, Fig 5.4.1） |
| cutting force | 切削力 | 刀具-工件去料所需力 $F_c$；本例恒值 $200{,}000$ N，单向门控（仅切削行程 $\dot x_6<0$ 作用，Fig 8.3.1） |
| cutting / return stroke | 切削 / 回程 | 切削行程 $\dot x_6<0$（慢、有切削力）/ 回程 $\dot x_6>0$（快、无切削力） |
| flywheel inertia effect | 飞轮惯量效应 | 惯量↑→转速波动↓；但对循环速率与轴承反力波动的影响方向随机构而变（§8.3 与 §8.2 相反） |
| coil spring | 螺旋弹簧 | 分布质量连续体；本节用集中质量链离散建模（§8.4, Fig 8.4.1） |
| lumped mass model | 集中质量模型 | 把连续弹簧均分成段，每段质量效应用集中质量 $m$ 代替、以刚度 $k$ 小弹簧连接（§8.4） |
| surge wave | 行波 / 喘振波 | 弹簧内沿长度传播并在固定端反射的扰动波；末端给初速激发（§8.4.1, Fig 8.4.2） |
| springs in series / equivalent stiffness | 弹簧串联 / 等效刚度 | 各段同受一力、变形相加；$1/k_e=\sum 1/k_i$，6 段同 $k$ 时 $k_e=k/6$（§8.4.2） |
| unilateral spring | 单侧弹簧 | 双线性接触弹簧：变形为正（分离）$F=0$，变形为负（接触）产生极大斥力 $K=10^6$ N/m（§8.4.2, Fig 8.4.4） |
| impact | 冲击 | 重物 $M$ 撞弹簧自由端；用单侧弹簧建模、仿真起始即发生（§8.4.2, Fig 8.4.3） |
| chattering | 颤振 | 冲击后两体在接触面反复高频接触-分离；$k$↑→波速↑→周期↓（§8.4.2, Fig 8.4.8） |
| separation | 分离 | 两体不再互推之时刻/位置；弹簧有质量使分离位置超过静平衡位（$1.27>1.2$ m，§8.4.2） |
| unilateral damper | 单侧阻尼器 | 仅接触时作用的阻尼，$F_d=200\ \text{N·s/m}\times\dot\ell$；抑制颤振位移与周期（§8.4.2, Fig 8.4.9） |
| wave propagation speed | 波传播速度 | 弹簧越硬（$k$↑）波速越快，故颤振周期越短（§8.4.2） |
| valve-lifter mechanism | 气门挺杆机构 | 内燃机凸轮驱动气门；§5.6 运动学模型补气门弹簧后做逆动力学（§8.5, Fig 5.6.1） |
| valve spring | 气门弹簧 | 把挺杆压在凸轮上、防分离的回位弹簧；刚度须保证高速下反力不变负（§8.5） |
| pushrod reaction force | 推杆反力 | 凸轮-挺杆接触反力 $N$，由逆动力学 Lagrange 乘子给出；$N\ge0$ 为可接受判据（§8.5, Fig 8.5.1） |
| cam–flat-faced follower joint | 凸轮-平面挺杆关节 | 单侧接触：只能推不能拉，物理 $N\ge0$；模型双侧约束下解出 $N<0$ 即分离信号（§8.5） |
| negative reaction force / separation criterion | 负反力 / 分离判据 | 逆动力学反力变负 ⟺ 真实凸轮-挺杆已分离、设计不可接受；$k$↑抗分离、$\omega$↑（惯性力 $\propto\omega^2$）易分离（§8.5） |

---

## 维护说明

- 与既有笔记冲突时，**以本表为准**，并回头修订旧笔记（如 `joint` 已从"铰"统一为"关节"、`configuration` 已从"位形"统一为"构型"）。
- 同一英文若在不同语境有不同中文（如 body=物体/刚体、coupler=耦合体/连杆），在"备注"列注明取舍条件。
