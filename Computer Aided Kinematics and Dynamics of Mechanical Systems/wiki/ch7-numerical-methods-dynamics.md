---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 7
title: "Numerical Methods in Dynamics"
pages: 243-281
sections:
  - "7.1 Organization of Computations"
  - "7.2 Solution of Mixed Differential-Algebraic Equations of Motion"
  - "7.3 Algorithms for Solving Differential-Algebraic Equations"
  - "7.4 Numerical Integration of First-Order Initial-Value Problems"
  - "7.5 Numerical Methods for Equilibrium Analysis"
created: 2026-05-18
last_updated: 2026-05-18
---

# Chapter 7: Numerical Methods in Dynamics

> 本章是 Ch.6（动力学理论推导）与 Ch.8（动力学应用案例）之间的桥梁，回答"Ch.6 推导出的混合微分-代数方程（DAE）如何用计算机数值求解"。首先介绍 DADS 动力学分析程序的计算组织（§7.1）；然后分析 DAE 的数学性质，给出理论上将 DAE 约化为 ODE 的坐标分区方法及其存在唯一性证明（§7.2）；接着介绍四种实用的 DAE 数值求解算法——广义坐标分区、直接积分、Baumgarte 约束稳定化和混合算法（§7.3）；再详细推导 Adams-Bashforth 预测器和 Adams-Moulton 校正器组成的 PECE 积分方法（§7.4）；最后讨论平衡分析的三种数值方法（§7.5）。

## 章节定位

| 维度 | 说明 |
|------|------|
| **前置** | Ch.4 运动学数值方法（Newton-Raphson、坐标分区、装配分析），Ch.6 约束动力学方程（Eq. 6.3.18 DAE） |
| **本章** | §7.1 计算组织 → §7.2 DAE 性质与理论约化 → §7.3 DAE 求解算法 → §7.4 ODE 数值积分 → §7.5 平衡分析 |
| **后续** | Ch.8 动力学建模应用案例 |

## 概念定义

### §7.1 计算组织

（§7.1 无独立概念定义，内容为 DADS 程序架构描述，见核心论点部分。）

### §7.2 混合微分-代数运动方程

**Mixed Differential-Algebraic Equations of Motion（混合微分-代数运动方程）** [p.248]
> The differential and algebraic equations of Eqs. 7.2.1 to 7.2.3 comprise the *mixed differential-algebraic equations of motion*.
>
> 方程 7.2.1（加速度级动力学方程）、7.2.2（位置约束）和 7.2.3（速度约束）共同构成**混合微分-代数运动方程**。这不是纯 ODE，也不是纯代数方程，而是两者的耦合。直到 1981 年 [39] 才被充分认识到这类方程**不能当作普通微分方程来处理**。

---

**Independent / Dependent Generalized Coordinates（独立/从属广义坐标）** [p.249]
> Therefore, **v** is interpreted as a vector of *independent generalized coordinates* and **u** is a vector of *dependent generalized coordinates*.
>
> 通过对约束 Jacobian $\Phi_\mathbf{q}$ 做高斯消元（Eq. 4.4.8 形式），将广义坐标 $\mathbf{q}$ 分为**独立坐标 $\mathbf{v}$**（其虚位移可自由选取，维度 = DOF）和**从属坐标 $\mathbf{u}$**（由约束方程和 $\mathbf{v}$ 唯一确定）。

---

**Kinematically Admissible Virtual Velocities（运动学容许虚速度）** [p.252]
> Observe that *kinematically admissible virtual velocities* $\delta\dot{\mathbf{q}} = [\delta\dot{\mathbf{u}}^T, \delta\dot{\mathbf{v}}^T]^T$ satisfy... $\Phi_\mathbf{u}\delta\dot{\mathbf{u}} + \Phi_\mathbf{v}\delta\dot{\mathbf{v}} = \mathbf{0}$.
>
> 满足约束速度方程（时间固定）的虚速度。用于证明约化质量矩阵 $\hat{\mathbf{M}}^v$ 正定性，从而保证 ODE 解的存在唯一性。

### §7.3 DAE 求解算法

**Generalized Coordinate Partitioning Algorithm（广义坐标分区算法）** [p.255-256]
> A computational implementation of this approach, called the *generalized coordinate partitioning algorithm*, may be carried out as follows...
>
> 将 §7.2 的理论约化**以隐式数值方式实现**的算法。不显式构造约化后的 ODE（Eq. 7.2.14），而是直接求解原始 DAE（Eq. 7.2.1）中的 $\ddot{\mathbf{q}}$ 和 $\boldsymbol{\lambda}$，然后仅提取独立分量 $\ddot{\mathbf{v}}$ 进行积分。从属坐标 $\mathbf{u}$ 通过 Newton-Raphson 求解约束方程精确恢复。可靠、精确，约束满足到用户指定精度。

---

**Direct Integration Algorithm（直接积分算法）** [p.256-257]
> The direct integration algorithm is simple, easy to implement, and computationally fast. It suffers, however, from a lack of error control on the constraints.
>
> 直接对 Eq. 7.2.1 求解 $\ddot{\mathbf{q}}$，然后积分**所有**广义坐标。简单高效但**完全没有约束满足性保障**，约束误差随时间积累（constraint drift）。

---

**Constraint Stabilization / Baumgarte Method（约束稳定化 / Baumgarte 方法）** [p.257]
> Baumgarte [40] observed, however, that the modified acceleration equation $\ddot{\Phi} + 2\alpha\dot{\Phi} + \beta^2\Phi = 0$ ... is stable.
>
> 将约束的二阶导数 $\ddot{\Phi} = \mathbf{0}$（数值不稳定）替换为阻尼振荡方程 $\ddot{\Phi} + 2\alpha\dot{\Phi} + \beta^2\Phi = \mathbf{0}$（Eq. 7.3.7），使 $\Phi$ 和 $\dot{\Phi}$ 渐近收敛到零。实现上只需在 Eq. 7.2.1 中将 $\boldsymbol{\gamma}$ 替换为 $\hat{\boldsymbol{\gamma}}$（Eq. 7.3.8）。比直接积分更稳定，计算量基本相同。缺点：无通用的 $\alpha$、$\beta$ 选取方法，奇异构型附近可能发散。

---

**Hybrid Algorithm（混合算法）** [p.258]
> A hybrid algorithm has been developed by Park [42] to take advantage of the better features of both methods.
>
> **DADS 采用的算法**。结合坐标分区的可靠性和约束稳定化的效率：正常时使用 Baumgarte 项抑制小幅约束振荡（高效路径 5a），约束误差超限时启动坐标分区校正（可靠路径 5b），奇异构型附近自动退化为纯坐标分区。

### §7.4 数值积分

**Initial-Value Problem（初值问题）** [p.254]
> The combination of the differential equation of Eq. 7.3.3 and initial conditions of Eq. 7.3.4 is an *initial-value problem*.
>
> 微分方程 $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, t)$ 与初始条件 $\mathbf{x}(t_0) = \mathbf{x}^0$ 的组合。

---

**Newton Backward Difference Polynomial（Newton 后向差分多项式）** [p.261-262]
> With equally spaced grid points $t_i - t_{i-1} = h$, this polynomial is constructed in the form of a *Newton backward difference polynomial*.
>
> $P_k(t) = f_n + \sum_{i=1}^{k-1} \frac{\nabla^i f_n}{i!\,h^i} \prod_{j=0}^{i-1}(t - t_{n-j})$（Eq. 7.4.4）。使用等距网格上的 $k$ 个历史函数值通过后向差分递推构造。

---

**Adams-Bashforth Predictor（Adams-Bashforth 预测公式）** [p.266]
> The result is called the *Adams-Bashforth formula of order $k$*.
>
> $\mathbf{x}_{n+1}^p = \mathbf{x}_n + h\sum_{i=1}^{k}\gamma_{i-1}\nabla^{i-1}\mathbf{f}_n$（Eq. 7.4.11）。**显式多步法**：$\mathbf{x}_{n+1}^p$ 完全由已知的 $\mathbf{f}_n, \mathbf{f}_{n-1}, \ldots$ 确定。$k=1$ 时退化为 Euler 方法。

---

**Adams-Moulton Corrector（Adams-Moulton 校正公式）** [p.272]
> The backward difference form of Eq. 7.4.14, derived in exactly the same way as Eq. 7.4.11, yields the *Adams-Moulton corrector of order $k+1$*.
>
> $\mathbf{x}_{n+1}^c = \mathbf{x}_n + h\sum_{i=1}^{k+1}\gamma_{i-1}^*\nabla^{i-1}\mathbf{f}_{n+1}^p$（Eq. 7.4.15）。利用预测步结果 $\mathbf{f}_{n+1}^p$ 作为额外插值点，获得更高阶更精确的近似。

---

**PECE Method（预测-求值-校正-求值方法）** [p.274]
> The kind of predictor-corrector procedure presented here is called a *PECE method*: Predict $\mathbf{x}_{n+1}^p$, Evaluate $\mathbf{f}_{n+1}^p$, Correct $\mathbf{x}_{n+1}^c$, Evaluate $\mathbf{f}_{n+1}$.
>
> 每步两次函数求值。最佳配对：$k$ 阶 Adams-Bashforth + $(k+1)$ 阶 Adams-Moulton。

---

**Local Truncation Error（局部截断误差）** [p.267]
> One source of error is due to approximating $\mathbf{x}^{(1)}(t)$ by an interpolating polynomial, known as *local truncation error*.
>
> 预测器：$\boldsymbol{\tau}_{n+1}^p \approx h\gamma_k\nabla^k\mathbf{f}_n$（Eq. 7.4.13）。校正器：$\boldsymbol{\tau}_{n+1}^c \approx h\gamma_{k+1}^*\nabla^{k+1}\mathbf{f}_{n+1}^p$（Eq. 7.4.16）。均可在运算中用后向差分在线估计，用于自适应步长和阶次控制。

### §7.5 平衡分析

**Dynamic Settling（动力学沉降法）** [p.277]
> The most universal method for finding a stable equilibrium configuration... is to integrate the equations of motion until $\dot{\mathbf{q}} = \ddot{\mathbf{q}} = \mathbf{0}$.
>
> 给系统加人工阻尼并积分运动方程，等待系统"沉降"到静平衡。通用但计算昂贵。

---

**Minimum Total Potential Energy（最小总势能原理）** [p.278]
> A conservative system is in a state of stable equilibrium if and only if the total potential energy is at a strict relative minimum.
>
> 保守系统稳定平衡的充要条件。$V(\mathbf{q}_e) < V(\mathbf{q})$ 对邻域内所有满足约束的 $\mathbf{q} \neq \mathbf{q}_e$ 成立。

---

**Influence Coefficient Matrix（影响系数矩阵）** [p.280]
> $\mathbf{H} = -\Phi_\mathbf{u}^{-1}\Phi_\mathbf{v}$（Eq. 7.5.17），so that $d\mathbf{u} = \mathbf{H}\,d\mathbf{v}$.
>
> 将约束微分 $d\Phi = \mathbf{0}$ 化为从属坐标变化量关于独立坐标变化量的线性映射。用于将约束最小化转化为无约束最小化。

## 符号定义

### DAE 系统（§7.2）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{M}$ | 矩阵 $nc \times nc$ | 系统质量矩阵 |
| $\Phi_\mathbf{q}$ | 矩阵 $nh \times nc$ | 约束 Jacobian |
| $\ddot{\mathbf{q}}$ | 向量 $nc \times 1$ | 广义加速度 |
| $\boldsymbol{\lambda}$ | 向量 $nh \times 1$ | Lagrange 乘子 |
| $\mathbf{Q}^A$ | 向量 $nc \times 1$ | 广义外力 |
| $\boldsymbol{\gamma}$ | 向量 $nh \times 1$ | 加速度方程右端项 |
| $\boldsymbol{\nu}$ | 向量 $nh \times 1$ | 速度方程右端项 |

### 坐标分区（§7.2）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{u}$ | 向量 $nh \times 1$ | 从属广义坐标 |
| $\mathbf{v}$ | 向量 $(nc-nh) \times 1$ | 独立广义坐标（DOF 维） |
| $\Phi_\mathbf{u}$ | 矩阵 $nh \times nh$ | 约束 Jacobian 对从属坐标的子矩阵（非奇异） |
| $\Phi_\mathbf{v}$ | 矩阵 $nh \times (nc-nh)$ | 约束 Jacobian 对独立坐标的子矩阵 |
| $\hat{\mathbf{M}}^v$ | 矩阵 $(nc-nh) \times (nc-nh)$ | 约化质量矩阵（Eq. 7.2.15），正定 |
| $\hat{\mathbf{Q}}^v$ | 向量 $(nc-nh) \times 1$ | 约化广义力（Eq. 7.2.16） |

### 约束稳定化（§7.3.4）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\alpha$ | 标量 > 0 | Baumgarte 阻尼参数 |
| $\beta$ | 标量 ≠ 0 | Baumgarte 频率参数 |
| $\hat{\boldsymbol{\gamma}}$ | 向量 | 修改后的右端项 $= \boldsymbol{\gamma} - 2\alpha(\Phi_\mathbf{q}\dot{\mathbf{q}} + \Phi_t) - \beta^2\Phi$（Eq. 7.3.8） |

### 数值积分（§7.4）

| 符号 | 类型 | 含义 |
|------|------|------|
| $h$ | 标量 | 时间步长 |
| $t_n$ | 标量 | 第 $n$ 个时间网格点 $= t_0 + nh$ |
| $\mathbf{x}_n$ | 向量 | 在 $t_n$ 处的数值近似解 |
| $\mathbf{f}_n$ | 向量 | $= \mathbf{f}(\mathbf{x}_n, t_n)$ |
| $\nabla^i f_n$ | 标量/向量 | 第 $i$ 阶后向差分 |
| $\gamma_i$ | 标量常数 | Adams-Bashforth 系数 |
| $\gamma_i^*$ | 标量常数 | Adams-Moulton 系数 |
| $\mathbf{x}_{n+1}^p$ | 向量 | Adams-Bashforth 预测值 |
| $\mathbf{x}_{n+1}^c$ | 向量 | Adams-Moulton 校正值 |
| $\boldsymbol{\tau}_{n+1}^p$ | 向量 | 预测器局部截断误差 |
| $\boldsymbol{\tau}_{n+1}^c$ | 向量 | 校正器局部截断误差 |
| $\varepsilon$ | 标量 | 误差容差 |

**Adams-Bashforth 系数**（Table 7.4.4）：$\gamma_0=1$, $\gamma_1=\frac{1}{2}$, $\gamma_2=\frac{5}{12}$, $\gamma_3=\frac{3}{8}$, $\gamma_4=\frac{251}{720}$, $\gamma_5=\frac{95}{288}$

**Adams-Moulton 系数**（Table 7.4.10）：$\gamma_0^*=1$, $\gamma_1^*=-\frac{1}{2}$, $\gamma_2^*=-\frac{1}{12}$, $\gamma_3^*=-\frac{1}{24}$, $\gamma_4^*=-\frac{19}{720}$, $\gamma_5^*=-\frac{3}{160}$

### 平衡分析（§7.5）

| 符号 | 类型 | 含义 |
|------|------|------|
| $V(\mathbf{q})$ | 标量函数 | 系统总势能 $= V_\mathbf{F} + V_f + V_\tau$ |
| $V_\mathbf{F}$ | 标量函数 | 常力势能 $= -\mathbf{F}^T\mathbf{r}^P$（Eq. 7.5.7） |
| $V_f$ | 标量函数 | 弹簧势能 $= \frac{k}{2}(\ell-\ell_0)^2 + \int F(\ell)\,d\ell$（Eq. 7.5.11） |
| $V_\tau$ | 标量函数 | 扭簧势能 $= \frac{k_\theta}{2}(\theta-\theta_0)^2 + \int T(\theta)\,d\theta$（Eq. 7.5.12） |
| $\mathbf{H}$ | 矩阵 | 影响系数矩阵 $= -\Phi_\mathbf{u}^{-1}\Phi_\mathbf{v}$（Eq. 7.5.17） |

## 核心论点

### §7.1 Organization of Computations

DADS 动力学分析程序继承运动学分析程序架构，分为**三段**（Fig. 7.1.1）：

1. **预处理器**：运动学数据 + 惯性/力/弹簧-阻尼器/初始条件/分析模式/输出选项
2. **动力学分析程序**：构建方程矩阵、装配系统、识别冗余约束、执行分析
3. **后处理器**：打印/绘图/动画

内部采用**三层结构**（Fig. 7.1.2）：ANALYSIS → JUNCTION → MODULES，与运动学共用同一模块集，力元模块是唯一新增。

Fig. 7.1.3 展示五阶段详细流程：输入数据读取 → 模型装配与可行性分析 → 平衡分析 → 动力学分析 → 逆动力学分析。

### §7.2 Solution of Mixed Differential-Algebraic Equations of Motion

#### DAE 的完整形式

$$\begin{bmatrix} \mathbf{M} & \Phi_\mathbf{q}^T \\ \Phi_\mathbf{q} & \mathbf{0} \end{bmatrix} \begin{bmatrix} \ddot{\mathbf{q}} \\ \boldsymbol{\lambda} \end{bmatrix} = \begin{bmatrix} \mathbf{Q}^A \\ \boldsymbol{\gamma} \end{bmatrix} \tag{7.2.1}$$

加上约束方程 $\Phi(\mathbf{q}, t) = \mathbf{0}$（7.2.2）和速度方程 $\Phi_\mathbf{q}\dot{\mathbf{q}} = \boldsymbol{\nu}$（7.2.3）。

#### 理论约化：DAE → ODE

通过高斯消元识别独立坐标 $\mathbf{v}$ 和从属坐标 $\mathbf{u}$，利用：
- $\dot{\mathbf{u}} = \Phi_\mathbf{u}^{-1}[\boldsymbol{\nu} - \Phi_\mathbf{v}\dot{\mathbf{v}}]$（7.2.11）
- $\ddot{\mathbf{u}} = \Phi_\mathbf{u}^{-1}[\boldsymbol{\gamma} - \Phi_\mathbf{v}\ddot{\mathbf{v}}]$（7.2.12）

得到**仅含独立坐标的纯 ODE**：

$$\hat{\mathbf{M}}^v\ddot{\mathbf{v}} = \hat{\mathbf{Q}}^v \tag{7.2.14}$$

$\hat{\mathbf{M}}^v$ 正定性通过 $\delta\dot{\mathbf{v}}^T\hat{\mathbf{M}}^v\delta\dot{\mathbf{v}} = \delta\dot{\mathbf{q}}^T\mathbf{M}\,\delta\dot{\mathbf{q}} > 0$（Eq. 7.2.18）证明。

**警告**：显式约化仅对最简单系统可行（Example 7.2.1 简单摆）。即使曲柄滑块机构也已不实际。实际计算必须用 §7.3 的数值算法。

### §7.3 Algorithms for Solving Differential-Algebraic Equations

四种算法的核心对比：

| 算法 | 约束满足 | 效率 | 稳定性 | 适用性 |
|------|---------|------|--------|--------|
| **坐标分区**（§7.3.2） | ✅ 精确（Newton-Raphson） | 中等（需迭代） | ✅ 可靠 | 通用 |
| **直接积分**（§7.3.3） | ❌ 漂移 | ✅ 最快 | ❌ 不稳定 | 短时间/温和动力学 |
| **Baumgarte 稳定化**（§7.3.4） | ⚠️ 渐近（$\alpha$,$\beta$ 依赖） | ✅ 快 | ⚠️ 奇异处可能发散 | 一般情况 |
| **混合算法**（§7.3.5） | ✅ 精确 + 渐近 | ✅ 快（大部分走稳定化路径） | ✅ 最可靠 | **DADS 采用** |

**混合算法**是最佳选择：正常时走高效的稳定化路径（5a），约束超限时启动可靠的坐标分区校正（5b），奇异处自动退化为纯坐标分区。

### §7.4 Numerical Integration of First-Order Initial-Value Problems

#### §7.4.1 多项式插值

| 方案 | 数据类型 | 适用性 |
|------|---------|--------|
| Taylor 多项式 | 单点多阶导数 | 理论基础，不适合通用积分 |
| Newton 后向差分多项式 | 多点函数值 | 实用，Adams 族的基础 |

#### §7.4.2 Adams-Bashforth Predictor

$$\mathbf{x}_{n+1}^p = \mathbf{x}_n + h\sum_{i=1}^{k}\gamma_{i-1}\nabla^{i-1}\mathbf{f}_n \tag{7.4.11}$$

**显式方法**，$k=1$ 即 Euler 法。自启动：从 $k=1$ 逐步升阶。

#### §7.4.3 Adams-Moulton Corrector

$$\mathbf{x}_{n+1}^c = \mathbf{x}_n + h\sum_{i=1}^{k+1}\gamma_{i-1}^*\nabla^{i-1}\mathbf{f}_{n+1}^p \tag{7.4.15}$$

利用预测值 $\mathbf{f}_{n+1}^p$ 构建更高阶插值。数值结果远优于纯预测器。

#### §7.4.4 PECE 实现

**每步流程**：Predict → Evaluate → Correct → Evaluate（2 次函数求值/步）。

**自适应控制**（倒车类比 Fig. 7.4.2）：
- $|\boldsymbol{\tau}_{n+1}^c| > \varepsilon$：减 $h$、降 $k$
- $|\boldsymbol{\tau}_{n+1}^c| \ll \varepsilon$：增 $h$、升 $k$

**推荐代码**：DE 子程序（Shampine & Gordon [36]）

### §7.5 Numerical Methods for Equilibrium Analysis

| 方法 | 适用性 | 优势 | 劣势 |
|------|--------|------|------|
| **Dynamic Settling** | 通用（含非保守力） | 最通用；选择稳定平衡 | 计算昂贵 |
| **直接求解 Eq. 7.5.2** | 理论可行 | — | ❌ 不推荐：病态、可能到不稳定平衡 |
| **最小总势能** | 保守系统 | 保证稳定平衡；$V_\mathbf{q}^T = -\mathbf{Q}^A$ 直接可用 | 仅限保守系统 |

**最小势能法**通过坐标分区转为无约束优化：

$$\text{minimize } V(\mathbf{v}), \quad \frac{dV^T}{d\mathbf{v}} = -\mathbf{H}^T\mathbf{Q}^{Au} - \mathbf{Q}^{Av} \tag{7.5.24}$$

用 Fletcher-Powell 算法求解，每步内用 Newton-Raphson 满足约束求 $\mathbf{u}$。

## 工程应用与实例

| 图号/例题号 | 名称 | 关键知识点 |
|------------|------|-----------|
| Fig. 7.1.1 | DADS 动力学计算流程 | 预处理器/分析程序/后处理器三段流 |
| Fig. 7.1.2 | DADS 动力学分析程序结构 | ANALYSIS-JUNCTION-MODULES 三层 |
| Fig. 7.1.3 | DADS 动力学分析详细流程 | 五阶段 ANALYSIS↔JUNCTION/MODULES 交互 |
| Fig. 7.4.1 | 通过 $k$ 点的插值 | Newton 后向差分多项式几何含义 |
| Fig. 7.4.2 | 倒车类比 | 步长/阶次自适应控制的直觉解释 |
| Example 7.2.1 | 简单摆显式约化 | $\mathbf{u}=[x_1,y_1]$, $v=\phi_1$, $(J'+m)\ddot{v}=-mg\cos v$ |
| Example 7.3.1 | 简单摆一阶化 | 二阶 ODE → 一阶 IVP |
| Example 7.4.1-7.4.2 | Taylor / Newton 差分逼近 $e^t$ | 两种插值方案的精度对比 |
| Example 7.4.3 | Euler 方法 | 最简积分，$h$ vs 精度的 trade-off |
| Example 7.4.4-7.4.5 | A-B / A-M 预测-校正 | 自启动 PECE 完整手算过程 |
| Tables 7.4.6-7.4.12 | 数值结果汇总 | $k$ 和 $h$ 对精度的系统性影响 |

## 与全书的关系

- **Ch.4 → Ch.7**：Ch.4 的坐标分区技术（§4.4）在 Ch.7 中被重用于 DAE→ODE 约化和平衡分析
- **Ch.6 → Ch.7**：Ch.6 推导的 DAE（Eq. 6.3.18）在 Ch.7 中被数值求解
- **Ch.7 → Ch.8**：Ch.7 提供的算法将在 Ch.8 的实际动力学建模案例中被应用
- **核心线索**：全书的核心计算路径为 建模 → 约束方程 → DAE → 坐标分区 → ODE → Adams PECE 积分，Ch.7 完成了这条链路的最后两环
