---
type: glossary
parent: computer-aided-kinematics-and-dynamics
title: "术语中英对照表 (Terminology Glossary)"
created: 2026-06-09
last_updated: 2026-06-11
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
| relative constraint | 相对约束 | 体与体 |
| driving constraint | 驱动约束 | |
| kinematically driven | 运动学驱动的 | |
| driver | 驱动器 | |
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

---

## 维护说明

- 与既有笔记冲突时，**以本表为准**，并回头修订旧笔记（如 `joint` 已从"铰"统一为"关节"、`configuration` 已从"位形"统一为"构型"）。
- 同一英文若在不同语境有不同中文（如 body=物体/刚体、coupler=耦合体/连杆），在"备注"列注明取舍条件。
