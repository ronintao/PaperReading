---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 6
title: "Dynamics of Planar Systems"
pages: 199-242
sections:
  - "6.1 Equations of Motion for a Rigid Body"
  - "6.2 Virtual Work and Generalized Force"
  - "6.3 Equations of Motion for Constrained Planar Systems"
  - "6.4 Inverse Dynamics of Kinematically Driven Systems"
  - "6.5 Equilibrium Conditions"
  - "6.6 Constraint Reaction Forces"
created: 2025-07-27
last_updated: 2025-07-27
---

# Chapter 6: Dynamics of Planar Systems

> 本章是全书从运动学到动力学的关键跨越。从牛顿方程出发，经达朗贝尔原理（虚功原理）消除内力，建立单刚体变分运动方程；然后引入广义力概念，将单体方程推广为多体系统的约束变分方程；再通过拉格朗日乘子定理将约束条件从虚位移限制转化为力方程，最终建立混合微分-代数方程（DAE）形式的约束动力学方程。此外还涵盖逆动力学、平衡条件和约束反力的系统化计算方法。

## 章节定位

| 维度 | 说明 |
|------|------|
| **前置** | Ch.2–3 运动学约束与雅可比矩阵，Ch.4 数值求解，Ch.5 建模实践 |
| **本章** | §6.1 单刚体运动方程 → §6.2 广义力 → §6.3 约束系统 DAE → §6.4 逆动力学 → §6.5 平衡 → §6.6 反力 |
| **后续** | Ch.7 数值积分方法（求解 DAE），Ch.8 动力学建模案例 |

## 概念定义

### §6.1 刚体运动方程

**Model of a Rigid Body（刚体模型）** [p.199]
> As a *model of a rigid body*, let a distance constraint (a massless bar with revolute joints at both ends) act between each pair of differential elements (thought of as particles) in the body.
>
> 刚体模型：在刚体的每对微分质量元素（视为质点）之间施加距离约束（一根两端带铰链的无质量杆件），以此约束体内各点间距离不变。

---

**Virtual Displacement（虚位移）** [p.200]
> Let $\delta\mathbf{r}^P$ denote an arbitrary *virtual displacement* of point $P$; that is, a small variation in the location of point $P$ that is permitted to occur with time held fixed. The $\delta$ operator is just the differential operator of calculus with time held fixed.
>
> 虚位移：点 $P$ 的任意虚位移 $\delta\mathbf{r}^P$ 是指在时间保持不变的条件下，点 $P$ 位置所允许的微小变分。$\delta$ 算子即为时间冻结时的微积分微分算子。

---

**D'Alembert's Principle / Principle of Virtual Work（达朗贝尔原理 / 虚功原理）** [p.202]
> $\int_m \delta\mathbf{r}^{PT}\ddot{\mathbf{r}}^P\,dm(P) = \int_m \delta\mathbf{r}^{PT}\mathbf{F}(P)\,dm(P)$ (Eq. 6.1.4), which must hold for all $\delta\mathbf{r}^P$ that are consistent with constraints on $\mathbf{r}^P$ that define rigid-body motion.
>
> 达朗贝尔原理（虚功原理）：对所有满足刚体运动约束的虚位移 $\delta\mathbf{r}^P$，惯性力的虚功等于外力的虚功。该结果消除了内力，只需处理外力。

---

**Centroid / Center of Mass（质心）** [p.203]
> If the origin of the $x'$-$y'$ frame is located at the *center of mass* or *centroid* of the body, then $\int_m \mathbf{s}'^P\,dm(P) = \mathbf{0}$ (Eq. 6.1.13).
>
> 质心：若体固坐标系 $x'$-$y'$ 的原点位于刚体质心，则按质心定义有 $\int_m \mathbf{s}'^P\,dm(P) = \mathbf{0}$。

---

**Polar Moment of Inertia（极惯性矩）** [p.207]
> $J' \equiv \int_m \mathbf{s}'^{PT}\mathbf{s}'^P\,dm(P)$ (Eq. 6.1.15), the polar moment of inertia with respect to the origin of the body-fixed $x'$-$y'$ frame.
>
> 极惯性矩：刚体相对于体固坐标系原点的极惯性矩，度量质量分布距参考点的远近。

---

**Parallel Axis Theorem（平行轴定理）** [p.207]
> $J'' = J' + m|\boldsymbol{\rho}''|^2$ (Eq. 6.1.22). This relation is called the *parallel axis theorem* for polar moment of inertia.
>
> 平行轴定理：非质心参考系的极惯性矩 $J''$ = 质心极惯性矩 $J'$ + $m$ $\times$ 质心到参考点距离的平方。

---

**Component / Composite Body（组合体）** [p.210]
> A typical example of such a *component* (or *composite body*) is shown in Fig. 6.1.5, in which all subcomponents and voids have some standard shape.
>
> 组合体：由多个标准形状子部件和空洞组合而成的刚体，其惯性属性可通过子部件的惯性属性叠加计算。空洞视为负质量。

---

### §6.2 虚功与广义力

**Virtual Work of a Force and Torque（力和力矩的虚功）** [p.213]
> $\delta W = \delta\mathbf{r}^T\mathbf{F} + \delta\phi\,n = \delta\mathbf{q}^T\mathbf{Q}$ (Eq. 6.2.1), where $\mathbf{q} = [\mathbf{r}^T, \phi]^T$ and $\mathbf{Q} = [\mathbf{F}^T, n]^T$ (Eq. 6.2.2).
>
> 虚功：力 $\mathbf{F}$ 和力矩 $n$ 对虚位移 $\delta\mathbf{r}$ 和虚转角 $\delta\phi$ 所做的虚功。广义力 $\mathbf{Q}$ 是与广义坐标 $\mathbf{q}$ 配对的力向量。

---

**Generalized Force（广义力）** [p.214]
> The basic idea in defining *generalized force* $\mathbf{Q}$ associated with generalized coordinate $\mathbf{q}$ is to first write the virtual work of a set of forces and moments in terms of products of physical virtual displacements and forces. Next, virtual displacements are written in terms of variations $\delta\mathbf{q}$ in generalized coordinates. Finally, coefficients of all variations are collected. These coefficients are defined to be generalized forces.
>
> 广义力：将虚功从物理力 $\times$ 物理虚位移改写为广义坐标变分 $\delta\mathbf{q}$ 的系数形式后，这些系数即为与对应广义坐标配对的广义力。

---

**Translational Spring-Damper-Actuator（平移弹簧-阻尼器-作动器）** [p.215]
> A compliant element in applications may consist of a spring, a damper, or a force actuator such as a hydraulic cylinder that exerts a force along the vector between points $P_i$ and $P_j$. Such an element is called a *translational spring-damper-actuator*.
>
> 平移弹簧-阻尼器-作动器：连接两个刚体上各一点的柔性元件，沿两点连线方向施力。可包含弹簧（刚度 $k$）、阻尼器（阻尼系数 $c$）和一般作动器力 $F$。

---

**Rotational Spring-Damper-Actuator（旋转弹簧-阻尼器-作动器）** [p.217–218]
> This compliant element exerts torques of equal magnitude but opposite orientation on bodies $i$ and $j$; hence it is called a *rotational spring-damper-actuator*.
>
> 旋转弹簧-阻尼器-作动器：在两刚体之间施加等大反向力矩的柔性元件。包含扭转弹簧（刚度 $k_\theta$）、扭转阻尼器（阻尼系数 $c_\theta$）和一般作动器力矩 $N$。

---

### §6.3 约束系统运动方程

**Applied Forces vs. Constraint Forces（施加力 vs. 约束力）** [p.219]
> *Applied forces* are defined here to be all forces acting on or between bodies in the system except forces of constraint. Thus, forces due to gravity and spring-damper-actuators are treated as applied forces.
>
> 施加力：除约束力外的所有力（重力、弹簧力、阻尼力、作动器力等）。约束力：运动副产生的反力。在虚功方法中，约束力对满足约束的虚位移不做功。

---

**Constrained Variational Equations of Motion（约束变分运动方程）** [p.220]
> $\delta\mathbf{q}^T[\mathbf{M}\ddot{\mathbf{q}} - \mathbf{Q}^A] = 0$ (Eq. 6.3.3), for all virtual displacements $\delta\mathbf{q}$ that are consistent with constraints.
>
> 约束变分运动方程：当虚位移满足系统约束时，所有约束力的虚功之和为零，因此运动方程中只含施加力。核心条件：$\delta\mathbf{q}$ 必须满足 $\boldsymbol{\Phi}_\mathbf{q}\delta\mathbf{q} = \mathbf{0}$。

---

**Lagrange Multiplier Theorem（拉格朗日乘子定理）** [p.223]
> If $\mathbf{b}^T\mathbf{x} = 0$ holds for all $\mathbf{x}$ that satisfy $\mathbf{A}\mathbf{x} = \mathbf{0}$, then there exists an $m$ vector $\boldsymbol{\lambda}$ of *Lagrange multipliers* such that $\mathbf{b}^T\mathbf{x} + \boldsymbol{\lambda}^T\mathbf{A}\mathbf{x} = 0$ for arbitrary $\mathbf{x}$.
>
> 拉格朗日乘子定理：若线性形式对所有满足线性约束的向量成立，则存在乘子向量使得对任意向量成立。这是将约束变分方程转化为 DAE 的数学基础。

---

**Mixed Differential-Algebraic Equations (DAE)（混合微分-代数方程）** [p.225]
> Eq. 6.3.18 is a *mixed system of differential-algebraic equations* (DAE), since no derivatives of the Lagrange multiplier $\boldsymbol{\lambda}$ appear.
>
> DAE：拉格朗日乘子形式的运动方程是微分方程（含 $\ddot{\mathbf{q}}$）和代数方程（约束 $\boldsymbol{\Phi} = \mathbf{0}$）的混合系统，$\boldsymbol{\lambda}$ 无导数项出现。

---

**Constrained Dynamic Existence Theorem（约束动力学存在性定理）** [p.225]
> Let $\boldsymbol{\Phi}_\mathbf{q}$ have full row rank and let the kinetic energy of the system be positive for any nonzero virtual velocity consistent with constraints. Then the coefficient matrix in Eq. 6.3.18 is nonsingular and $\ddot{\mathbf{q}}$ and $\boldsymbol{\lambda}$ are uniquely determined.
>
> 约束动力学存在性定理：当约束雅可比满秩且约束一致虚速度的动能严格正定时，DAE 系数矩阵非奇异，加速度和乘子唯一确定。

---

### §6.4 逆动力学

**Inverse Dynamics（逆动力学）** [p.229]
> If driving constraints equal in number to the number of kinematic degrees of freedom are appended, the system is kinematically determined and the constraint Jacobian is square and nonsingular. This very special situation yields simplified results applicable for the analysis of kinematically driven systems.
>
> 逆动力学：当驱动约束数 = 运动学自由度数时，系统运动完全确定，可直接求解加速度，再反求所需的驱动力/力矩（拉格朗日乘子）。

---

### §6.5 平衡条件

**Equilibrium（平衡）** [p.230]
> A system is said to be in *equilibrium* if it remains stationary under the action of applied forces; that is, if $\ddot{\mathbf{q}} = \dot{\mathbf{q}} = \mathbf{0}$.
>
> 平衡：系统在施加力作用下保持静止的状态。

---

**Total Potential Energy（总势能）** [p.231]
> $TPE = SE - W(F)$ (Eq. 6.5.3), where $SE$ is the strain energy of compliant components and $-W(F)$ is the potential energy of all forces.
>
> 总势能：弹性元件应变能加上外力势能之和。

---

**Principle of Minimum Total Potential Energy（最小总势能原理）** [p.231]
> For *conservative mechanical systems*, the *principle of minimum total potential energy* states that a system is in a state of stable equilibrium if the total potential energy takes on a strict relative minimum at that position.
>
> 最小总势能原理：对保守系统，稳定平衡状态对应总势能的严格相对最小值。

---

### §6.6 约束反力

**Constraint Reaction Force（约束反力）** [p.233–235]
> The objective is to use Eq. 6.6.2 to develop relations for joint reaction forces $\mathbf{F}_i^{nk}$ and torques $T_i^{nk}$ in terms of the Lagrange multipliers.
>
> 约束反力：将约束对刚体的作用等效为体固坐标系中的反力和反力矩，通过拉格朗日乘子系统化计算。

---

## 符号定义

### §6.1 基本量与惯性量

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{r}$ | 2×1 向量 | 体固坐标系原点在全局坐标系中的位置 |
| $\phi$ | 标量 | 刚体转角 |
| $\mathbf{q}$ | 3×1 向量 | 单体广义坐标 $\mathbf{q} = [\mathbf{r}^T, \phi]^T$ |
| $\mathbf{s}'^P$ | 2×1 向量 | 点 $P$ 在质心体固坐标系中的位置 |
| $\mathbf{r}^P$ | 2×1 向量 | 点 $P$ 的全局位置，$\mathbf{r}^P = \mathbf{r} + \mathbf{A}\mathbf{s}'^P$ |
| $\delta\mathbf{r}^P$ | 2×1 向量 | 点 $P$ 的虚位移 |
| $\mathbf{A}$ | 2×2 矩阵 | 旋转矩阵 $[\cos\phi, -\sin\phi; \sin\phi, \cos\phi]$ |
| $\mathbf{B}$ | 2×2 矩阵 | $\mathbf{A}$ 对 $\phi$ 的导数 |
| $m$ | 标量 | 刚体总质量 |
| $J'$ | 标量 | 质心极惯性矩 |
| $J''$ | 标量 | 非质心参考系极惯性矩 |
| $\mathbf{F}$ | 2×1 向量 | 合力 |
| $n$ | 标量 | 合力矩 |
| $\boldsymbol{\rho}''$ | 2×1 向量 | 质心在非质心体固系中的位置 |
| $\gamma$ | 标量 | 面密度（单位面积质量）|

### §6.2 虚功与广义力

| 符号 | 类型 | 含义 |
|------|------|------|
| $\delta W$ | 标量 | 虚功 |
| $\mathbf{Q}$ | 3×1 向量 | 广义力 $[\mathbf{F}^T, n]^T$ |
| $\mathbf{d}_{ij}$ | 2×1 向量 | 从体 $i$ 的 $P_i$ 到体 $j$ 的 $P_j$ 的向量 |
| $\ell$, $\ell_0$ | 标量 | 弹簧-阻尼器-作动器长度 / 自由长度 |
| $k$, $c$ | 标量 | 弹簧刚度 / 阻尼系数 |
| $f$ | 标量 | 平移弹簧-阻尼器-作动器总力 |
| $\theta_{ij}$ | 标量 | 体 $j$ 相对体 $i$ 的夹角，$\theta_{ij} = \phi_j - \phi_i$ |
| $k_\theta$, $c_\theta$ | 标量 | 扭转弹簧刚度 / 扭转阻尼系数 |
| $n$ | 标量 | 旋转弹簧-阻尼器-作动器总力矩 |

### §6.3 约束系统运动方程

| 符号 | 类型 | 含义 |
|------|------|------|
| $nb$ | 标量 | 系统中刚体数量 |
| $\mathbf{q}$ | $3nb$×1 向量 | 系统组合广义坐标 |
| $\mathbf{M}$ | $3nb$×$3nb$ 矩阵 | 系统质量矩阵 $\text{diag}(\mathbf{M}_1, \ldots, \mathbf{M}_{nb})$ |
| $\mathbf{Q}^A$, $\mathbf{Q}^C$ | 向量 | 组合广义施加力 / 约束力 |
| $\boldsymbol{\Phi}(\mathbf{q}, t)$ | $nc$×1 向量 | 约束方程 |
| $\boldsymbol{\Phi}_\mathbf{q}$ | $nc$×$3nb$ 矩阵 | 约束雅可比 |
| $\boldsymbol{\lambda}$ | $nc$×1 向量 | 拉格朗日乘子 |
| $\boldsymbol{\nu}$ | 向量 | $-\boldsymbol{\Phi}_t$，速度方程右端 |
| $\boldsymbol{\gamma}$ | 向量 | 加速度方程右端 |

### §6.5 平衡条件

| 符号 | 类型 | 含义 |
|------|------|------|
| $TPE$ | 标量 | 总势能 |
| $SE$ | 标量 | 弹性应变能 |
| $W(F)$ | 标量 | 外力做功 |

### §6.6 约束反力

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{F}_i^{nk}$ | 2×1 向量 | 约束 $k$ 对体 $i$ 的反力（体固 $x''$-$y''$ 系）|
| $T_i^{nk}$ | 标量 | 约束 $k$ 对体 $i$ 的反力矩 |
| $\mathbf{C}_i$ | 2×2 矩阵 | $x''$-$y''$ 到 $x'$-$y'$ 坐标系的旋转矩阵 |

## 核心论点

### §6.1 从牛顿方程到变分运动方程

本节从最基本的牛顿第二定律出发，推导出刚体变分运动方程（虚功原理）。核心推导链：

1. **起点**：微分质量的牛顿方程（Eq. 6.1.1）——包含内力，且对每个微元都要写，不实用。

2. **虚功预乘**：两端左乘 $\delta\mathbf{r}^{PT}$，对全体质量积分。

3. **消除内力**：利用刚体距离约束的变分性质——$\delta(\mathbf{r}^P - \mathbf{r}^R)$ 正交于 $(\mathbf{r}^P - \mathbf{r}^R)$，而内力沿此方向，故 $\iint \delta\mathbf{r}^{PT}\mathbf{f}(P,R)dm(R)dm(P) = 0$（Eq. 6.1.3）。

4. **达朗贝尔原理**：$\int_m \delta\mathbf{r}^{PT}\ddot{\mathbf{r}}^P dm = \int_m \delta\mathbf{r}^{PT}\mathbf{F}(P)dm$（Eq. 6.1.4）。

5. **代入刚体运动学**：$\mathbf{r}^P = \mathbf{r} + \mathbf{A}\mathbf{s}'^P$，$\delta\mathbf{r}^P = \delta\mathbf{r} + \delta\phi\,\mathbf{B}\mathbf{s}'^P$，$\ddot{\mathbf{r}}^P = \ddot{\mathbf{r}} + \ddot{\phi}\mathbf{B}\mathbf{s}'^P - \dot{\phi}^2\mathbf{A}\mathbf{s}'^P$。

6. **质心坐标系下简化**：交叉项消失，离心项消失（反对称性），得到：

$$\delta\mathbf{r}^T[m\ddot{\mathbf{r}} - \mathbf{F}] + \delta\phi[J'\ddot{\phi} - n] = 0 \quad \text{(Eq. 6.1.18)}$$

7. **微分运动方程**：由 $\delta\mathbf{r}$ 和 $\delta\phi$ 任意性得 $m\ddot{\mathbf{r}} = \mathbf{F}$，$J'\ddot{\phi} = n$（Eq. 6.1.19）。

**关键洞察**：虚功方法的核心优势在于利用刚体约束的几何特性一步消除内力。

### §6.1.4 质心和极惯性矩的计算

- **质心**：$\boldsymbol{\rho}'' = \frac{1}{m}\int_m \mathbf{s}''^P dm(P)$
- **平行轴定理**：$J'' = J' + m|\boldsymbol{\rho}''|^2$
- **组合体**：$\boldsymbol{\rho}'' = \frac{1}{m}\sum m_i\boldsymbol{\rho}_i''$，$J^* = \sum(J_i' + m_i|\boldsymbol{\rho}_i^*|^2)$，空洞视为负质量

**Table 6.1.1 — 常见平面均质体的质量和极惯性矩**：

| 形状 | 质量 $m$ | 极惯性矩 $J'$（关于质心） |
|------|---------|----------------------|
| 细杆 | $\gamma\ell h$ | $\frac{m}{12}\ell^2$ |
| 矩形 | $\gamma ab$ | $\frac{1}{12}m(a^2+b^2)$ |
| 等腰三角形 | $\frac{1}{2}\gamma bh$ | $m(\frac{b^2}{24}+\frac{h^2}{18})$ |
| 圆 | $\gamma\pi R^2$ | $\frac{1}{2}mR^2$ |
| 半圆 | $\frac{1}{2}\gamma\pi R^2$ | $mR^2(\frac{1}{2}-\frac{16}{9\pi^2})$ |
| 细环 | $2\pi R\gamma d$ | $mR^2$ |

### §6.2 虚功与广义力

#### 外力的广义力

对作用在体 $i$ 上点 $P$ 的力 $\mathbf{F}^P$（全局坐标）：

$$\mathbf{Q} = \begin{bmatrix} \mathbf{F}^P \\ \mathbf{s}'^{PT}\mathbf{B}_i^T\mathbf{F}^P \end{bmatrix} \quad \text{(Eq. 6.2.3)}$$

若力是体固的（如火箭推力 $\mathbf{F}'^P$）：

$$\mathbf{Q} = \begin{bmatrix} \mathbf{A}_i \\ (\mathbf{R}\mathbf{s}'^P)^T \end{bmatrix}\mathbf{F}'^P \quad \text{(Eq. 6.2.4)}$$

#### 平移弹簧-阻尼器-作动器

力：$f = k(\ell - \ell_0) + c\dot{\ell} + F(\ell, \dot{\ell}, t)$（Eq. 6.2.10）

虚功（拉力为正）：$\delta W = -f\,\delta\ell$（Eq. 6.2.11）

广义力：

$$\mathbf{Q}_i = \frac{f}{\ell}\begin{bmatrix}\mathbf{d}_{ij}\\\mathbf{d}_{ij}^T\mathbf{B}_i\mathbf{s}_i'\end{bmatrix}, \quad \mathbf{Q}_j = -\frac{f}{\ell}\begin{bmatrix}\mathbf{d}_{ij}\\\mathbf{d}_{ij}^T\mathbf{B}_j\mathbf{s}_j'\end{bmatrix} \quad \text{(Eq. 6.2.14)}$$

#### 旋转弹簧-阻尼器-作动器

力矩：$n = k_\theta(\theta_{ij} - \theta_0) + c_\theta\dot{\theta}_{ij} + N(\theta_{ij}, \dot{\theta}_{ij}, t)$（Eq. 6.2.18）

广义力：$\mathbf{Q}_i = [0, 0, n]^T$，$\mathbf{Q}_j = -[0, 0, n]^T$（Eq. 6.2.22）

### §6.3 约束平面系统的运动方程

#### 6.3.1 系统变分方程

1. 各体变分方程求和：$\sum_{i=1}^{nb}\delta\mathbf{q}_i^T[\mathbf{M}_i\ddot{\mathbf{q}}_i - \mathbf{Q}_i] = 0$
2. 分离施加力与约束力：$\mathbf{Q} = \mathbf{Q}^A + \mathbf{Q}^C$
3. **约束力虚功消除**：对满足约束的虚位移，约束力总虚功为零（运动副约束力等大反向，在约束一致虚位移下互相抵消）
4. **关键区别**：单体约束力虚功 $\neq 0$；但求和后对约束一致虚位移为零
5. 结果：$\delta\mathbf{q}^T[\mathbf{M}\ddot{\mathbf{q}} - \mathbf{Q}^A] = 0$，其中 $\boldsymbol{\Phi}_\mathbf{q}\delta\mathbf{q} = \mathbf{0}$

#### 6.3.2 拉格朗日乘子

乘子定理保证存在 $\boldsymbol{\lambda}$ 使得对**任意** $\delta\mathbf{q}$：

$$\mathbf{M}\ddot{\mathbf{q}} + \boldsymbol{\Phi}_\mathbf{q}^T\boldsymbol{\lambda} = \mathbf{Q}^A \quad \text{(Eq. 6.3.16)}$$

物理解读：$\boldsymbol{\Phi}_\mathbf{q}^T\boldsymbol{\lambda} = \mathbf{Q}^C$（广义约束力）。

#### 6.3.3 混合微分-代数方程

$$\begin{bmatrix}\mathbf{M} & \boldsymbol{\Phi}_\mathbf{q}^T\\\boldsymbol{\Phi}_\mathbf{q} & \mathbf{0}\end{bmatrix}\begin{bmatrix}\ddot{\mathbf{q}}\\\boldsymbol{\lambda}\end{bmatrix} = \begin{bmatrix}\mathbf{Q}^A\\\boldsymbol{\gamma}\end{bmatrix} \quad \text{(Eq. 6.3.18)}$$

**存在唯一性**：当 $\boldsymbol{\Phi}_\mathbf{q}$ 满秩且 $\mathbf{M}$ 在约束一致子空间上正定时，系数矩阵非奇异。

#### 6.3.4 初始条件

| 条件 | 方程 | 方程数 |
|------|------|--------|
| 运动+驱动约束 | $\boldsymbol{\Phi}(\mathbf{q}, t_0) = \mathbf{0}$ | $nc$ |
| 初始位置条件 | $\boldsymbol{\Phi}'(\mathbf{q}(t_0), t_0) = \mathbf{0}$ | $= DOF$ |
| 速度约束 | $\boldsymbol{\Phi}_\mathbf{q}\dot{\mathbf{q}}(t_0) = \boldsymbol{\nu}(t_0)$ | $nc$ |
| 初始速度条件 | $\mathbf{B}'\dot{\mathbf{q}}(t_0) = \mathbf{v}'$ | $= DOF$ |

### §6.4 逆动力学

当驱动约束数 = DOF 时，$|\boldsymbol{\Phi}_\mathbf{q}| \neq 0$（Eq. 6.4.1）。

**加速度直接求解**：$\ddot{\mathbf{q}} = \boldsymbol{\Phi}_\mathbf{q}^{-1}\boldsymbol{\gamma}$（Eq. 6.4.4）

**乘子反求**：$\boldsymbol{\lambda} = \boldsymbol{\Phi}_\mathbf{q}^{-1T}[\mathbf{Q}^A - \mathbf{M}\ddot{\mathbf{q}}]$（Eq. 6.4.5）

**工程价值**：工程师指定驱动运动，求解所需的驱动力/力矩，评估作动器能力。§6.6 的反力公式进一步将乘子转化为物理反力。

### §6.5 平衡条件

**平衡方程**：$\boldsymbol{\Phi}_\mathbf{q}^T\boldsymbol{\lambda} = \mathbf{Q}^A$（Eq. 6.5.2）

**最小总势能原理**（保守系统）：

$$TPE = SE - W(F) \quad \text{(Eq. 6.5.3)}$$

- 线性弹簧：$SE = \frac{1}{2}k(\ell-\ell_0)^2$，旋转弹簧：$\frac{1}{2}k_\theta(\theta-\theta_0)^2$
- 常力势能：$-W(F) = -(x^PF_x^P + y^PF_y^P + n\phi)$

**关键性质**：$\frac{\partial TPE}{\partial\mathbf{q}} = -\mathbf{Q}^{AT}$（Eq. 6.5.8）——广义力是总势能梯度的负值，为数值最小化提供梯度。

### §6.6 约束反力

**一般反力公式**（体固 $x''$-$y''$ 坐标系中）：

$$\mathbf{F}_i^{nk} = -\mathbf{C}_i^T\mathbf{A}_i^T\boldsymbol{\Phi}_{\mathbf{r}_i}^{kT}\boldsymbol{\lambda}^k \quad \text{(Eq. 6.6.8)}$$

$$T_i^{nk} = (\mathbf{s}_i'^{PT}\mathbf{B}_i^T\boldsymbol{\Phi}_{\mathbf{r}_i}^{kT} - \boldsymbol{\Phi}_{\phi_i}^{kT})\boldsymbol{\lambda}^k \quad \text{(Eq. 6.6.9)}$$

**标准关节特化**：
- **绝对 $x$ 约束**：$\mathbf{F}_i^{ax} = -[1,0]^T\lambda^{ax}$（仅 $x$ 分量），无反力矩
- **铰链约束**：$\mathbf{F}_i^{r} = -\boldsymbol{\lambda}^{r}$（乘子即为反力的负值），无反力矩
- **平移约束**：反力垂直于平移方向，反力矩一般不为零

## 工程应用与实例

| 图号/例题号 | 名称 | 类型 | 关键知识点 |
|------------|------|------|-----------|
| Fig. 6.1.1 | 刚体受力图 | 示意图 | 内力模型：距离约束杆 |
| Example 6.1.1 | 拖拉机平面运动方程 | 单体建模 | 小角近似→线性方程；Eq. 6.1.19 直接适用 |
| Table 6.1.1 | 常见平面体 $m$ 和 $J'$ | 公式表 | 细杆、矩形、三角形、圆、半圆、细环 |
| Example 6.1.2 | 组合摆的质心和极惯性矩 | 组合体计算 | 杆+圆盘-孔洞，平行轴定理逐部件叠加 |
| Fig. 6.2.2 | 平移弹簧-阻尼器-作动器 | 示意图 | 向量 $\mathbf{d}_{ij}$，力 $f$，虚功 $\delta W = -f\delta\ell$ |
| Fig. 6.2.3 | 旋转弹簧-阻尼器-作动器 | 示意图 | 相对角 $\theta_{ij}$，力矩 $n$ |
| Example 6.3.1 | 简单摆——约束变分方程 | 建模 | 3坐标，2约束，1 DOF |
| Example 6.3.2 | 两体曲柄滑块——约束变分方程 | 建模 | 6坐标 - 5约束 = 1 DOF |
| Example 6.3.3 | 拉格朗日乘子数值例 | 代数例题 | 验证乘子定理 |
| Example 6.3.4 | 简单摆——DAE | 建模 | 5×5 系统 |
| Example 6.3.5 | 两体曲柄滑块——DAE | 建模 | 11×11 系统 |
| Example 6.3.6 | 简单摆——初始条件 | 建模 | 初位+约束→$\mathbf{q}(0)$；初速+速度约束→$\dot{\mathbf{q}}(0)$ |
| Example 6.4.1 | 简单摆——逆动力学 | 逆动力学 | 运动学确定→直接求 $\ddot{\mathbf{q}}$→反求 $\boldsymbol{\lambda}$ |
| Example 6.5.1 | 带扭转弹簧的简单摆——平衡 | 平衡分析 | 非线性平衡方程：弹簧力矩 = 重力力矩 |
| Example 6.5.2 | 双摆——平衡 | 平衡分析 | 最小势能法，解析解 $\phi = \arctan(...)$ |
| Example 6.6.1 | 简单摆——约束反力 | 反力计算 | 从乘子→物理反力+驱动力矩 |

### 习题结构

| 节号 | 习题编号 | 主题 |
|------|--------|------|
| §6.1 | 6.1.1–6.1.6 | 虚位移验证、变分方程验证、反对称性验证、组合体惯性矩 |
| §6.2 | 6.2.1–6.2.2 | 变距离力元广义力、弹簧+平移副广义力 |
| §6.3 | 6.3.1–6.3.4 | 双摆变分方程/DAE/初始条件、乘子定理反例 |
| §6.4 | 6.4.1–6.4.3 | 单摆/滑块-摆/曲柄滑块逆动力学 |
| §6.5 | 6.5.1–6.5.2 | 弹簧支撑滑块平衡、双摆约束平衡 |
| §6.6 | 6.6.1–6.6.4 | 各类关节反力计算 |

## 与全书的关系

**承前**：
- Ch.2–3 的约束方程 $\boldsymbol{\Phi}$、雅可比 $\boldsymbol{\Phi}_\mathbf{q}$、加速度方程 $\boldsymbol{\gamma}$ 在本章 DAE 中直接复用
- Ch.4 的 Newton-Raphson 方法用于求解非线性初始条件和平衡方程
- Ch.5 的建模经验（选体、选约束、选驱动）直接迁移到动力学建模

**启后**：
- Ch.7 将介绍求解 DAE (Eq. 6.3.18) 的数值积分方法（本章仅建立方程，未求解）
- Ch.7 还将实现最小势能法中的数值最小化算法（Eq. 6.5.8 提供梯度）
- Ch.8 将用本章的动力学方程对实际机构进行仿真分析

**核心贡献**：本章建立了完整的从"多体运动学模型"到"多体动力学方程"的桥梁。关键步骤是：虚功原理消除内力 → 广义力统一力的表示 → 拉格朗日乘子解除虚位移限制 → DAE 成为可计算的标准形式。
