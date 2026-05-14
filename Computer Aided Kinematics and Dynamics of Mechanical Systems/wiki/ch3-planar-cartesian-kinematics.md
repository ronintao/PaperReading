---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 3
title: "Planar Cartesian Kinematics"
pages: 48-117
sections:
  - "3.1 Kinematics of a Body"
  - "3.2 Absolute Constraints"
  - "3.3 Relative Constraints"
  - "3.4 Gears, Cam-Followers, and Point-Followers"
  - "3.5 Driving Constraints"
  - "3.6 Position, Velocity, and Acceleration Analysis"
  - "3.7 Singular Configurations"
created: 2026-05-14
last_updated: 2026-05-14
---

# Chapter 3: Planar Cartesian Kinematics

## 章节定位

第3章是全书的**核心方法论章节**（pp.48-117），建立平面笛卡尔运动学的完整框架。以笛卡尔广义坐标 $\mathbf{q}_i = [x_i, y_i, \phi_i]^T$ 为基础，系统化地构建所有平面运动副（铰链、移动副、齿轮、凸轮）的约束方程及其 Jacobian，定义驱动约束使系统运动完全确定，然后给出位置（Newton-Raphson）、速度、加速度分析的统一求解流程。最后讨论奇异构型（lock-up 和 bifurcation）。本章是第4章（计算方法实现）和第5-7章（动力学）的直接前置，其约束方程和 Jacobian 构造方法贯穿全书。前置知识为第2章的向量矩阵代数和矩阵微积分记号。

---

## 概念定义

**Rigid Body（刚体）** [p.48]
> A rigid body that is used to model a component of a mechanism is defined as a system of particles the distances between which remain unchanged. Each particle in a rigid body is located by its constant position vector in a reference frame that is attached to and moves with the body, called the body-fixed reference frame.
>
> 刚体是用于建模机构部件的粒子系统，粒子间距离保持不变。刚体中每个粒子由其在随体参考系中的常位置向量确定。

---

**Body-Fixed Reference Frame（随体参考系）** [p.48]
> A reference frame that is attached to and moves with the body.
>
> 固定于刚体上并随之运动的参考系。

---

**Mechanism（机构）** [p.49]
> A mechanism is a collection of rigid bodies that are arranged to allow relative motion.
>
> 机构是一组刚体的集合，其排列方式允许相对运动。

---

**Kinematics（运动学）** [p.49]
> Kinematics is the study of the position, velocity, and acceleration of a system of interconnected bodies that make up a mechanism, independent of the forces that produce the motion.
>
> 运动学是研究组成机构的互连刚体系统的位置、速度和加速度，与产生运动的力无关。

---

**Kinematic Synthesis（运动综合）** [p.49]
> Kinematic synthesis is the process of finding the geometry of a mechanism that will yield desired motion characteristics.
>
> 运动综合是寻找能产生所需运动特性的机构几何形状的过程。

---

**Kinematic Analysis（运动分析）** [p.49]
> Kinematic analysis is the process of predicting position, velocity, and acceleration, once a design is specified.
>
> 运动分析是在给定设计后预测位置、速度和加速度的过程。

---

**Generalized Coordinates（广义坐标）** [p.49]
> Any set of variables that uniquely specifies the position and orientation of all bodies in a mechanism, that is, the configuration of the mechanism, is called a set of generalized coordinates. Generalized coordinates may be independent or dependent.
>
> 唯一确定机构中所有刚体位置和方向的任意变量集合。广义坐标可以是独立的或从属的（需满足约束方程）。

---

**Cartesian Generalized Coordinates（笛卡尔广义坐标）** [p.49]
> The column vector $\mathbf{q}_i \equiv [x, y, \phi]_i^T$ is the vector of planar Cartesian generalized coordinates for body $i$. Using Cartesian generalized coordinates for each body, a maximal set of coordinates is defined.
>
> 列向量 $\mathbf{q}_i = [x_i, y_i, \phi_i]^T$ 是刚体 $i$ 的平面笛卡尔广义坐标向量。对每个刚体使用笛卡尔广义坐标，定义了极大坐标集。

---

**Holonomic Kinematic Constraint Equations（完整运动约束方程）** [p.50]
> When conditions on relative motion between a pair of bodies are expressed as algebraic equations in terms of generalized coordinates, they are called holonomic kinematic constraint equations.
>
> 当一对刚体间的相对运动条件被表达为广义坐标的代数方程时，称为完整运动约束方程。

---

**Stationary Constraint（定常约束）** [p.50]
> If $t$ does not enter explicitly into the equation of constraint, the constraint is called a stationary constraint.
>
> 若时间 $t$ 不显式出现在约束方程中，该约束称为定常约束。

---

**Nonholonomic Constraints（非完整约束）** [p.50]
> More general constraint equations that contain inequalities or relations between velocity components are called nonholonomic constraints.
>
> 包含不等式或速度分量间关系的更一般约束方程称为非完整约束。

**备注**：本书中"约束"默认指完整约束。

---

**Degrees of Freedom / DOF（自由度）** [p.51]
> If the constraints of Eq. 3.1.1 or 3.1.2 are consistent and independent, then the system is said to have $nc - nh$ degrees of freedom, abbreviated DOF $= nc - nh$.
>
> 若约束方程一致且独立，则系统具有 $nc - nh$ 个自由度。

---

**Driving Constraints（驱动约束）** [p.51]
> If DOF independent driving constraints are specified for kinematic analysis, denoted $\Phi^D(\mathbf{q}, t) = \mathbf{0}$, then the configuration of the system as a function of time can be determined.
>
> 为运动分析指定的 DOF 个独立驱动约束，使系统构型可作为时间的函数确定。

---

**Velocity Equation（速度方程）** [p.52]
> Differentiating both sides of the constraint equation with respect to time yields the velocity equation: $\Phi_\mathbf{q}\dot{\mathbf{q}} = -\Phi_t \equiv \boldsymbol{\nu}$.
>
> 对约束方程关于时间求导得到速度方程。

---

**Acceleration Equation（加速度方程）** [p.53]
> Differentiating the velocity equation with respect to time yields the acceleration equation: $\Phi_\mathbf{q}\ddot{\mathbf{q}} = -(\Phi_\mathbf{q}\dot{\mathbf{q}})_\mathbf{q}\dot{\mathbf{q}} - 2\Phi_{\mathbf{q}t}\dot{\mathbf{q}} - \Phi_{tt} \equiv \boldsymbol{\gamma}$.
>
> 对速度方程关于时间求导得到加速度方程。

---

**Jacobian Matrix（雅可比矩阵）** [p.53]
> The matrix $\Phi_\mathbf{q}$ that arises in the velocity and acceleration equations plays a central role in the theory and numerical methods of kinematics and dynamics. It is called the Jacobian matrix. It is the most important matrix that is used in the kinematics and dynamics of constrained mechanical systems.
>
> 出现在速度方程和加速度方程中的矩阵 $\Phi_\mathbf{q}$，在运动学和动力学中起核心作用。称为雅可比矩阵，是约束机械系统中最重要的矩阵。

---

**Absolute Distance Constraint（绝对距离约束）** [p.57]
> The absolute distance constraint defines the physical limitation that point $P_i$ on body $i$ can only move on a circular path, due to a link of fixed length with revolute joints.
>
> 绝对距离约束限定刚体 $i$ 上点 $P_i$ 只能在固定半径圆弧上运动。

**条件**：$C_3 > 0$（若 $C_3 = 0$，退化且雅可比为零）。

---

**Absolute Position Constraint（绝对位置约束）** [p.59]
> An absolute position constraint on point $P_i$ of body $i$ in the $x$ or $y$ direction might be imagined as the condition that a pin on body $i$ at point $P_i$ slide in a slot parallel to the $x$ or $y$ axis.
>
> 绝对位置约束可想象为刚体 $i$ 上点 $P_i$ 处的销钉在平行于 $x$ 或 $y$ 轴的槽中滑动。

---

**Revolute Joint（转动副/铰链）** [p.65]
> A revolute joint allows relative rotation about a point $P$ that is common to bodies $i$ and $j$. A revolute joint eliminates two degrees of freedom from the pair.
>
> 转动副允许两刚体绕共有点 $P$ 相对转动。消除2个自由度。

---

**Translational Joint（移动副/滑动副）** [p.66]
> A translational joint allows relative translation of a pair of bodies along a common axis, but no relative rotation. A translational joint eliminates two degrees of freedom from the pair.
>
> 移动副允许两刚体沿公共轴线相对平移，但不允许相对转动。消除2个自由度。

---

**Composite Joint（复合副）** [p.69]
> The resulting combination of revolute and translational joints via a coupler may be viewed as a composite joint, yielding elementary constraint equations and avoiding the need to introduce additional generalized coordinates for the coupler.
>
> 通过连杆组合转动副和移动副可视为复合副，产生简单约束方程，避免引入连杆的额外广义坐标。

---

**Revolute-Revolute Composite Joint（转动-转动复合副）** [p.69]
> A pair of rigid bodies connected by a coupler with two revolute joints. Only one constraint equation is required: $\Phi^{rr(i,j)} = \mathbf{d}_{ij}^T\mathbf{d}_{ij} - C^2 = 0$.
>
> 通过带两个转动副的连杆连接的一对刚体。仅需一个距离约束方程。

---

**Revolute-Translational Composite Joint（转动-移动复合副）** [p.70]
> Bodies $i$ and $j$ connected by a coupler, with a revolute joint on body $j$ and a translational joint on body $i$. Eliminates only one degree of freedom.
>
> 刚体 $i$ 和 $j$ 通过连杆连接（$j$ 上为转动副，$i$ 上为移动副）。仅消除一个自由度。

---

**Convex-Convex Gear Set（外啮合齿轮组）** [p.71]
> A convex-convex gear set consists of a pair of gears on two bodies constrained so that the distance $R_i + R_j$ between their centers is fixed. Gear teeth cause the pitch circles to roll relative to each other, without slip.
>
> 外啮合齿轮组由两体上的齿轮组成，中心距固定为 $R_i + R_j$。齿轮齿使节圆无滑动滚动。

---

**Rack and Pinion（齿条与小齿轮）** [p.76]
> If the radius of the gear on body $i$ becomes infinite, a straight gear profile called a rack results. The gear on body $j$ is then called a pinion.
>
> 若刚体 $i$ 上齿轮半径变为无穷大，得到齿条。刚体 $j$ 上的齿轮称为小齿轮。

**关键关系**：齿条与小齿轮是 revolute-translational composite joint 的特例。

---

**Cam-Follower Pair（凸轮-从动件副）** [p.79]
> Body $i$ is the cam and body $j$ is the follower. The two bodies are in contact at point $P$, but sliding is permitted. It is assumed that the cam and its follower always remain in contact and that the contact surfaces are either convex shapes or flat.
>
> 刚体 $i$ 为凸轮，刚体 $j$ 为从动件。两体在点 $P$ 处接触但允许滑动。假定始终保持接触且轮廓为凸形或平面。

---

**Point-Follower Joint（点从动件副）** [p.85]
> Pin $P$ is attached to body $i$ and can slide and rotate in a slot on body $j$. The coordinates of any point on the slot are described by $\mathbf{a}_j = \mathbf{A}_j\rho_j(\alpha_j)\mathbf{u}_j'(\alpha_j)$.
>
> 销钉 $P$ 固定在刚体 $i$ 上，可在刚体 $j$ 上的槽中滑动和转动。

---

**Driving Constraint（驱动约束）** [p.86]
> The motion of many mechanical systems is described by actuator input that specifies the time history of some position coordinates or the relative position of pairs of bodies. To uniquely determine the time history of motion, a number of inputs must be specified, equal in number to the degrees of freedom.
>
> 许多机械系统的运动由执行器输入描述。为唯一确定运动时间历程，需指定等于自由度数的输入数。

---

**Absolute Driver（绝对驱动约束）** [p.87]
> Time-dependent absolute coordinate constraints, called drivers, may be imposed. Allowing the parameters $C_1$, $C_2$, and $C_3$ to be time dependent yields absolute coordinate drivers.
>
> 将绝对约束的参数设为时间函数，即得绝对坐标驱动。

---

**Relative Driver（相对驱动约束）** [p.90]
> Constraints between coordinates of points on pairs of bodies can be specified as functions of time, in the form of relative coordinate drivers.
>
> 体对上点坐标间的约束可指定为时间函数，形成相对坐标驱动。

---

**Revolute-Rotational Driver（转动副-转角驱动）** [p.93]
> An electrical or hydraulic actuator that controls the relative angular orientation of a pair of bodies at a revolute joint. The attachment angles $\theta_i$ and $\theta_j$ are defined by the physical mounting.
>
> 控制铰链处两体相对角度的电动或液压执行器。安装角由物理安装确定。

---

**Translational-Distance Driver（平移距离驱动）** [p.94]
> The relative translation of a pair of bodies along a translational joint, encountered in robots and numerically controlled machine tools.
>
> 一对刚体沿移动副的相对平移，常用于机器人和数控机床。

---

**Position Analysis（位置分析）** [p.98]
> The objective of position analysis is to solve the system of constraint equations for $\mathbf{q}$ as a function of time. Since these equations are highly nonlinear, finding an analytical solution is generally impossible.
>
> 位置分析的目标是将约束方程组求解为 $\mathbf{q}$ 关于时间的函数。由于方程高度非线性，通常不可能找到解析解。

---

**Implicit Function Theorem（隐函数定理）** [p.100]
> If $\mathbf{q}^0$ is a solution at $t = t_0$, $\Phi$ is twice continuously differentiable, and the Jacobian is nonsingular at $(\mathbf{q}^0, t_0)$, then there exists a unique solution $\mathbf{q} = \mathbf{f}(t)$ in some interval about $t_0$.
>
> 若 $\mathbf{q}^0$ 在 $t_0$ 时为解，$\Phi$ 二次连续可微，且 Jacobian 非奇异，则在 $t_0$ 附近存在唯一解。

---

**Newton-Raphson Method（牛顿-拉夫森方法）** [p.100]
> An iterative technique: $\Phi_\mathbf{q}(\mathbf{q}^{(k)}, t)\Delta\mathbf{q}^{(k)} = -\Phi(\mathbf{q}^{(k)}, t)$, then $\mathbf{q}^{(k+1)} = \mathbf{q}^{(k)} + \Delta\mathbf{q}^{(k)}$. It is quadratically convergent.
>
> 迭代技术：求解修正量后更新估计。具有二次收敛性。

---

**Lock-up Configuration（锁死构型）** [p.105]
> A configuration in which the crank can no longer be driven. Characterized by $\dot{\mathbf{q}} \to \infty$ and $\ddot{\mathbf{q}} \to \infty$.
>
> 曲柄无法继续驱动的构型。特征为速度和加速度趋于无穷大。

---

**Bifurcation（分岔）** [p.105]
> Branching of motion to two possible paths. Two possible motions can occur from the same configuration.
>
> 运动分支到两条可能路径的现象。从同一构型可产生两种运动。

---

**Consistent Redundancy（一致冗余）** [p.99]
> A redundant constraint that is automatically satisfied if the remaining constraints are satisfied.
>
> 在其余约束满足时自动满足的冗余约束。

---

**Inconsistent Redundancy（不一致冗余）** [p.99]
> A redundant constraint such that $\Phi = \mathbf{0}$ cannot be satisfied for any value of $\mathbf{q}$.
>
> 对任何 $\mathbf{q}$ 值都无法满足的冗余约束。

---

**Virtual Displacement（虚位移）** [p.109]
> A small displacement $\delta\mathbf{q}$ that satisfies constraints to first order with time held fixed: $\Phi_\mathbf{q}\delta\mathbf{q} = \mathbf{0}$.
>
> 时间固定条件下满足约束一阶近似的小位移。

---

## 符号定义

### §3.1 基本运动学

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{q}_i = [x_i, y_i, \phi_i]^T$ | 向量 (3×1) | 刚体 $i$ 的平面笛卡尔广义坐标 |
| $\mathbf{r}_i = [x_i, y_i]^T$ | 向量 (2×1) | 刚体 $i$ 随体坐标系原点在全局系中的位置 |
| $\phi_i$ | 标量，角度 | 刚体 $i$ 随体坐标系相对全局系的转角 |
| $\mathbf{q} = [\mathbf{q}_1^T, \ldots, \mathbf{q}_{nb}^T]^T$ | 向量 ($nc \times 1$) | 系统广义坐标向量 |
| $nb$ | 标量，整数 | 系统中刚体数量 |
| $nc = 3nb$ | 标量，整数 | 笛卡尔广义坐标总数 |
| $nh$ | 标量，整数 | 完整约束方程数量 |
| $\mathbf{A}_i$ | 矩阵 (2×2) | 刚体 $i$ 的旋转矩阵，$[\cos\phi_i, -\sin\phi_i; \sin\phi_i, \cos\phi_i]$ |
| $\mathbf{B}_i = \partial\mathbf{A}_i/\partial\phi_i$ | 矩阵 (2×2) | $\mathbf{A}_i$ 对 $\phi_i$ 的导数，$[-\sin\phi_i, -\cos\phi_i; \cos\phi_i, -\sin\phi_i]$ |
| $\mathbf{s}_i'^P = [x_i'^P, y_i'^P]^T$ | 向量 (2×1) | 点 $P$ 在刚体 $i$ 随体系中的常坐标向量 |
| $\mathbf{r}_i^P = \mathbf{r}_i + \mathbf{A}_i\mathbf{s}_i'^P$ | 向量 (2×1) | 点 $P$ 在全局坐标系中的位置 |
| $\Phi^K(\mathbf{q})$ | 向量函数 ($nh \times 1$) | 运动学约束方程 |
| $\Phi^D(\mathbf{q}, t)$ | 向量函数 ($DOF \times 1$) | 驱动约束方程 |
| $\Phi(\mathbf{q}, t)$ | 向量函数 ($nc \times 1$) | 组合约束方程 |
| $\Phi_\mathbf{q}$ | 矩阵 ($nc \times nc$) | 约束 Jacobian（方阵） |
| $\boldsymbol{\nu} = -\Phi_t$ | 向量 | 速度方程右端项 |
| $\boldsymbol{\gamma}$ | 向量 | 加速度方程右端项 |

### §3.2-3.3 绝对与相对约束

| 符号 | 类型 | 含义 |
|------|------|------|
| $\Phi^{ad(i)}$, $\Phi^{ax(i)}$, $\Phi^{ay(i)}$, $\Phi^{a\phi(i)}$ | 标量函数 | 绝对距离/x/y/角度约束 |
| $\Phi^{rx(i,j)}$, $\Phi^{ry(i,j)}$, $\Phi^{r\phi(i,j)}$, $\Phi^{rd(i,j)}$ | 标量函数 | 相对 x/y/角度/距离约束 |
| $C_1, C_2, C_3, C_4$ | 标量，常数 | 约束中的给定常数 |
| $\mathbf{d}_{ij} = \mathbf{r}_j + \mathbf{s}_j^P - \mathbf{r}_i - \mathbf{s}_i^P$ | 向量 (2×1) | 体 $i$ 上 $P_i$ 到体 $j$ 上 $P_j$ 的连接向量 |

### §3.3.2 转动副与移动副

| 符号 | 类型 | 含义 |
|------|------|------|
| $\Phi^{r(i,j)}$ | 向量函数 (2×1) | 转动副约束方程 |
| $\Phi^{t(i,j)}$ | 向量函数 (2×1) | 移动副约束方程 |
| $\mathbf{v}_i = \mathbf{A}_i\mathbf{v}_i'$ | 向量 (2×1) | 体 $i$ 上平移方向向量（全局系） |
| $\mathbf{v}_i^\perp = \frac{1}{v_i}\mathbf{A}_i\mathbf{R}\mathbf{v}_i'$ | 向量 (2×1) | 垂直于平移方向的单位向量 |
| $\mathbf{R} = [0, -1; 1, 0]$ | 矩阵 (2×2) | 90°逆时针旋转矩阵 |
| $\mathbf{A}_{ij} = \mathbf{A}_i^T\mathbf{A}_j$ | 矩阵 (2×2) | 体 $j$ 相对体 $i$ 的旋转矩阵 |
| $\mathbf{B}_{ij} = \mathbf{B}_i^T\mathbf{A}_j = \mathbf{R}^T\mathbf{A}_{ij}$ | 矩阵 (2×2) | 辅助矩阵 |

### §3.3.3 复合副

| 符号 | 类型 | 含义 |
|------|------|------|
| $\Phi^{rr(i,j)}$ | 标量函数 | 转动-转动复合副约束（距离约束特例） |
| $\Phi^{rt(i,j)}$ | 标量函数 | 转动-移动复合副约束 |

### §3.4 齿轮与凸轮

| 符号 | 类型 | 含义 |
|------|------|------|
| $R_i, R_j$ | 标量，长度 | 齿轮 $i$、$j$ 的节圆半径 |
| $\Phi^{g(i,j)}$ | 标量函数 | 齿轮约束方程 |
| $\Phi^{rp(i,j)}$ | 向量函数 (2×1) | 齿条-小齿轮约束方程 |
| $\rho(\alpha)$ | 标量函数 | 凸轮轮廓极坐标径向距离 |
| $\alpha, \alpha_i, \alpha_j$ | 标量/广义坐标 | 轮廓参数角（附加广义坐标） |
| $\mathbf{g}' = d\mathbf{a}'/d\alpha$ | 向量 (2×1) | 轮廓曲线切向量（随体系） |
| $\Phi^{cf(i,j)}$ | 向量函数 (3×1) | 凸轮-从动件约束（3个方程） |
| $\Phi^{cff(i,j)}$ | 向量函数 (2×1) | 凸轮-平面从动件约束（2个方程） |
| $\Phi^{pf(i,j)}$ | 向量函数 (2×1) | 点从动件约束 |

### §3.5 驱动约束

| 符号 | 类型 | 含义 |
|------|------|------|
| $C_1(t), C_2(t), C_3(t)$ | 标量函数 | 绝对驱动的时间函数 |
| $C_4(t)$ | 标量函数，$>0$ | 相对距离驱动时间函数 |
| $C(t)$ | 标量函数 | 转角/平移距离驱动时间函数 |
| $\Phi^{axd(i)}$, $\Phi^{ayd(i)}$, $\Phi^{a\phi d(i)}$ | 标量约束 | 绝对 x/y/角度驱动 |
| $\Phi^{rxd(i,j)}$, $\Phi^{ryd(i,j)}$, $\Phi^{r\phi d(i,j)}$ | 标量约束 | 相对 x/y/角度驱动 |
| $\Phi^{rdd(i,j)}$, $\Phi^{rrd(i,j)}$, $\Phi^{tdd(i,j)}$ | 标量约束 | 相对距离/转角/平移距离驱动 |
| $\nu^d = \dot{C}(t)$ | 标量 | 驱动约束速度方程右端项 |
| $\gamma^d = \gamma + \ddot{C}(t)$ | 标量 | 驱动约束加速度方程右端项 |

### §3.6-3.7 位置分析与奇异构型

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{q}^{(k)}, \Delta\mathbf{q}^{(k)}$ | 向量 | Newton-Raphson 第 $k$ 次迭代估计与修正量 |
| $\varepsilon$ | 标量 | 收敛容差 |
| $\Psi_0(\mathbf{q}, t_0, r)$ | 标量函数 | 装配最小化目标函数 |
| $t^*$, $\mathbf{q}^*$ | 标量/向量 | 奇异点时刻与对应构型 |
| $\boldsymbol{\beta}$ | 向量 | Jacobian 左零空间向量（$\Phi_\mathbf{q}^T\boldsymbol{\beta} = \mathbf{0}$） |
| $\delta\mathbf{q}$ | 向量 | 虚位移（$\Phi_\mathbf{q}\delta\mathbf{q} = \mathbf{0}$） |
| $\mathbf{b}$ | 向量 | 设计参数向量 |

---

## 核心论点

### §3.1 运动学三级分析框架

本节建立运动学分析的完整数学框架，形成三级递进结构：

1. **位置分析**：求解非线性代数方程 $\Phi(\mathbf{q}, t) = \mathbf{0}$（数值方法：Newton-Raphson，见 Ch.4）
2. **速度分析**：求解线性方程 $\Phi_\mathbf{q}\dot{\mathbf{q}} = \boldsymbol{\nu}$（Eq. 3.1.9）
3. **加速度分析**：求解线性方程 $\Phi_\mathbf{q}\ddot{\mathbf{q}} = \boldsymbol{\gamma}$（Eq. 3.1.10）

**关键洞察**：位置方程非线性，速度和加速度方程线性，共享同一个 Jacobian $\Phi_\mathbf{q}$。$|\Phi_\mathbf{q}| \neq 0$ 是整个分析可行的前提。

**约束方程必须蕴含铰的几何**（p.50）：如果约束仅"与几何一致"而不"蕴含几何"，数学模型无法正确描述物理系统（Example 3.1.3 演示此陷阱）。

---

### §3.2-3.3 约束库

**绝对约束**（体→地面）

| 类型 | 方程 | 约束数 | $\nu$ | $\gamma$ |
|------|------|--------|-------|---------|
| abs-dist | $(\mathbf{r}_i^P - \mathbf{C})^T(\mathbf{r}_i^P - \mathbf{C}) - C_3^2 = 0$ | 1 | 0 | $\neq 0$ |
| abs-x | $x_i^P - C_1 = 0$ | 1 | 0 | $(x_i'^P\cos\phi_i - y_i'^P\sin\phi_i)\dot\phi_i^2$ |
| abs-y | $y_i^P - C_2 = 0$ | 1 | 0 | $(x_i'^P\sin\phi_i + y_i'^P\cos\phi_i)\dot\phi_i^2$ |
| abs-$\phi$ | $\phi_i - C_3 = 0$ | 1 | 0 | 0 |

**相对约束**（体→体）

| 类型 | 约束数 | 消除DOF |
|------|--------|---------|
| 转动副 $\Phi^{r(i,j)}$ | 2 | 2 |
| 移动副 $\Phi^{t(i,j)}$ | 2 | 2 |
| 相对距离 $\Phi^{rd(i,j)}$ | 1 | 1 |
| RR复合副 $\Phi^{rr(i,j)}$ | 1 | 1 |
| RT复合副 $\Phi^{rt(i,j)}$ | 1 | 1 |

---

### §3.4 高副约束

**齿轮约束**

外啮合齿轮通过弧长等式 $\alpha_i R_i = \alpha_j R_j$ 推导，简化为投影方程：

$$\Phi^{g(i,j)} = (\mathbf{r}_j^P - \mathbf{r}_i^P)\mathbf{u}^\perp = 0$$

通过符号约定（$R_i = -\bar{R}_i < 0$），凹-凸齿轮组（内啮合）的方程形式与外啮合完全统一。

**凸轮/从动件约束对比**

| 约束类型 | 方程数 | 附加坐标 | 净消除DOF |
|---------|--------|---------|---------|
| Cam-Follower (convex-convex) | 3 | $\alpha_i, \alpha_j$ | 1 |
| Cam-Flat-Faced Follower | 2 | $\alpha_i$ | 1 |
| Point-Follower | 2 | $\alpha_j$ | 1 |

所有高副在平面情况下都仅消除 1 个自由度，允许 1 个相对滑动。

---

### §3.5 驱动约束

**驱动约束 vs 运动学约束的本质区别**：
- **运动学约束**：描述物理连接，不显式依赖时间 → $\nu = \mathbf{0}$
- **驱动约束**：描述执行器输入，显式依赖时间 → $\nu \neq \mathbf{0}$

驱动约束数 = DOF，两者结合使 $nh + DOF = nc$（方程数 = 未知数）。

**驱动约束的一般形式**：$\Phi^d(\mathbf{q}, t) = \Phi(\mathbf{q}) - \mathbf{C}(t) = \mathbf{0}$

右端项规律：$\nu^d = \dot{C}(t)$，$\gamma^d = \gamma^{kinematic} + \ddot{C}(t)$

---

### §3.6 位置、速度、加速度分析

**统一求解框架**

| 阶段 | 方程 | 性质 | 方法 |
|------|------|------|------|
| 位置 | $\Phi(\mathbf{q}, t) = \mathbf{0}$ | 非线性 | Newton-Raphson |
| 速度 | $\Phi_\mathbf{q}\dot{\mathbf{q}} = \boldsymbol{\nu}$ | 线性 | 直接解（Jacobian 已分解） |
| 加速度 | $\Phi_\mathbf{q}\ddot{\mathbf{q}} = \boldsymbol{\gamma}$ | 线性 | 直接解（同一 Jacobian） |

**Newton-Raphson**：$\Phi_\mathbf{q}\Delta\mathbf{q}^{(k)} = -\Phi(\mathbf{q}^{(k)}, t)$，$\mathbf{q}^{(k+1)} = \mathbf{q}^{(k)} + \Delta\mathbf{q}^{(k)}$。二次收敛。不收敛可能表示机构无法装配。

**时间网格**（§3.6.4）：利用 Taylor 展开提供下一时刻初始估计：$\mathbf{q}_{i+1} \approx \mathbf{q}_i + \Delta t\dot{\mathbf{q}}_i + \frac{1}{2}\Delta t^2\ddot{\mathbf{q}}_i$

---

### §3.7 奇异构型

**奇异判据**：$|\Phi_\mathbf{q}(\mathbf{q}^*, t^*)| = 0$

**两类奇异**

| 特征 | Lock-up | Bifurcation |
|------|---------|-------------|
| 速度方程 | 无有限解 | 有解但不唯一 |
| 替代定理 | $\exists\boldsymbol{\beta}: \boldsymbol{\beta}^T\Phi_t \neq 0$ | $\forall\boldsymbol{\beta}: \boldsymbol{\beta}^T\Phi_t = 0$ |
| 物理表现 | $\dot{\mathbf{q}} \to \infty$，运动终止 | 两条运动路径 |
| 检测 | $\dot{\mathbf{q}} \to \infty$ | $|\Phi_\mathbf{q}|$ 变号 |

**虚位移与分岔**：奇异时 $\exists\delta\mathbf{q}\neq\mathbf{0}$ 使 $\Phi_\mathbf{q}\delta\mathbf{q} = \mathbf{0}$，若速度解存在则 $\dot{\mathbf{q}} \pm \delta\mathbf{q}$ 都是解 → 分岔。

**设计敏感性**：$\Phi_\mathbf{q}\delta\mathbf{q} = -\Phi_\mathbf{b}\delta\mathbf{b}$，奇异点处某些设计变化可能导致无法装配。

**冗余约束**：Jacobian 行秩 < 约束数时存在冗余。一致冗余（约束自动满足）和不一致冗余（无解）需通过秩检验区分。

---

## 工程应用与实例

| 图号/例题号 | 名称 | 类型 | 应用 | 关键知识点 |
|------------|------|------|------|-----------|
| Ex 3.1.1, Fig 3.1.2 | Simple pendulum | 单体摆 | 基本约束建模 | DOF=1, Jacobian行列式恒为1 |
| Ex 3.1.2, Fig 3.1.3 | Two-body slider-crank | 滑块-曲柄 | 多体约束组装 | 6坐标+5约束+1驱动, Jacobian稀疏 |
| Ex 3.1.3, Fig 3.1.4 | Inclined slider | 斜面滑块 | 约束公式化陷阱 | 约束未蕴含铰几何→奇异 |
| Ex 3.3.3, Fig 3.3.2 | Four-bar (revolute) | 四连杆 | 转动副建模 | 地面为body 4, 4个转动副, DOF=1 |
| Ex 3.3.4, Fig 3.3.6 | Four-body slider-crank | 四体曲柄滑块 | 混合转动+移动副 | 3转动+1移动, DOF=1 |
| Ex 3.4.1, Fig 3.4.3 | Gear pair | 齿轮对 | 齿轮约束验证 | $R_1=1, R_2=2$ |
| Ex 3.4.2, Fig 3.4.6 | Slider-crank + rack-pinion | 曲柄+齿条 | 齿条控制曲柄 | 速度解数值结果 |
| Ex 3.4.3, Fig 3.4.9 | Cam-follower (IC engine) | 凸轮-从动件 | 内燃机气门 | 分段轮廓 $\rho_1(\alpha_1)$ |
| Ex 3.4.5, Fig 3.4.13 | Point-follower (valve lifter) | 点从动件 | 替代建模方式 | $\dot{y}_2 = \frac{3}{4}\cos 3\phi_1$ |
| Ex 3.5.2, Fig 3.5.3 | Four-bar (rotational driver) | 四连杆+转角驱动 | 绝对转角驱动 | 5×5速度方程 |
| Ex 3.5.3, Fig 3.5.6 | Excavator boom | 挖掘机动臂 | 双液压缸驱动 | $C_{41}(t) = \frac{1}{3}t + 1.8$ |
| Ex 3.5.5, Fig 3.5.10 | Wrecker boom | 吊车臂 | 平移距离驱动 | 4×4速度方程 |
| Ex 3.6.2, Fig 3.6.2 | Double pendulum (1-DOF) | 双摆 | 完整N-R分析 | 2次迭代收敛, $\|\Phi_\mathbf{q}\|=-\cos\phi_2$ |
| Ex 3.7.1, Fig 3.7.1 | Slider-crank lock-up | 曲柄滑块 | Lock-up | $\sin\phi_1 = \ell$ |
| Ex 3.7.2, Fig 3.7.4 | Parallelogram bifurcation | 平行四杆 | Bifurcation | 两种运动路径 |
| Ex 3.7.3, Fig 3.7.6 | Two-body analytical | 双体简化 | 解析奇异分析 | $q = \cos\omega t \mp \sqrt{\cos^2\omega t + \ell^2 - 1}$ |
| Ex 3.7.7, Fig 3.7.9 | Five-bar parallelogram | 五体平行四杆 | 冗余约束 | Jacobian秩恒为2 |

---

## 与全书的关系

| 本章概念 | 后续展开位置 |
|----------|------------|
| 约束方程 $\Phi(\mathbf{q},t)=\mathbf{0}$ | Ch.4（数值求解的完整实现）, Ch.5-7（动力学方程中的约束力） |
| Jacobian $\Phi_\mathbf{q}$ | Ch.4（稀疏矩阵技术）, Ch.6（Lagrange乘子法）, Ch.7（增广公式） |
| Newton-Raphson 位置求解 | Ch.4（详细算法流程、收敛策略、代码实现） |
| 速度/加速度方程 $\boldsymbol{\nu}, \boldsymbol{\gamma}$ | Ch.4（计算机实现方法）, Ch.6-7（动力学方程右端项） |
| 奇异构型 $\|\Phi_\mathbf{q}\|=0$ | Ch.4（数值检测方法）, Ch.5（动力学中的奇异处理） |
| 冗余约束 | Ch.4 §4.6（冗余约束的识别和消除算法） |
| 虚位移 $\delta\mathbf{q}$ | Ch.6（虚功原理，Lagrange方程的基础） |
| 设计参数 $\mathbf{b}$ | Ch.5（运动学设计灵敏度分析） |
| 平面笛卡尔方法（整体） | Ch.9-11（空间系统的推广：3D旋转矩阵、Euler参数等） |
