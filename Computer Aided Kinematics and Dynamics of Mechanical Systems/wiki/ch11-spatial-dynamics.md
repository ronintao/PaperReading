---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 11
title: "Dynamics of Spatial Systems"
pages: 416-454
sections:
  - "11.1 Equations of Motion for a Rigid Body"
  - "11.2 Properties of Mass Center, Moments of Inertia, and Products of Inertia"
  - "11.3 Equations of Motion of Constrained Spatial Systems"
  - "11.4 Internal Forces"
  - "11.5 Inverse Dynamics, Equilibrium Analysis, and Reaction Forces in Joints"
  - "11.6 Numerical Considerations in Solving Spatial Differential-Algebraic Equations of Motion"
created: 2026-05-19
last_updated: 2026-05-19
---

# Chapter 11: Dynamics of Spatial Systems

## 章节定位

本章是 Part Two（空间系统）的**动力学核心**，与 Part One 中 Ch.6（Dynamics of Planar Systems）完全对应。Ch.9-10 建立了空间运动学的理论框架和建模方法，本章将运动学扩展到动力学领域：

1. **单刚体运动方程**（§11.1）——从牛顿定律经 d'Alembert 原理推导变分 Newton-Euler 方程，关键区别在于陀螺项 $\tilde{\boldsymbol{\omega}}'\mathbf{J}'\boldsymbol{\omega}'$
2. **惯性属性**（§11.2）——质心、惯性矩阵变换、平行轴定理、主轴、复合体惯性
3. **约束系统运动方程**（§11.3）——两种形式：Newton-Euler 形式（一阶混合 DAE）和 Euler 参数形式（二阶 DAE）
4. **内力（力元）**（§11.4）——TSDA 和 RSDA 的广义力推导
5. **逆动力学与反力**（§11.5）——与 Ch.6 流程完全平行
6. **数值方法**（§11.6）——两种积分策略的对比，DADS 软件实现

与 Ch.6 的核心区别：角速度为 3×1 向量（非标量）、惯性矩阵为 3×3（非标量）、姿态用 Euler 参数（非角度）、旋转方程含非线性陀螺项。

---

## 概念定义

**Centroidal Body Reference Frame（质心体固定参考系）** [p.420]
> A body-fixed x'-y'-z' reference frame selected with its origin at the center of mass (or centroid) of the body. It is thus called a centroidal body reference frame.
>
> 选择原点位于刚体质心（center of mass / centroid）的体固定 x'-y'-z' 参考系，称为质心体固定参考系。

---

**Inertia Matrix / Inertia Tensor（惯性矩阵 / 惯性张量）** [p.420]
> The constant inertia matrix (or inertia tensor) J' with respect to the x'-y'-z' centroidal frame is defined as J' ≡ -∫_m š'^P š'^P dm(P). The diagonal elements are called moments of inertia and the off-diagonal elements are called products of inertia. J' is symmetric: J' = J'^T.
>
> 关于质心系 x'-y'-z' 的常量惯性矩阵（惯性张量）J' 定义为 J' ≡ -∫_m š'^P š'^P dm(P)。对角元素称为惯性矩（moments of inertia），非对角元素称为惯性积（products of inertia）。J' 是对称矩阵：J' = J'^T。

---

**Newton-Euler Equations of Motion（牛顿-欧拉运动方程）** [p.422]
> For an unconstrained rigid body: mr̈ = F and J'ω̇' = n' - ω̃'J'ω'. These are differential equations in r and ω'. Since ω' cannot be integrated directly, a set of orientation generalized coordinates, such as Euler parameters, is required.
>
> 无约束刚体的运动方程：mr̈ = F 和 J'ω̇' = n' - ω̃'J'ω'。这是关于 r 和 ω' 的微分方程。由于 ω' 不能直接积分，需要引入姿态广义坐标（如 Euler 参数）。

---

**Euler Equations of Motion（欧拉方程）** [p.423]
> For a body with one point O'' fixed in space, with no orientation constraints, the Euler equations of motion are: J''ω̇'' = n'' - ω̃''J''ω''. These are nonlinear in angular velocities and closed-form solution is generally not possible.
>
> 对于一点 O'' 固定在空间中的物体，若无姿态约束，则欧拉方程为：J''ω̇'' = n'' - ω̃''J''ω''。方程右端角速度项为非线性，一般无封闭解。

---

**Plane of Symmetry / Axis of Symmetry（对称面 / 对称轴）** [p.427]
> A body has a plane of symmetry if the location of points and mass distribution are symmetric about a plane with normal n. The centroid lies on that plane. A body has an axis of symmetry if every plane containing that axis is a plane of symmetry.
>
> 若物体的质点位置和质量分布关于法线为 n 的某平面对称，则该平面称为对称面，质心位于对称面上。若包含某轴的每一个平面都是对称面，则该轴称为对称轴。

---

**Parallel Axis Theorem（平行轴定理）** [p.428]
> Moments of inertia with respect to a noncentroidal x''-y''-z'' frame (parallel to the centroidal frame, C=I) are those with respect to the parallel centroidal x'-y'-z' frame plus the mass times the square of the distances between the respective parallel axes.
>
> 关于非质心系 x''-y''-z''（与质心系平行，C=I）的惯性矩等于关于平行质心系 x'-y'-z' 的惯性矩加上质量乘以两平行轴间距离的平方。

---

**Principal Axes / Principal Moments of Inertia（主轴 / 主惯性矩）** [p.431]
> The axes of a centroidal reference frame for which the products of inertia are all zero are called principal axes. The eigenvalues ζ₁ ≥ ζ₂ ≥ ζ₃ ≥ 0 of J'' are the principal moments of inertia. The inertia matrix in the principal axis frame is diagonal: J' = diag(ζ₁, ζ₂, ζ₃).
>
> 使所有惯性积为零的质心参考系坐标轴称为主轴。J'' 的特征值 ζ₁ ≥ ζ₂ ≥ ζ₃ ≥ 0 即为主惯性矩。在主轴系下惯性矩阵为对角阵。

---

**Positive Semidefinite / Positive Definite（半正定 / 正定）** [p.430]
> The inertia matrix J'' is positive semidefinite: a^T J'' a ≥ 0 for any vector a. If mass density is nowhere zero in the body and there exist three linearly independent position vectors, J'' is positive definite.
>
> 惯性矩阵 J'' 是半正定的。若体内质量密度处处非零且存在三个线性无关的位置向量，则 J'' 为正定。

---

**Applied Forces / Constraint Forces（施加力 / 约束力）** [p.441]
> Forces and torques may be partitioned into applied (F^A, n'^A) and constraint (F^C, n'^C). For all constraints treated in this text, constraint forces do no work for virtual displacements consistent with constraints.
>
> 力和力矩可分为施加力（F^A, n'^A）和约束力（F^C, n'^C）。对本书所有约束，约束力对与约束一致的虚位移不做功。

---

**Constrained Newton-Euler Equations of Motion（约束 Newton-Euler 运动方程）** [p.441]
> The constrained Newton-Euler equations for a spatial multibody system: Mr̈ + Φ_r^T λ = F^A and J'ω̇' + Φ_π'^T λ = n'^A - ω̃'J'ω'. Must be supplemented with kinematic constraints and their time derivatives.
>
> 空间多体系统约束 Newton-Euler 方程：Mr̈ + Φ_r^T λ = F^A 和 J'ω̇' + Φ_π'^T λ = n'^A - ω̃'J'ω'。需辅以运动学约束及其时间导数。

---

**Euler Parameter Form of Equations of Motion（Euler 参数形式运动方程）** [p.442-445]
> The equations of motion written entirely in Euler parameters, with Lagrange multipliers λ (kinematic) and λᵖ (normalization), yield the Euler parameter system acceleration equation (Eq. 11.3.29) — a second-order mixed DAE that can be integrated using any method from Chapter 7.
>
> 完全用 Euler 参数表达的运动方程，含 Lagrange 乘子 λ（运动学）和 λᵖ（归一化），得到 Euler 参数系统加速度方程（Eq. 11.3.29）——可用 Ch.7 任意方法积分的二阶混合 DAE。

---

**Translational Spring-Damper-Actuator (TSDA)（平移弹簧-阻尼-作动器）** [p.445-447]
> A TSDA connects points Pᵢ and Pⱼ on bodies i and j. Force magnitude: f = k(ℓ - ℓ₀) + cℓ̇ + F(ℓ, ℓ̇). Generalized forces derived via virtual work δW = -f δℓ.
>
> TSDA 连接体 i 和体 j 上的点 Pᵢ 和 Pⱼ。力大小：f = k(ℓ - ℓ₀) + cℓ̇ + F(ℓ, ℓ̇)。广义力通过虚功 δW = -f δℓ 推导。

---

**Rotational Spring-Damper-Actuator (RSDA)（旋转弹簧-阻尼-作动器）** [p.448-449]
> An RSDA acts about the common axis of a revolute/cylindrical/screw joint. Torque: n = k_θ(θ + 2n_rev π) + c_θ θ̇ + N(θ + 2n_rev π, θ̇). Only angular generalized force components are nonzero.
>
> RSDA 作用于转动副/圆柱副/螺旋副公共轴。力矩：n = k_θ(θ + 2n_rev π) + c_θ θ̇ + N(θ + 2n_rev π, θ̇)。只有角向广义力分量非零。

---

**Joint Reaction Forces and Torques（关节反力与反力矩）** [p.450-451]
> For joint k with constraint Φᵏ = 0 and multipliers λᵏ: F_i^nk = -C_i^T A_i^T Φ_{r_i}^{kT} λᵏ and T_i^nk = -C_i^T(Φ_{π_i}^{kT} - s̃_i'^P A_i^T Φ_{r_i}^{kT})λᵏ (Eq. 11.5.6).
>
> 关节 k 的反力/反力矩公式（Eq. 11.5.6），通过 Lagrange 乘子和约束 Jacobian 直接计算。

---

## 符号定义

### §11.1 刚体运动方程

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{r}$ | 3×1 向量 | 体固定参考系原点在惯性系中的位置向量 |
| $\mathbf{s}'^P$ | 3×1 向量（常量） | 点 P 在质心体固定系中的位置向量 |
| $\mathbf{s}''^P$ | 3×1 向量（常量） | 点 P 在非质心体固定系 x''-y''-z'' 中的位置向量 |
| $dm(P)$ | 标量（微元） | 点 P 处的微分质量 |
| $m$ | 标量 | 刚体总质量 |
| $\mathbf{F}$ | 3×1 向量 | 总外力 |
| $\mathbf{n}'$ | 3×1 向量 | 关于质心系原点的总力矩 |
| $\mathbf{J}'$ | 3×3 对称矩阵（常量） | 质心惯性矩阵 |
| $\boldsymbol{\omega}'$ | 3×1 向量 | 体在体固定系中的角速度 |
| $\delta\mathbf{r}^P$ | 3×1 向量 | 点 P 的虚位移 |
| $\delta\boldsymbol{\pi}'$ | 3×1 向量 | 体固定系的虚转动 |

### §11.2 惯性属性

| 符号 | 类型 | 含义 |
|------|------|------|
| $\boldsymbol{\rho}''$ | 3×1 向量 | 质心在 x''-y''-z'' 系中的位置 |
| $\mathbf{C}$ | 3×3 正交矩阵 | 从 x''-y''-z'' 到 x'-y'-z' 的旋转矩阵 |
| $\mathbf{J}''$ | 3×3 对称矩阵 | 关于 x''-y''-z'' 系的惯性矩阵 |
| $\zeta_1, \zeta_2, \zeta_3$ | 标量（非负） | 主惯性矩（J'' 的特征值） |
| $\mathbf{f}'', \mathbf{g}'', \mathbf{h}''$ | 3×1 单位向量 | 主轴方向（J'' 的特征向量） |
| $m_i, \boldsymbol{\rho}_i''$ | 标量/向量 | 复合体第 $i$ 子构件的质量和质心位置 |

### §11.3 约束系统运动方程

| 符号 | 类型 | 含义 |
|------|------|------|
| $n_b$ | 正整数 | 系统中刚体数量 |
| $\mathbf{r}$ | $3n_b \times 1$ | 所有体质心位置堆叠向量 |
| $\mathbf{p}$ | $4n_b \times 1$ | 所有体 Euler 参数堆叠向量 |
| $\mathbf{M}$ | $3n_b \times 3n_b$ 对角 | 系统质量矩阵 |
| $\mathbf{J}'$ | $3n_b \times 3n_b$ 块对角 | 系统惯性矩阵 |
| $\boldsymbol{\Phi}_r, \boldsymbol{\Phi}_{\pi'}$ | 矩阵 | 约束 Jacobian（对 r 和对虚转动） |
| $\boldsymbol{\Phi}_{\mathbf{p}}$ | 矩阵 | 约束对 Euler 参数的 Jacobian，$\boldsymbol{\Phi}_{\mathbf{p}_i} = 2\boldsymbol{\Phi}_{\pi_i'}\mathbf{G}_i$ |
| $\boldsymbol{\Phi}_{\mathbf{p}}^{\mathbf{p}}$ | $n_b \times 4n_b$ | Euler 参数归一化约束 Jacobian |
| $\boldsymbol{\lambda}$ | 向量 | 运动学约束 Lagrange 乘子 |
| $\boldsymbol{\lambda}^{\mathbf{p}}$ | $n_b \times 1$ | Euler 参数归一化 Lagrange 乘子 |
| $\boldsymbol{\gamma}, \boldsymbol{\gamma}^{\mathbf{p}}$ | 向量 | 加速度方程右端项 |

### §11.4 内力

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{d}_{ij}$ | 3×1 向量 | 从 $P_i$ 到 $P_j$ 的向量 |
| $\ell, \ell_0$ | 标量 | TSDA 当前长度和自由长度 |
| $k, c$ | 标量 | TSDA 弹簧刚度和阻尼系数 |
| $f$ | 标量 | TSDA 合力大小 |
| $k_\theta, c_\theta$ | 标量 | RSDA 扭转弹簧和阻尼系数 |
| $\theta, n_{\text{rev}}$ | 标量/整数 | RSDA 相对转角和累积圈数 |
| $n$ | 标量 | RSDA 力矩大小 |
| $\mathbf{Q}_i, \mathbf{Q}_j$ | 向量 | 对体 $i, j$ 的广义力 |

### §11.5 反力

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{F}_i^{nk}$ | 3×1 向量 | 关节 $k$ 对体 $i$ 的反力（关节定义系） |
| $\mathbf{T}_i^{nk}$ | 3×1 向量 | 关节 $k$ 对体 $i$ 的反力矩（关节定义系） |
| $\mathbf{C}_i$ | 3×3 正交矩阵 | 从关节定义系到质心系的旋转矩阵 |
| $\mathbf{s}$ | $3n_b \times 1$ | 中间速度变量（一阶形式），$\mathbf{s} \equiv \dot{\mathbf{r}}$ |

## 核心论点

### §11.1 刚体运动方程

#### 从牛顿定律到变分形式

1. **起点**：牛顿第二定律对微分质量 $dm(P)$（Eq. 11.1.1）

2. **内力消除**：刚体距离约束导致内力共线，虚功为零（Eq. 11.1.6）

3. **变分方程**（d'Alembert 原理，Eq. 11.1.7）：
$$\int_m \delta\mathbf{r}^{PT}\ddot{\mathbf{r}}^P\,dm(P) - \int_m \delta\mathbf{r}^{PT}\mathbf{F}(P)\,dm(P) = 0$$

4. **引入广义坐标**：利用 $\delta\mathbf{r}^P = \delta\mathbf{r} - \mathbf{A}\tilde{\mathbf{s}}'^P\delta\boldsymbol{\pi}'$（Eq. 11.1.8）和 $\ddot{\mathbf{r}}^P$（Eq. 11.1.9）代入展开

5. **质心系简化**：$\int \mathbf{s}'^P\,dm = 0$ → 交叉项消失 → **变分 Newton-Euler 方程**：
$$\delta\mathbf{r}^T[m\ddot{\mathbf{r}} - \mathbf{F}] + \delta\boldsymbol{\pi}'^T[\mathbf{J}'\dot{\boldsymbol{\omega}}' + \tilde{\boldsymbol{\omega}}'\mathbf{J}'\boldsymbol{\omega}' - \mathbf{n}'] = 0 \quad (11.1.19)$$

6. **无约束** → Newton-Euler 方程（Eq. 11.1.20）：
$$m\ddot{\mathbf{r}} = \mathbf{F}, \quad \mathbf{J}'\dot{\boldsymbol{\omega}}' = \mathbf{n}' - \tilde{\boldsymbol{\omega}}'\mathbf{J}'\boldsymbol{\omega}'$$

#### 与平面动力学 (Ch.6) 的关键区别

| 对比项 | 平面 (Ch.6) | 空间 (Ch.11) |
|-------|------------|-------------|
| 角速度 | 标量 $\dot\theta$ | 3×1 向量 $\boldsymbol{\omega}'$ |
| 旋转方程陀螺项 | 无 | $\tilde{\boldsymbol{\omega}}'\mathbf{J}'\boldsymbol{\omega}'$（非线性） |
| 惯性矩阵 | 标量 $J$ | 3×3 矩阵 $\mathbf{J}'$ |
| 姿态表示 | 角度 $\theta$ | Euler 参数 $\mathbf{p}$（4个） |
| 封闭解 | 特殊情况可能 | 一般不可能 |

#### 一点固定的特殊情况

- 点 O'' 固定 → $\delta\mathbf{r} = 0$，使用非质心系 x''-y''-z''
- **Euler 方程**：$\mathbf{J}''\dot{\boldsymbol{\omega}}'' = \mathbf{n}'' - \tilde{\boldsymbol{\omega}}''\mathbf{J}''\boldsymbol{\omega}''$（Eq. 11.1.23）
- Example 11.1.2: 绕 y 轴旋转的摆 → 惯性积对反力矩有重大影响

### §11.2 惯性属性

#### 质心位置与对称性

$$\boldsymbol{\rho}'' = \frac{1}{m}\int_m \mathbf{s}''^P\,dm(P) \quad (11.2.1)$$

- 对称面 → 质心在对称面上
- 对称轴 → 质心在对称轴上

#### 惯性矩阵变换

一般公式（Eq. 11.2.7）：
$$\mathbf{J}'' = \mathbf{C}^T\mathbf{J}'\mathbf{C} + m(\boldsymbol{\rho}''^T\boldsymbol{\rho}''\mathbf{I} - \boldsymbol{\rho}''\boldsymbol{\rho}''^T)$$

平行轴定理（C = I）：$J_{x''x''} = J_{x'x'} + m(\rho_{y''}^2 + \rho_{z''}^2)$

对称面使惯性积消失：若 x''-y'' 平面是对称面 → $J_{z''x''} = J_{z''y''} = 0$

#### 主轴求解

1. 惯性矩阵对角化：$\mathbf{J}' = \mathbf{C}\mathbf{J}''\mathbf{C}^T$（Eq. 11.2.13）
2. J'' 半正定（Eq. 11.2.14），均质体 → 正定
3. 特征值分解 → $\mathbf{J}' = \text{diag}(\zeta_1, \zeta_2, \zeta_3)$

#### 复合体惯性

1. 质心定位（Eq. 11.2.18）：$\boldsymbol{\rho}'' = \frac{1}{m}\sum m_i\boldsymbol{\rho}_i''$
2. 复合体惯性矩阵（Eq. 11.2.19）：$\mathbf{J}^* = \sum \mathbf{J}_i^*$
3. 子构件惯性变换（Eq. 11.2.20）
4. 空腔处理：负质量子构件

#### Table 11.2.1 标准均质体惯性属性

| 体型 | 质量 | 主惯性矩 |
|------|------|---------|
| 细杆 | $\gamma\ell A$ | $J_{x'x'} = J_{z'z'} = \frac{m}{12}\ell^2$ |
| 正方体 | $\gamma a^3$ | $J = \frac{1}{6}ma^2$ |
| 长方体 | $\gamma abc$ | $J_{x'x'} = \frac{m}{12}(b^2+c^2)$ |
| 球 | $\frac{4}{3}\pi\gamma R^3$ | $J = \frac{2}{5}mR^2$ |
| 圆柱 | $\pi\gamma R^2 h$ | $J_{x'x'}=\frac{m}{12}(3R^2+h^2),\; J_{z'z'}=\frac{m}{2}R^2$ |
| 圆锥 | $\frac{1}{3}\pi\gamma R^2 h$ | $J_{x'x'}=\frac{3}{80}m(4R^2+h^2),\; J_{z'z'}=\frac{3}{10}mR^2$ |

### §11.3 约束系统运动方程

#### §11.3.1 约束 Newton-Euler 方程

1. 系统级变分方程 → 力的分解 → 约束力做零功
2. Lagrange 乘子引入 → **约束 Newton-Euler 方程**（Eq. 11.3.8）：

| 方程 | 内容 |
|------|------|
| 平移 | $\mathbf{M}\ddot{\mathbf{r}} + \boldsymbol{\Phi}_r^T\boldsymbol{\lambda} = \mathbf{F}^A$ |
| 旋转 | $\mathbf{J}'\dot{\boldsymbol{\omega}}' + \boldsymbol{\Phi}_{\pi'}^T\boldsymbol{\lambda} = \mathbf{n}'^A - \tilde{\boldsymbol{\omega}}'\mathbf{J}'\boldsymbol{\omega}'$ |
| 加速度约束 | $\boldsymbol{\Phi}_r\ddot{\mathbf{r}} + \boldsymbol{\Phi}_{\pi'}\dot{\boldsymbol{\omega}}' = \boldsymbol{\gamma}$ |

3. **系统加速度方程**（Eq. 11.3.11）——一阶混合 DAE（ω' 不可积分）
4. 需辅以 Euler 参数运动学方程和约束方程

#### §11.3.2 Euler 参数形式

1. **速度方程变换**：$\boldsymbol{\Phi}_r\dot{\mathbf{r}} + \boldsymbol{\Phi}_{\mathbf{p}}\dot{\mathbf{p}} = \mathbf{v}$（Eq. 11.3.14）
2. **关键恒等式**：$\dot{\boldsymbol{\omega}}' = 2\mathbf{G}\ddot{\mathbf{p}}$（因 $\dot{\mathbf{G}}\dot{\mathbf{p}} = 0$，Eq. 11.3.16-17）
3. **逆关系**（Eq. 11.3.21）：$\ddot{\mathbf{p}} = \frac{1}{2}\mathbf{G}^T\dot{\boldsymbol{\omega}}' - \frac{1}{4}\boldsymbol{\omega}'^T\boldsymbol{\omega}'\,\mathbf{p}$
4. **Euler 参数系统加速度方程**（Eq. 11.3.29）——二阶 DAE：

$$\begin{bmatrix} \mathbf{M} & 0 & \boldsymbol{\Phi}_r^T & 0 \\ 0 & 4\mathbf{G}^T\mathbf{J}'\mathbf{G} & \boldsymbol{\Phi}_{\mathbf{p}}^T & \boldsymbol{\Phi}_{\mathbf{p}}^{\mathbf{p}T} \\ \boldsymbol{\Phi}_r & \boldsymbol{\Phi}_{\mathbf{p}} & 0 & 0 \\ 0 & \boldsymbol{\Phi}_{\mathbf{p}}^{\mathbf{p}} & 0 & 0 \end{bmatrix} \begin{bmatrix} \ddot{\mathbf{r}} \\ \ddot{\mathbf{p}} \\ \boldsymbol{\lambda} \\ \boldsymbol{\lambda}^{\mathbf{p}} \end{bmatrix} = \begin{bmatrix} \mathbf{F}^A \\ 2\mathbf{G}^T\mathbf{n}'^A + 8\dot{\mathbf{G}}^T\mathbf{J}'\dot{\mathbf{G}}\mathbf{p} \\ \boldsymbol{\gamma} \\ \boldsymbol{\gamma}^{\mathbf{p}} \end{bmatrix}$$

#### Eq. 11.3.11 vs Eq. 11.3.29 对比

| 对比项 | Eq. 11.3.11 | Eq. 11.3.29 |
|-------|-------------|-------------|
| 未知量 | $\ddot{\mathbf{r}}, \dot{\boldsymbol{\omega}}', \boldsymbol{\lambda}$ | $\ddot{\mathbf{r}}, \ddot{\mathbf{p}}, \boldsymbol{\lambda}, \boldsymbol{\lambda}^{\mathbf{p}}$ |
| 阶数 | 一阶混合 DAE | 二阶 DAE |
| (2,2) 子矩阵 | $\mathbf{J}'$（常量） | $4\mathbf{G}^T\mathbf{J}'\mathbf{G}$（坐标相关） |
| 积分 | 需特殊处理 | 可直接用 Ch.7 方法 |

### §11.4 内力

#### §11.4.1 TSDA

- 几何：$\mathbf{d}_{ij}$（Eq. 11.4.1）、$\ell^2 = \mathbf{d}_{ij}^T\mathbf{d}_{ij}$、$\dot{\ell}$（Eq. 11.4.4）
- 力：$f = k(\ell - \ell_0) + c\dot{\ell} + F(\ell, \dot{\ell})$（Eq. 11.4.6）
- 广义力（Eq. 11.4.10）：$\mathbf{Q}_i = \frac{f}{\ell}\begin{bmatrix}\mathbf{d}_{ij} \\ \tilde{\mathbf{s}}_i'^P\mathbf{A}_i^T\mathbf{d}_{ij}\end{bmatrix}$
- $\ell \to 0$ 时用 L'Hôpital 法则（Eq. 11.4.5）

#### §11.4.2 RSDA

- 累积角：$\theta + 2n_{\text{rev}}\pi$
- 力矩：$n = k_\theta(\theta + 2n_{\text{rev}}\pi) + c_\theta\dot{\theta} + N$（Eq. 11.4.12）
- 广义力（Eq. 11.4.16）：$\mathbf{Q}_i = [0;\; n\mathbf{h}_i']$（只有角向分量非零）

### §11.5 逆动力学、平衡分析与关节反力

#### 逆动力学

与平面系统（§6.4）流程完全相同：运动学求解 → 代数求解 λ → 计算反力

#### 关节反力公式（Eq. 11.5.6）

$$\mathbf{F}_i^{nk} = -\mathbf{C}_i^T\mathbf{A}_i^T\boldsymbol{\Phi}_{r_i}^{kT}\boldsymbol{\lambda}^k, \quad \mathbf{T}_i^{nk} = -\mathbf{C}_i^T(\boldsymbol{\Phi}_{\pi_i'}^{kT} + \tilde{\mathbf{s}}_i'^{PT}\mathbf{A}_i^T\boldsymbol{\Phi}_{r_i}^{kT})\boldsymbol{\lambda}^k$$

#### 平衡分析

与 §6.5 模式相同：动态趋近、直接求解、或最小势能法

### §11.6 数值方法

#### 两种积分策略

| 策略 | 方程 | 特点 |
|------|------|------|
| Euler 参数二阶 | Eq. 11.3.29 | 直接用 Ch.7 方法；$4\mathbf{G}^T\mathbf{J}'\mathbf{G}$ 坐标相关每步重算 |
| Newton-Euler + 重建 | Eq. 11.3.11 → Eq. 11.3.21 | $\mathbf{J}'$ 常量不变；(2,2) 子矩阵无需重算 |

DADS 软件采用混合算法：Euler 参数二阶时间导数形式，理论可靠且经广泛验证。

#### 一阶 DAE 形式（Eq. 11.5.7-11.5.8）

定义 $\mathbf{s} \equiv \dot{\mathbf{r}}$ 将系统转为一阶 DAE，附加 $\dot{\mathbf{r}} = \mathbf{s}$, $\dot{\mathbf{p}} = \frac{1}{2}\mathbf{G}^T\boldsymbol{\omega}'$ 和约束方程，可用直接数值积分求解。

---

## 工程应用与实例

| 图号/例题号 | 名称 | 类型 | 应用 | 关键知识点 |
|------------|------|------|------|-----------|
| Ex. 11.1.1, Fig. 11.1.2 | 单位球面上的摆 | 约束刚体动力学 | 球面约束 + Lagrange 乘子 | 约束方程变分 → 乘子引入方法 |
| Ex. 11.1.2, Fig. 11.1.4 | 绕 y 轴旋转的摆 | 一点固定旋转体 | 陀螺仪 | 惯性积对反力矩的影响 |
| Ex. 11.2.1, Fig. 11.2.2 | 均质楔形体质心 | 质心积分 | CAD 质量属性 | 三重积分求质心 |
| Ex. 11.2.2 | 楔形体惯性矩 | 平行轴定理 | CAD 惯性属性 | 对称面 → 惯性积为零 |
| Ex. 11.2.3, Fig. 11.2.4-5 | 三角形平板主轴 | 特征值问题 | 惯性矩阵对角化 | J'' → 质心 → J' → 特征值 → 主轴 |
| Ex. 11.2.4, Fig. 11.2.7 | 球端圆柱 | 复合体惯性 | 连杆/传动轴设计 | Table 11.2.1 + 平行轴定理 |
| Ex. 11.2.5, Fig. 11.2.8 | 带孔长方体 | 复合体（含空腔） | 机加工零件 | 空腔 = 负质量子构件 |
| Fig. 11.4.1 | TSDA | 力元 | 悬架弹簧/减震器 | 虚功推导广义力；ℓ→0 奇异处理 |
| Fig. 11.4.2 | RSDA | 力元 | 铰链扭簧/旋转阻尼 | 只有角向广义力；累积角处理多圈 |
| Fig. 11.5.1 | 关节反力与反力矩 | 反力计算 | 关节强度校核 | 由 λ^k 和 Jacobian 直接计算 |

---

## 与全书的关系

| 关联章节 | 关系 |
|---------|------|
| Ch.6 (Planar Dynamics) | **直接对应**：本章是 Ch.6 的空间推广，核心结构完全平行（单体方程 → 约束方程 → 内力 → 逆动力学 → 反力 → 数值方法） |
| Ch.7 (Numerical Methods for Dynamics) | 数值积分方法直接用于 Eq. 11.3.29；独立广义坐标分区/混合算法 |
| Ch.9 (Spatial Cartesian Kinematics) | Euler 参数、G 矩阵、约束方程及 Jacobian 全部来自 Ch.9 |
| Ch.10 (Spatial Kinematic Modeling) | 空间建模技术（约束冗余处理、关节组合）为本章的前置条件 |
| Ch.8 (Planar Dynamic Modeling) | 平面建模经验可直接类推到空间系统 |
| Ch.12 (未来) | 空间动力学建模与仿真案例，将综合运用本章所有方程 |

### 本章核心公式速查

| 公式 | 编号 | 用途 |
|------|------|------|
| $\int \mathbf{s}'^P\,dm = 0$, $\boldsymbol{\rho}'' = \frac{1}{m}\int \mathbf{s}''^P\,dm$ | 11.1.13, 11.2.1 | 惯性属性 |
| $\mathbf{J}' = -\int \tilde{\mathbf{s}}'^P\tilde{\mathbf{s}}'^P\,dm$, $\mathbf{J}'' = -\int \tilde{\mathbf{s}}''^P\tilde{\mathbf{s}}''^P\,dm$ | 11.1.17, 11.2.4 | 惯性矩阵定义 |
| $\mathbf{J}'' = \mathbf{C}^T\mathbf{J}'\mathbf{C} + m(\boldsymbol{\rho}''^T\boldsymbol{\rho}''\mathbf{I} - \boldsymbol{\rho}''\boldsymbol{\rho}''^T)$ | 11.2.7 | 惯性矩阵变换 |
| Newton-Euler 系统加速度方程 | 11.3.11 | 一阶混合 DAE |
| Euler 参数系统加速度方程 | 11.3.29 | 二阶 DAE |
| $\mathbf{F}_i^{nk}, \mathbf{T}_i^{nk}$ | 11.5.6 | 关节反力 |
