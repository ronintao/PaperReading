---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 9
title: "Spatial Cartesian Kinematics"
pages: 305-375
sections:
  - "9.1 Vectors in Space"
  - "9.2 Kinematics of a Rigid Body in Space"
  - "9.3 Euler Parameter Orientation Generalized Coordinates"
  - "9.4 Kinematic Constraints"
  - "9.5 Driving Constraints"
  - "9.6 Position, Velocity, and Acceleration Analysis"
created: 2026-05-18
last_updated: 2026-05-18
---

# Chapter 9: Spatial Cartesian Kinematics

## 章节定位

本章是全书 **Part Two（空间运动学与动力学）的入门**，把第 3 章的平面笛卡尔运动学方法系统地推广到三维空间。承担三件事：（1）把第 2 章的平面向量代数扩展为空间向量代数（叉积、tilde 算子、刚体方向余弦矩阵）；（2）引入 **Euler 参数**作为无奇异的姿态广义坐标，建立角速度/虚旋转与参数导数/变分之间的桥梁；（3）建立空间运动副约束库（基本约束 → 6 类基本运动副 → 7 类复合关节 → 4 类驱动约束），并给出位置/速度/加速度统一求解框架。

本章 **不讨论**动力学方程的建立（留给 Ch.10–11 处理空间动力学），也 **不深入数值实现细节**（沿用 Ch.4 的数值方法）。前置知识：Ch.2 平面向量与矩阵微积分、Ch.3 平面笛卡尔运动学（约束库与 N-R 求解结构）、Ch.4 装配/N-R/秩判断的数值方法。

---

## 概念定义

### §9.1 空间向量

**Geometric Vector（几何向量）** [p.306]
> A *geometric vector*, or simply a vector, is defined as the directed line segment from one point in space to another point in space.
>
> 几何向量（或简称向量）定义为空间中从一点到另一点的有向线段。

---

**Magnitude of a Vector（向量的模/长度）** [p.306]
> The *magnitude of a vector* ã is its length (the distance between A and B) and is denoted by a or |ã|.
>
> 向量 ã 的模是其长度（A 与 B 之间的距离），记为 a 或 |ã|。

---

**Unit Vector / Zero Vector（单位向量 / 零向量）** [p.306]
> A *unit vector*, having a length of 1 unit, in the direction ã ≠ 0̃ is (1/a)ã. ... A vector with zero length is denoted as 0̃ and is called the *zero vector*.
>
> 长度为 1 的向量为单位向量；长度为 0 的向量记为 0̃，为零向量。

---

**Parallelogram Rule（平行四边形法则）** [p.307]
> Two vectors ã and b̃ are added according to the *parallelogram rule*…
>
> 两个向量按平行四边形法则相加。

---

**Cartesian Reference Frame / Cartesian Components / Direction Cosines（笛卡尔参考系/分量/方向余弦）** [p.308–309]
> Such a frame is called a *Cartesian reference frame*. … These components are called the *Cartesian components of the vector*. … The quantities cos θ(ĩ, ã), cos θ(j̃, ã), and cos θ(k̃, ã) are called the *direction cosines of vector* ã.
>
> 右手正交 x-y-z 系称为笛卡尔参考系；向量沿三轴投影称为笛卡尔分量；与三坐标轴单位向量夹角的余弦称为方向余弦。

---

**Scalar / Dot Product（标量积/点积）** [p.309]
> The *scalar product* (sometimes called the *dot product*) of two vectors ã and b̃ is defined as the product of their magnitudes and the cosine of the angle between them.
>
> 两个向量的标量积定义为模的乘积与夹角余弦的乘积。

---

**Orthogonal Vectors（正交向量）** [p.309]
> Two nonzero vectors are said to be *orthogonal vectors* if their scalar product is zero.
>
> 若两个非零向量的标量积为零，则称它们正交。

---

**Vector / Cross Product（向量积/叉积）** [p.310]
> A new concept for spatial vectors is the *vector product* (sometimes called the *cross product*) of two vectors ã and b̃, defined as the vector ã × b̃ = ab sin θ(ã, b̃)ũ.
>
> 空间向量独有的新概念——叉积，定义为 ã × b̃ = ab sin θ(ã, b̃)ũ，ũ 是垂直于 ã,b̃ 平面的右手单位向量。

---

**Algebraic Vector（代数向量）** [p.311]
> This is the *algebraic representation of a geometric vector*.
>
> 几何向量在选定参考系下用列矩阵 **a** = [aₓ, a_y, a_z]^T 表达，称为代数向量；依赖参考系。

---

**Skew-Symmetric Matrix / Tilde Operator（反对称矩阵 / 波浪号算子）** [p.312–313]
> A skew-symmetric matrix ã associated with an algebraic vector **a** = [aₓ, a_y, a_z]^T is defined as…
>
> 与代数向量 **a** 关联的反对称矩阵 ã 是一个 3×3 矩阵，使叉积 c̃ = ã × b̃ 写成矩阵乘法 **c = ã b**。

---

**Centripetal Acceleration（向心加速度）** [p.317]
> This is the classical *centripetal acceleration* of a point that moves on a circular path, since the direction of r̈ is opposite to the direction of **r**.
>
> 圆周运动质点 r̈ = −ω²r 方向与位置向量相反，即向心加速度。

---

### §9.2 刚体空间运动学

**Body-Fixed Reference Frame（体固定参考系）** [p.318]
> The geometry of the body … may be defined in an x'-y'-z' reference frame that is fixed to the body, called a *body-fixed reference frame*.
>
> 固定在刚体上的 x'-y'-z' 参考系。又名"工程制图参考系"。

---

**Direction Cosine Matrix / Rotation Transformation Matrix（方向余弦矩阵 / 旋转变换矩阵）** [p.322]
> Where **A** is called the *direction cosine matrix* or *rotation transformation matrix*.
>
> 把向量从体固定系变换到全局系的 3×3 正交矩阵 **A**。

---

**Orthogonal Matrix（正交矩阵）** [p.322]
> A^T A = I and the direction cosine matrix **A** is an *orthogonal matrix*.
>
> A^T A = I，故 A 是正交矩阵，A^{-1} = A^T。

---

**Angular Velocity（角速度）** [p.330]
> ȦA^T is skew-symmetric. … There exists a vector **ω**, called the *angular velocity* of the x'-y'-z' frame.
>
> 体固定系相对全局系的角速度向量 ω，由反对称矩阵 ω̃ ≡ ȦA^T 唯一定义。

---

**Virtual Displacement / Virtual Rotation（虚位移 / 虚旋转）** [p.332–333]
> A *virtual displacement* δr^P of point P is defined as an *infinitesimal displacement* … with time held fixed. … δπ plays the role of a rotation, called a *virtual rotation* of the x'-y'-z' reference frame.
>
> 虚位移：时间冻结下点的无穷小位移；虚旋转：时间冻结下体固定系的无穷小转动 δπ。**虽然有限旋转不是向量，但虚旋转是向量**，可加可分量化。

---

### §9.3 Euler 参数

**Euler's Theorem（Euler 定理）** [p.336]
> Euler's Theorem states that for any given orientation of the body, there exists an axis passing through the origin about which the reference frame can be rotated through an angle χ to achieve the desired orientation.
>
> 对刚体任意姿态，必存在过原点的轴 u，使体固定系绕 u 转角 χ 即可到达目标姿态。

---

**Euler Parameters（Euler 参数）** [p.338]
> The set of four *Euler parameters*, defined as e₀ ≡ cos(χ/2), **e** = [e₁, e₂, e₃]^T ≡ **u** sin(χ/2).
>
> 4 个 Euler 参数 p = [e₀; e]：编码旋转轴 u 与转角 χ。等价于单位四元数。

---

**Euler Parameter Normalization Constraint（Euler 参数归一化约束）** [p.340]
> They must satisfy the *Euler parameter normalization constraint* p^T p = e₀² + e₁² + e₂² + e₃² = 1.
>
> 4 个 Euler 参数受单位范数约束 p^T p = 1（Eq.9.3.9）。

---

**Quasi-Coordinate（准坐标）** [p.347]
> Angular velocity is not the time derivative of any vector. For this reason, angular velocity is often called a *quasi-coordinate* in the dynamics literature.
>
> 角速度不是任何向量的时间导数（不可积），故称"准坐标"。直接含义：不存在"角度向量"使其时间导数为 ω。

---

### §9.4 运动学约束

**Joint Definition Frame（关节定义坐标系）** [p.348]
> x''_i-y''_i-z''_i *joint definition frame* is attached to the body, with its origin at point P_i.
>
> 附在体 i 上原点为 P_i 的局部参考系；由 fᵢ, gᵢ, hᵢ 三个体固定单位向量构成，专用于声明关节几何。

---

**Dot-1 Constraint（点积-1 约束）** [p.350]
> This condition is called the *dot-1 constraint* between vectors **a**_i and **a**_j.
>
> 两体固定向量 aᵢ⊥aⱼ 的条件：Φ^d1 = aᵢ^T aⱼ = 0。仅约束姿态。

---

**Dot-2 Constraint（点积-2 约束）** [p.351]
> This condition is called the *dot-2 constraint* between vectors **a**_i and **d**_ij.
>
> 体固定向量 aᵢ 与连线 dᵢⱼ 正交：Φ^d2 = aᵢ^T dᵢⱼ = 0。同时约束位置与姿态。

---

**Spherical Constraint / Ball Joint（球副 / 球铰）** [p.353]
> A *spherical pair* (or *ball-and-socket joint*) … permits any orientation of body j relative to body i, but does not allow relative translation between the bodies.
>
> 一对点 Pᵢ=Pⱼ 始终重合：3 方程，3 相对 DOF。

---

**Absolute Constraint（绝对约束）** [p.355]
> *Absolute constraints* on a single body i are obtained by setting a coordinate of point P_i on body i, or an Euler parameter, to a constant.
>
> 把体 i 的位置坐标或 Euler 参数固定为常数（或函数），等价于把该 DOF 对地锁死。

---

**Parallel-1 / Parallel-2 Constraint（平行-1 / 平行-2 约束）** [p.357–359]
> Vectors **h**_i and **h**_j are *parallel*. … Two scalar constraint equations are required.
>
> 用两个 dot-1 表达 hᵢ ∥ hⱼ（Φ^p1，2 方程）；用两个 dot-2 表达 hᵢ ∥ dᵢⱼ（Φ^p2，2 方程）。

---

**Universal Joint（万向节）** [p.360]
> A *universal joint* … is constructed by … two revolute joints whose axes intersect orthogonally.
>
> 球副 + 两轴 dot-1 正交 = 4 方程，2 DOF。当两叉夹角 φ=π/2 时出现奇异（驱动轴锁死，Fig. 9.4.15）。

---

**Revolute Joint（转动副）** [p.366]
> A *revolute joint* … allows relative rotation about a common axis, but precludes relative translation along this axis.
>
> 共轴铰链 = 球副 + Φ^p1：5 方程，1 DOF（绕公共轴转）。

---

**Cylindrical Joint（柱铰）** [p.367–368]
> A *cylindrical joint* … allows relative rotation about a common axis … and relative translation along this axis.
>
> 共线条件 Φ^p1 + Φ^p2：4 方程，2 DOF（绕轴转 + 沿轴滑）。

---

**Translational Joint（平移副 / 滑动副）** [p.369–370]
> The *translational joint* … allows relative translation along a common axis …, but precludes relative rotation about this axis.
>
> 柱铰 + 1 个 fᵢ⊥fⱼ：5 方程，1 DOF（仅沿轴滑）。

---

**Screw Joint（螺旋副）** [p.372]
> The *screw joint* … is a cylindrical joint …, with the additional condition that relative translation along the common axis of rotation is specified by a *screw pitch* α times the relative angle of rotation.
>
> 柱铰 + 螺距耦合 hᵢ^T dᵢⱼ = α(θ + 2nπ − θ₀)：5 方程，1 DOF。

---

**Composite Joint / Coupler（复合关节 / 联接杆）** [p.373]
> A pair of bodies is connected by an intermediate body (or *coupler*) … called a *composite joint*.
>
> 把"两端铰 + 杆"等价代换成两端体之间的直接约束，省去 coupler 自身坐标。

---

**Spherical–Spherical Joint（球-球复合铰）** [p.373–374]
> The analytical definition of the spherical-spherical joint is simply that the distance between points P_i and P_j be equal to C ≠ 0.
>
> 两端球铰 + 等长杆 → 点距 = 杆长 C：1 方程，5 DOF。

---

**Strut Composite Joint（支柱复合铰）** [p.379–380]
> A coupler that has a cylindrical joint about the fixed vector h_i in body i and a spherical joint at point P_j in body j.
>
> 一端柱铰、一端球铰：hᵢ ∥ dᵢⱼ（Φ^p2 = 0）：2 方程，4 DOF。

---

### §9.5 驱动约束

**Driving Constraint（驱动约束）** [p.380]
> Such time-dependent constraints are called *driving constraints*.
>
> 含时间函数 C(t) 的约束，把执行器（液压缸/伺服电机）的运动历史强加给系统。

---

**Absolute Driver（绝对驱动）** [p.380]
> The first three constraints of Eq. 9.4.15 may be written as time-dependent absolute drivers.
>
> Φ^kd = (xᵢᴾ/yᵢᴾ/zᵢᴾ) − Cₖ(t) = 0：直接驱动笛卡尔坐标，每个锁住 1 DOF。

---

**Distance / Translational / Rotational Driver（距离 / 平移 / 转动驱动）** [p.380–382]
> Φ^ssd = Φ^ss(P_i, P_j, 0) − (C(t))² ; Φ^td = Φ^d2(h_i, d_ij) − C(t) ; Φ^rotd ≡ θ + 2nπ − C(t)
>
> 三种相对量驱动：两点距离²、沿轴位移、绕轴转角分别 = 给定函数。

---

### §9.6 求解三段方程

**Generalized Coordinates of Body / System（体/系统广义坐标）** [p.382]
> qᵢ = [rᵢ; pᵢ] ; q = [q₁^T, …, q_{nb}^T]^T.
>
> 单体 7 元 = 3 位置 + 4 Euler；系统坐标 7nb 维。

---

**Velocity Coefficient Matrix（速度系数矩阵）** [p.385]
> The coefficient matrix in the velocity equations of Eq. 9.6.12 is different from the Jacobian matrix in position analysis.
>
> 用 ω' 表达的速度方程系数矩阵；与位置 Jacobian Φ_q **不同**，但同样必须非奇异。

---

## 符号定义

> [!note]
> 全章符号体系正式确立于本章；后续 Ch.10–11 空间动力学沿用。本表按出现节顺序分组。

### §9.1 向量基础

| 符号 | 类型 | 含义 |
|------|------|------|
| $\tilde{a},\tilde{b},\tilde{c}$ | 几何向量 | 空间中的有向线段 |
| $a, |\tilde{a}|$ | 标量 | 向量的模 |
| $\tilde{0}$ | 几何向量 | 零向量 |
| $\tilde{i},\tilde{j},\tilde{k}$ | 单位向量 | x, y, z 轴方向单位向量 |
| $\theta(\tilde{a},\tilde{b})$ | 角度 | 两向量夹角 |
| $\mathbf{a},\mathbf{b},\mathbf{c}$ | 列矩阵 (3×1) | 几何向量的代数表示 |
| $\tilde{\mathbf{a}}$ | 反对称矩阵 (3×3) | tilde 算子；使 $\mathbf{c}=\tilde{\mathbf{a}}\mathbf{b}$ 表示叉积 |

### §9.2 刚体运动学

| 符号 | 类型 | 含义 |
|------|------|------|
| $x'\text{-}y'\text{-}z'$ | 参考系 | 体固定系 |
| $\mathbf{f}',\mathbf{g}',\mathbf{h}'$ | 单位向量 | 体固定系三个轴向量 |
| $\mathbf{A}$ | 3×3 正交矩阵 | 方向余弦/旋转变换矩阵，$\mathbf{s} = \mathbf{A}\mathbf{s}'$ |
| $\mathbf{r}$ | 3×1 向量 | 全局系到体固定系原点的平移向量 |
| $\mathbf{s}'^P$ | 3×1 常向量 | 点 P 在体固定系中的坐标 |
| $\mathbf{r}^P$ | 3×1 向量 | 点 P 在全局系中的位置 = $\mathbf{r}+\mathbf{A}\mathbf{s}'^P$ |
| $\boldsymbol{\omega}$ | 3×1 向量 | 角速度（全局系分量） |
| $\boldsymbol{\omega}'$ | 3×1 向量 | 角速度（体固定系分量），$\boldsymbol{\omega}'=\mathbf{A}^T\boldsymbol{\omega}$ |
| $\tilde{\boldsymbol{\omega}}$ | 3×3 反对称矩阵 | $\tilde{\boldsymbol{\omega}}=\dot{\mathbf{A}}\mathbf{A}^T$ |
| $\delta\mathbf{r},\delta\boldsymbol{\pi},\delta\boldsymbol{\pi}'$ | 3×1 向量 | 平移虚位移、虚旋转（全局/体固定） |
| $\mathbf{A}_{ij}$ | 3×3 矩阵 | 体 j 相对体 i 的相对变换：$\mathbf{A}_{ij}=\mathbf{A}_i^T\mathbf{A}_j$ |

### §9.3 Euler 参数

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{u}$ | 3×1 单位向量 | Euler 旋转轴 |
| $\chi$ | 标量 | Euler 旋转角 |
| $e_0$ | 标量 | $\cos(\chi/2)$ |
| $\mathbf{e}$ | 3×1 向量 | $\mathbf{u}\sin(\chi/2)$ |
| $\mathbf{p}$ | 4×1 向量 | $[e_0;\mathbf{e}]$ Euler 参数 |
| $\mathbf{E}$ | 3×4 矩阵 | $\mathbf{E}=[-\mathbf{e},\;\tilde{\mathbf{e}}+e_0\mathbf{I}]$ |
| $\mathbf{G}$ | 3×4 矩阵 | $\mathbf{G}=[-\mathbf{e},\;-\tilde{\mathbf{e}}+e_0\mathbf{I}]$ |
| $\mathrm{tr}\,\mathbf{A}$ | 标量 | A 的迹 |

### §9.4–§9.5 运动副与驱动

| 符号 | 类型 | 含义 |
|------|------|------|
| $P_i, Q_i$ | 点 | 体 i 上的关节定义点 |
| $\mathbf{f}_i,\mathbf{g}_i,\mathbf{h}_i$ | 单位向量 | 关节定义系轴向量（体固定常量） |
| $\mathbf{C}_i^p$ | 3×3 正交矩阵 | 关节定义系到体固定系的变换 = $[\mathbf{f}'_i,\mathbf{g}'_i,\mathbf{h}'_i]$ |
| $\mathbf{d}_{ij}$ | 3×1 向量 | $P_i$ 到 $P_j$ 的连线向量 |
| $\Phi^{d1}, \Phi^{d2}$ | 标量 | dot-1 / dot-2 约束 |
| $\Phi^{p1}, \Phi^{p2}$ | 2×1 向量 | 平行-1 / 平行-2 约束 |
| $\Phi^{s}$ | 3×1 向量 | 球副约束 |
| $\Phi^{ss}$ | 标量 | 球-球距离-平方约束 |
| $\Phi^{scr}$ | 标量 | 螺旋副附加方程 |
| $\alpha$ | 标量 | 螺旋副螺距（轴向位移/转角） |
| $\theta, n, \theta_0$ | 标量 | 相对转角、累计圈数、初始角 |
| $C(t)$ | 标量函数 | 驱动函数；$\dot C, \ddot C$ 为速度/加速度项 |

### §9.6 求解变量

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{q}_i = [\mathbf{r}_i;\mathbf{p}_i]$ | 7×1 向量 | 单体广义坐标 |
| $\mathbf{q}$ | 7nb×1 向量 | 系统广义坐标 |
| $\Phi^K, \Phi^D, \Phi^P$ | 向量函数 | 运动学/驱动/Euler归一化约束 |
| $\Phi_\mathbf{q}$ | $7nb\times 7nb$ 矩阵 | 位置 Jacobian |
| $\boldsymbol{\nu}^K, \boldsymbol{\nu}^D$ | 向量 | 速度方程右端 = $-\Phi_t$ |
| $\boldsymbol{\gamma}^K, \boldsymbol{\gamma}^D$ | 向量 | 加速度方程右端 |

---

## 核心论点

### 1. 平面 → 空间的关键差异：叉积与不可交换旋转

| 维度 | 平面（Ch.2/3）| 空间（Ch.9）|
|------|---------------|-------------|
| 向量积 | 不存在；旋转用单角度 $\phi$ | 叉积 $\tilde{a}\times\tilde{b}$，tilde 算子 $\tilde{\mathbf{a}}$ |
| 姿态自由度 | 1 | 3（9 个方向余弦 − 6 个正交约束）|
| 大旋转交换性 | 仍可交换（标量加） | **不可交换**（Fig. 9.2.3/9.2.4）|
| 角速度 | 标量 $\dot\phi$ | 向量 $\boldsymbol{\omega}$，且为准坐标（不是任何向量的时间导数）|
| 旋转矩阵 | $2\times 2$，1 个独立元 | $3\times 3$ 正交，3 个独立元 |
| 虚旋转 | 标量 $\delta\phi$ | 3×1 向量 $\delta\boldsymbol{\pi}$（仍是向量！）|

**核心结论**：有限旋转不是向量，但**无穷小旋转（虚旋转）和角速度是向量**——这一区分让线性代数仍可处理刚体姿态的微分关系。

### 2. Tilde 算子把叉积转化为线性代数

| 编号 | 公式 | 含义 |
|------|------|------|
| 9.1.21 | $\tilde{\mathbf{a}}=\begin{bmatrix}0&-a_z&a_y\\a_z&0&-a_x\\-a_y&a_x&0\end{bmatrix}$ | 反对称矩阵定义 |
| 9.1.22 | $\mathbf{c}=\tilde{\mathbf{a}}\mathbf{b}$ | 叉积矩阵化 |
| 9.1.23 | $\tilde{\mathbf{a}}^T=-\tilde{\mathbf{a}}$ | 反对称性 |
| 9.1.25 | $\tilde{\mathbf{a}}\mathbf{b}=-\tilde{\mathbf{b}}\mathbf{a}$ | 反交换 |
| 9.1.26 | $\tilde{\mathbf{a}}\mathbf{a}=\mathbf{0}$ | 自身叉积为 0 |
| 9.1.28 | $\tilde{\mathbf{a}}\tilde{\mathbf{b}}=\mathbf{b}\mathbf{a}^T-(\mathbf{a}^T\mathbf{b})\mathbf{I}$ | 双 tilde 展开 |
| 9.2.20 | $\tilde{\mathbf{s}}\mathbf{A}=\mathbf{A}\tilde{\mathbf{s}}'$ | tilde-A 交换律 |
| 9.2.21 | $(\mathbf{A}\mathbf{s}')^\sim=\mathbf{A}\tilde{\mathbf{s}}'\mathbf{A}^T$ | tilde 在变换下的形式 |

> **意义**：所有"叉积/反对称"操作都被吸收进矩阵代数，使运动学方程可以用线性求解器（LU/N-R）解出来——这是 DADS 等通用程序得以实现的基础。

### 3. 角速度的两种表示与 Ȧ 恒等式

- **全局系角速度**：$\tilde{\boldsymbol{\omega}}=\dot{\mathbf{A}}\mathbf{A}^T$（Eq. 9.2.36），$\dot{\mathbf{A}}=\tilde{\boldsymbol{\omega}}\mathbf{A}$（Eq. 9.2.39）
- **体固定系角速度**：$\boldsymbol{\omega}'=\mathbf{A}^T\boldsymbol{\omega}$，$\dot{\mathbf{A}}=\mathbf{A}\tilde{\boldsymbol{\omega}}'$（Eq. 9.2.40）

两表示等价但**取值不同**；动力学中习惯用 $\boldsymbol{\omega}'$（因为惯性张量 J' 在体固定系中为常量）。

### 4. Euler 参数：无奇异姿态广义坐标

**完整链条**：

\[
\text{姿态 }\mathbf{A} \;\Longleftrightarrow\;\mathbf{p}=[e_0;\mathbf{e}]\text{ s.t. }\mathbf{p}^T\mathbf{p}=1
\]

| 关键公式 | 编号 | 含义 |
|----------|------|------|
| $\mathbf{A}=(2e_0^2-1)\mathbf{I}+2(\mathbf{e}\mathbf{e}^T+e_0\tilde{\mathbf{e}})$ | 9.3.6 | A 的紧凑表达 |
| $\mathbf{A}=\mathbf{E}\mathbf{G}^T$ | 9.3.26 | A 的因子分解 |
| $\boldsymbol{\omega}'=2\mathbf{G}\dot{\mathbf{p}}$ | 9.3.34 | 体固定系角速度 |
| $\boldsymbol{\omega}=2\mathbf{E}\dot{\mathbf{p}}$ | 9.3.36 | 全局系角速度 |
| $\dot{\mathbf{p}}=\tfrac12\mathbf{G}^T\boldsymbol{\omega}'$ | 9.3.35 | 反向关系 |
| $\delta\boldsymbol{\pi}'=2\mathbf{G}\,\delta\mathbf{p}$ | 9.3.41 | 体固定虚旋转 |

**Euler 参数 vs Euler 角**：

| 维度 | Euler 角（3-2-1 等）| Euler 参数（四元数）|
|------|---------------------|--------------------|
| 参数数 | 3 | 4（含 1 约束）|
| 奇异 | 万向锁（云台死锁）| **无奇异** |
| 双值 | 单值 | $\mathbf{p}^+, \mathbf{p}^-=-\mathbf{p}^+$ 描述同一姿态 |
| 微分方程 | 含 sec/cot 之类奇异项 | **代数关系，全光滑** |

### 5. 角速度是准坐标——不可积性

§9.3 末尾给出严格证明（Eq. 9.3.45）：把 $\delta\pi'_x$ 展开为 $\delta\mathbf{p}$ 的线性组合，验证精确微分的 Schwarz 条件 $\partial f_1/\partial x_2 = \partial f_2/\partial x_1$ **不成立**。结论：**不存在"角度向量" $\boldsymbol{\Theta}'$ 使 $\dot{\boldsymbol{\Theta}}'=\boldsymbol{\omega}'$**。这意味着：

- 不能把 $\boldsymbol{\omega}'$ 直接积出 "角度位移"；
- 必须用 $\dot{\mathbf{p}}=\tfrac12\mathbf{G}^T\boldsymbol{\omega}'$ 桥接姿态变量与角速度；
- 动力学方程中"广义动量 = 惯性 × 角速度"是非完整的。

### 6. 运动副约束库的搭积木结构

把所有约束分为三层：

```
  level 0 (基元):  Φ^d1   Φ^d2   Φ^s   球-球距离
                    ↓      ↓      ↓
  level 1 (复合):  Φ^p1=2×Φ^d1   Φ^p2=2×Φ^d2
                    ↓      ↓
  level 2 (运动副): 球副 / 万向节 / 转动副 / 柱铰 / 平移副 / 螺旋副
                    ↓
  level 3 (复合关节): 球-球 / 转-球 / 转-转(平行/正交相交) / 转-柱 / 转-平移 / 支柱
                    ↓
  level 4 (驱动):   绝对驱动 / 距离驱动 / 平移驱动 / 转动驱动
```

**6 类基本运动副约束方程数与 DOF**（每个运动副 6 = 方程数 + DOF）：

| 运动副 | 方程数 | 相对 DOF | 主成分 | 公式 |
|--------|--------|----------|--------|------|
| 球副 | 3 | 3 | $\Phi^s$ | 9.4.16 |
| 万向节 | 4 | 2 | $\Phi^s + \Phi^{d1}(\mathbf{h}_i,\mathbf{h}_j)$ | 9.4.19 |
| 转动副 | 5 | 1 | $\Phi^s + \Phi^{p1}$ | 9.4.22 |
| 柱铰 | 4 | 2 | $\Phi^{p1} + \Phi^{p2}$ | 9.4.23 |
| 平移副 | 5 | 1 | $\Phi^{p1} + \Phi^{p2} + \Phi^{d1}(\mathbf{f}_i,\mathbf{f}_j)$ | 9.4.24 |
| 螺旋副 | 5 | 1 | 柱铰 + $\Phi^{scr}$ | 9.4.26 |

**7 类复合关节**（隐去 coupler 的等价约束）：

| 复合关节 | 公式 | 方程数 | DOF |
|----------|------|--------|-----|
| 球-球 | 9.4.28 | 1 | 5 |
| 转-球 | 9.4.29 | 2 | 4 |
| 平行轴 转-转 | 9.4.30 | 4 | 2 |
| 正交相交 转-转 | 9.4.31 | 4 | 2 |
| 转-柱 | 9.4.32 | 2 | 3 |
| 转-平移 | 9.4.33 | 4 | 2 |
| 支柱 | 9.4.34 | 2 | 4 |

### 7. 万向节奇异——空间运动学的典型病理

当万向节两叉夹角 $\varphi=\pi/2$ 时（Fig. 9.4.15），dot-1 变分方程退化为：

\[
\tan\theta_1\,\delta\theta_2 = (2/\tan\theta_2)\,\delta\theta_1,\qquad \tan\theta_1=0
\]

意味着**任意 $\delta\theta_2$ 必有 $\delta\theta_1=0$**——驱动轴锁死，主动转动无法传递到从动轴。工程含义：

- 必须在装配时让两叉夹角 $\varphi$ 远离 $\pi/2$；
- 高速汽车传动轴用**双万向节（CV joint）**串联两个等角万向节，相互抵消角度误差。

### 8. 求解三段方程：位置/速度/加速度的层次结构

**位置（Eq. 9.6.5–9.6.11）**：

\[
\Phi(\mathbf{q},t)=\begin{bmatrix}\Phi^K(\mathbf{q})\\ \Phi^D(\mathbf{q},t)\\ \Phi^P(\mathbf{q})\end{bmatrix}=\mathbf{0}\quad(7nb\text{ 方程})\;\Longrightarrow\;\text{Newton-Raphson}
\]

**速度（Eq. 9.6.12）**——切换到 $\boldsymbol{\omega}'$ 坐标：

\[
\sum_i\bigl\{[\Phi^K_{r_i};\,\Phi^D_{r_i}]\,\dot{\mathbf{r}}_i + [\Phi^K_{\pi'_i};\,\Phi^D_{\pi'_i}]\,\boldsymbol{\omega}'_i\bigr\}=[\boldsymbol{\nu}^K;\,\boldsymbol{\nu}^D]
\]

> **关键**：用 $\boldsymbol{\omega}'$ 而非 $\dot{\mathbf{p}}$ 做速度变量后，Euler 归一化的速度方程（Eq. 9.6.9）$\mathbf{p}^T\mathbf{G}^T=\mathbf{0}$ 恒满足，可省去；方程数从 7nb 降到 6nb。

**加速度（Eq. 9.6.19）**——同一系数矩阵，仅换右端：

\[
[\text{velocity coef. matrix}]\,[\ddot{\mathbf{r}}_i;\,\dot{\boldsymbol{\omega}}'_i]=[\boldsymbol{\gamma}^K;\,\boldsymbol{\gamma}^D]
\]

> **效率要点**：速度方程的 LU 分解可被加速度方程**复用**。这是 DADS 等商业软件的核心优化。

**双重非奇异要求**：位置 Jacobian $\Phi_\mathbf{q}$（7nb×7nb）与速度系数矩阵（6nb×6nb）**结构不同**，必须分别保证非奇异——前者奇异 → 装配死点；后者奇异 → 瞬时机构锁死（如万向节 $\varphi=\pi/2$）。

---

## 工程应用与实例

| 例题号 | 名称 | 类型 | 应用 | 关键知识点 |
|--------|------|------|------|-----------|
| 9.1.6 | 三点确定笛卡尔系 | 几何重建 | CAD 装配/视觉跟踪 | $\mathbf{f}=\Delta\mathbf{r}^{PQ}/|\cdot|$, $\mathbf{h}=\tilde{\mathbf{f}}\Delta\mathbf{r}^{PR}/|\cdot|$, $\mathbf{g}=\tilde{\mathbf{h}}\mathbf{f}$ |
| 9.1.7 / 9.1.9 | 匀速圆周运动 | 教学示例 | 旋转机械 | $\ddot{\mathbf{r}}=-\omega^2\mathbf{r}$（向心加速度），$\dot{\mathbf{a}}^T\mathbf{a}=0$ |
| 9.2.2 | 绕 z 轴简单旋转 | 退化校验 | 平面/空间一致性 | 空间方法降维至平面（Ch.2 旋转矩阵）|
| 9.2.4 / 9.2.5 | 绕 z 旋转的 ω 与点 P 速度 | 教学示例 | $\tilde{\boldsymbol{\omega}}=\dot{\mathbf{A}}\mathbf{A}^T$ 验证 | 速度/加速度方程的简单验证 |
| 9.3.1 | 绕 $\mathbf{u}=[1,1,1]^T/\sqrt{3}$ 旋转 | 几何示例 | 任意轴旋转 | Euler 参数 $\mathbf{e}=[1,1,1]^T\sin(\varphi/2)/\sqrt{3}$，A 矩阵推导 |
| 9.4.7 | 万向节运动学 | 经典机构 | 汽车传动轴 | $\theta_2=\arctan(\tan\theta_1/\cos\varphi)$，$\varphi=\pi/2$ 锁死 |
| 9.4.8 | 转动副约束验证 | 校验例题 | 任意 $\theta$ | $\Phi^s\equiv 0$, $\Phi^{p1}\equiv 0$ 恒成立 |
| 9.4.9 | 柱铰约束验证 | 校验例题 | 任意 $\theta, s$ | 柱铰允许 2 DOF |
| 9.4.10 | 平移副约束验证 | 校验例题 | 任意 $s$ | 5 个约束方程逐项验证 |
| 9.4.11 | 螺旋副约束验证 | 校验例题 | $s=\alpha(\theta+2n\pi-\theta_0)$ | 螺距耦合的代数验证 |
| 9.4.12 | 滑块-曲柄机构（3 种 coupler）| 综合应用 | 内燃机 | 球-球/转-球/平行轴转-转 三种等价建模均给 DOF=14−13=1 |

---

## 与全书的关系

| 本章概念 | 后续展开位置 |
|----------|-------------|
| Tilde 算子 $\tilde{\mathbf{a}}$ | 全书空间章节通用；Ch.10 出现在惯性力 $\tilde{\boldsymbol{\omega}}'\mathbf{J}'\boldsymbol{\omega}'$ |
| 方向余弦矩阵 $\mathbf{A}$ | Ch.10 用于把体固定系惯性张量变换到全局系；Ch.11 空间动力学建模 |
| 角速度 $\boldsymbol{\omega}'$ | Ch.10 牛顿-欧拉方程 $\mathbf{J}'\dot{\boldsymbol{\omega}}'+\tilde{\boldsymbol{\omega}}'\mathbf{J}'\boldsymbol{\omega}'=\boldsymbol{n}'$ |
| Euler 参数 $\mathbf{p}$ | Ch.10 作为姿态广义坐标；动力学方程通过 $\mathbf{G}$ 矩阵把 $\boldsymbol{\omega}'$ 与 $\dot{\mathbf{p}}$ 衔接 |
| Euler 归一化约束 $\mathbf{p}^T\mathbf{p}=1$ | Ch.7 数值积分中作为隐式约束（漂移修正、Baumgarte 稳定）|
| 6 类基本运动副 + 7 类复合关节 | Ch.11 空间多体建模的"积木"；与 Ch.5（平面建模）形成对照 |
| 4 类驱动约束 | Ch.10–11 逆动力学（运动学确定系统）的输入；与 Ch.6 平面驱动一致 |
| 位置/速度/加速度三段方程 | Ch.10 动力学方程与之联立形成 DAE；Ch.7 的数值方法直接套用 |
| 万向节奇异、装配死点 | Ch.11 空间案例研究中再次出现，方法论与 Ch.5 平面奇异分析一致 |

**承上启下定位**：本章是 Part Two（空间）的"运动学骨架"，与 Part One 中 Ch.3 的关系完全对应——Ch.3:Ch.6 = Ch.9:Ch.10。掌握本章后，再加上 Ch.6/7 通用的动力学拉格朗日乘子框架，即可在 Ch.10–11 直接组装空间多体动力学方程。
