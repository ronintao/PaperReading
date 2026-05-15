---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 4
title: "Numerical Methods in Kinematics"
pages: 118-152
sections:
  - "4.1 Organization of Computations"
  - "4.2 Evaluation of Constraint Equations and Jacobian"
  - "4.3 Assembly of a System"
  - "4.4 Linear Equation Solution and Matrix Factorization"
  - "4.5 Newton-Raphson Method for Nonlinear Equations"
  - "4.6 Detection and Elimination of Redundant Constraints"
created: 2025-07-27
last_updated: 2025-07-27
---

# Chapter 4: Numerical Methods in Kinematics

## 章节定位

第四章是全书从**理论到实现的桥梁**（pp.118-152），将第3章建立的约束方程库和运动学三级分析框架转化为可计算的数值流程。内容包括：DADS 代码的三层计算架构（§4.1）、约束方程和 Jacobian 的稀疏评估与存储（§4.2）、系统装配的最小化方法（§4.3）、线性方程求解的高斯消元和 LU 分解（§4.4）、Newton-Raphson 非线性方程求解（§4.5）、冗余约束的自动检测与消除（§4.6）。本章为第5章（三维运动学）和第8-10章（动力学数值方法）提供所有计算基础设施。前置知识为第3章的约束方程和 Jacobian 构造。

---

## 概念定义

**Kinematic Analysis (Computer-Aided)（计算机辅助运动学分析）** [p.118]
> The governing equations of kinematics developed in Chapter 3 may be assembled and solved to determine the position, velocity, and acceleration of a system, provided adequate driving conditions are specified. Numerical methods that permit both computer assembly and solution of kinematic equations are presented in this chapter.
>
> 第3章建立的运动学方程可被组装和求解，以确定系统的位置、速度和加速度（需指定充分的驱动条件）。本章介绍允许计算机组装和求解运动学方程的数值方法。

---

**Four Modes of Kinematic Computation（运动学计算的四种模式）** [p.118]
> Four distinct modes of kinematic computation are considered: (1) assembly analysis, (2) position analysis, (3) velocity analysis, (4) acceleration analysis.
>
> 四种运动学计算模式：(1) 装配分析——仅给定估计值确定装配构型；(2) 位置分析——从已知装配构型出发逐时间步求解；(3) 速度分析；(4) 加速度分析。

---

**Preprocessor（预处理器）** [p.119]
> Logic is programmed into the preprocessor to permit the user to enter body names or numbers and define types of joints that connect pairs of bodies.
>
> 预处理器允许用户输入刚体名称/编号和定义连接刚体对的关节类型，从而定义运动学系统的结构。

---

**Analysis Program（分析主程序）** [p.121]
> An analysis program that controls the process of kinematic analysis.
>
> 控制运动学分析过程的主程序。

---

**Junction Subroutine（连接子程序）** [p.121]
> A junction program that assigns tasks to a set of computation modules (subroutines).
>
> 将任务分配给一组计算模块（子程序）的连接程序。

---

**Computation Modules（计算模块）** [p.121]
> A library of modules associated with bodies and joint types that are supported by the formulation.
>
> 与公式化方法所支持的刚体和关节类型相关联的模块库。

---

**Flags（分析阶段标志）** [p.121]
> The analysis program use flags (integers) to define the phase of analysis that is being carried out and passes instructions to the junction subroutine.
>
> 分析程序使用标志（整数）来定义当前执行的分析阶段，并向连接子程序传递指令。

---

**Nonzero Entry Scheme（非零条目方案）** [p.124]
> A vector of nonzero Jacobian entries is evaluated and sent, along with row and column indexes (pointers), to a subroutine for matrix factoring.
>
> 评估非零 Jacobian 条目向量，连同行列索引（指针），发送给矩阵分解子程序。

---

**Assembly of a System（系统装配）** [p.127]
> The determination of an assembled configuration of a system, given only estimates for the position and orientation of each component. It differs from position analysis in that a good estimate of the assembled configuration may not be available.
>
> 仅给定各构件位置和方向的估计值，确定系统的装配构型。与位置分析的区别在于可能没有好的初始估计。

---

**Assembly Minimization（装配最小化）** [p.130]
> The basic idea employed is to minimize error in satisfying the constraint equations, to find a solution that is as near as possible to the initial estimate $\mathbf{q}^0$.
>
> 基本思想是最小化约束方程的误差，找到尽可能接近初始估计 $\mathbf{q}^0$ 的解。

---

**Conjugate Gradient Minimization Algorithm（共轭梯度最小化算法）** [p.131]
> A method that is well suited for minimizing the function of Eq. 4.3.2 for large-scale systems is the conjugate gradient minimization algorithm of nonlinear programming (Fletcher and Powell).
>
> 适用于大规模系统的最小化方法——共轭梯度最小化算法（Fletcher-Powell 方法）。

---

**Gaussian Elimination（高斯消元法）** [p.133]
> Gaussian elimination is based on the elementary idea of eliminating variables one at a time. It consists of two major steps, forward elimination and back substitution.
>
> 基于逐个消去变量的基本思想，由前向消元和回代两个主要步骤组成。

---

**Row Pivoting（行选主元）** [p.134-135]
> In the $j$th forward-elimination step, the equation with the largest coefficient (in absolute value) of $x_j$ on or below the diagonal is chosen and interchanged with the $j$th row. This amounts simply to interchanging the order of equations.
>
> 在第 $j$ 步消元中，选择对角线及以下行中 $|a_{kj}|$ 最大的行作为主行并交换。

---

**Full Pivoting（全选主元）** [p.136]
> Full pivoting is the selection of the largest element from among the diagonal and all elements below and to the right as the pivot. Both row and column interchanges are required.
>
> 在对角线及其右下方所有元素中选最大者作为主元，需要行列交换。

---

**Dependent and Independent Variables（从属变量与独立变量）** [p.138]
> $\mathbf{v}$ may be treated as a vector of independent variables and $\mathbf{u}$ as a vector of dependent variables. The variable $\mathbf{x}$ is said to be partitioned into independent and dependent coordinates.
>
> $\mathbf{v}$ 为独立变量，$\mathbf{u}$ 为从属变量。变量 $\mathbf{x}$ 被划分为独立坐标和从属坐标。

---

**Ill-Conditioned Matrix（病态矩阵）** [p.140]
> When the bottom right factors in the coefficient matrix are nearly zero, but not to within round-off error, the coefficient matrix is said to be ill-conditioned, and severe numerical difficulties may be encountered.
>
> 当消元后底部右侧块的元素接近零但不在舍入误差范围内时，称矩阵为病态的。

---

**L-U Factorization（LU 分解）** [p.140]
> Given any nonsingular matrix $\mathbf{A}$, there exists an upper triangular matrix $\mathbf{U}$ with nonzero diagonal elements and a lower triangular matrix $\mathbf{L}$ with unit diagonal elements, such that $\mathbf{A} = \mathbf{LU}$.
>
> 对任意非奇异矩阵 $\mathbf{A}$，存在 $\mathbf{L}$（下三角，对角线为1）和 $\mathbf{U}$（上三角），使得 $\mathbf{A} = \mathbf{LU}$。

---

**Crout's Method（Crout 方法）** [p.141]
> Crout's method calculates elements of $\mathbf{L}$ and $\mathbf{U}$ recursively. An auxiliary matrix $\mathbf{B}$ can be defined to store both $\mathbf{L}$ and $\mathbf{U}$ elements in-place.
>
> Crout 方法递归计算 $\mathbf{L}$ 和 $\mathbf{U}$ 的元素，可原地存储（覆盖原矩阵 $\mathbf{A}$）。

---

**Quadratic Convergence（二次收敛）** [p.144]
> If the algorithm converges and the Jacobian is nonsingular, it is quadratically convergent; that is, there is a constant $c$ such that $|q^{(k+1)} - q^*| < c|q^{(k)} - q^*|^2$.
>
> 若算法收敛且 Jacobian 非奇异，则为二次收敛：误差的下一步值以当前误差的平方量级减小。

---

**Redundant Constraints（冗余约束）** [p.147]
> If redundant constraint equations exist in the $nh$ kinematic constraint equations $\Phi^K(\mathbf{q}) = \mathbf{0}$, the number of system degrees of freedom is not $3nb - nh$.
>
> 若 $nh$ 个运动学约束中存在冗余约束，系统的自由度不等于 $3nb - nh$。

---

**Virtual Displacement（虚位移）** [p.147]
> A virtual displacement $\delta\mathbf{q}$ (a small variation in $\mathbf{q}$ with time held fixed) that satisfies the linearized constraint equations $\Phi_\mathbf{q}^K\delta\mathbf{q} = \mathbf{0}$.
>
> 虚位移：时间固定条件下 $\mathbf{q}$ 的微小变化，满足 $\Phi_\mathbf{q}^K\delta\mathbf{q} = \mathbf{0}$。

---

**Isolated Singular Point（孤立奇异点）** [p.150]
> A bifurcation point that has multiple solutions. By perturbing a few generalized coordinates and reassembling, if the Jacobian has increased row rank, the constraint is redundant only at an isolated singular point.
>
> 孤立奇异点：初始构型恰好处于分支点。通过扰动坐标并重新装配，若秩恢复，则仅为孤立奇异而非全局冗余。

---

## 符号定义

### §4.2 约束方程与 Jacobian 评估

| 符号 | 类型 | 含义 |
|------|------|------|
| $\Phi_\mathbf{q}^{(i+1)}$ | 矩阵 ($nh \times nc$) | 第 $(i+1)$ 次迭代处的约束 Jacobian |
| $\Delta\mathbf{q}^{(i)}$ | 向量 ($nc \times 1$) | 第 $i$ 次 Newton-Raphson 修正量 |
| $\Phi^{(i)}$ | 向量 ($nh \times 1$) | 第 $i$ 次迭代处的约束方程值 |
| $\boldsymbol{\nu} = -\Phi_t$ | 向量 | 速度方程右端项 |
| $\boldsymbol{\gamma}$ | 向量 | 加速度方程右端项 |
| ENTRY (1)~(8) | 标量 | 转动副约束的 8 个非零 Jacobian 条目（Eq. 4.2.5） |

### §4.3 系统装配

| 符号 | 类型 | 含义 |
|------|------|------|
| $\Phi^K(\mathbf{q})$ | 向量函数 | 运动学约束方程 |
| $\Phi^D(\mathbf{q}, t_0)$ | 向量函数 | 驱动约束方程（在 $t_0$ 时刻） |
| $\mathbf{q}^0$ | 向量 | 用户提供的装配构型初始估计 |
| $\mathbf{q}^a$ | 向量 | 装配后的解 |
| $\psi(\mathbf{q}, t_0, r)$ | 标量函数 | 装配最小化目标函数（Eq. 4.3.2） |
| $r$ | 标量，$> 0$ | 约束违反惩罚权重参数 |
| $\psi_\mathbf{q}$ | 向量 ($nc \times 1$) | 目标函数的梯度（Eq. 4.3.4） |
| $\mathbf{H}^{(i)}$ | 矩阵 ($nc \times nc$) | Hessian 逆的近似（初始为单位阵） |
| $\mathbf{s}^i$ | 向量 | 共轭搜索方向 |
| $\alpha^i$ | 标量 | 一维线搜索步长 |

### §4.4 线性方程求解与矩阵分解

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{A}$ | 矩阵 ($n \times n$ 或 $m \times n$) | 系数矩阵 |
| $\mathbf{x}$ | 向量 ($n \times 1$) | 未知数向量 |
| $\mathbf{b}$ | 向量 | 右端向量 |
| $a_{jj}^{(j-1)}$ | 标量 | 第 $j$ 步消元的主元 |
| $\mathbf{U}, \mathbf{R}, \hat{\mathbf{b}}$ | 矩阵/向量 | 非方阵消元后的分块（Eq. 4.4.8-4.4.9） |
| $\mathbf{u}$ | 向量 ($m \times 1$) | 从属变量 |
| $\mathbf{v}$ | 向量 ($n-m \times 1$) | 独立变量 |
| $r$ | 整数 | 矩阵行秩 |
| $\mathbf{L}$ | 矩阵，下三角 | LU 分解的下三角因子（单位对角线） |
| $\mathbf{U}$ | 矩阵，上三角 | LU 分解的上三角因子 |
| $\mathbf{B}$ | 矩阵 | Crout 辅助矩阵，同时存储 $\mathbf{L}$ 和 $\mathbf{U}$ |

### §4.5 Newton-Raphson

| 符号 | 类型 | 含义 |
|------|------|------|
| $\Phi(\mathbf{q})$ | 向量函数 ($n \times 1$) | $n$ 个非线性方程 |
| $\mathbf{q}^*$ | 向量 ($n \times 1$) | 精确解向量 |
| $\varepsilon_e$ | 标量 | 方程误差容差 |
| $\varepsilon_s$ | 标量 | 解误差容差 |
| $c$ | 常数 | 二次收敛常数 |

### §4.6 冗余约束检测与消除

| 符号 | 类型 | 含义 |
|------|------|------|
| $\Phi^{KI}(\mathbf{q})$ | 向量函数 ($nh' \times 1$) | 独立运动学约束 |
| $\Phi^{KR}$ | 向量函数 | 冗余运动学约束（消元后全零行） |
| $nh'$ | 整数 | 独立运动学约束数（= Jacobian 行秩） |
| $d = 3nb - nh'$ | 整数 | 系统真实自由度 |
| $\delta\mathbf{q}$ | 向量 | 虚位移 |
| $\Phi_\mathbf{u}^{KI}$ | 矩阵，上三角 | 消元后独立约束对从属变量的 Jacobian |
| $\Phi_\mathbf{v}^{KI}$ | 矩阵 | 消元后独立约束对独立变量的 Jacobian |

---

## 核心论点

### 引言：运动学计算的四种模式

第四章的核心主题是将 Ch.3 的运动学理论转化为可计算的数值流程。引言（p.118）指出：

1. **位置方程高度非线性**，变量众多（大型系统无法手写方程，更别说解析求解）
2. **速度和加速度方程为线性**，适合矩阵分解
3. 需要**计算机自动组装和求解**

四种计算模式的依赖关系：

```
Assembly Analysis (§4.3)     无好的初值，可能无解
        │ 成功
        ▼
Position Analysis (§4.5)     从已知构型出发，沿时间步推进
        │ 每步完成后
        ▼
Velocity Analysis (§3.6)     线性方程，同一 Jacobian
        │
        ▼
Acceleration Analysis (§3.6)  线性方程，同一 Jacobian
```

---

### §4.1 计算组织（DADS 架构）

DADS 代码的**三层架构**（Fig. 4.1.1, 4.1.2, 4.1.3）：

**顶层流程（Fig. 4.1.1）：**

| 层 | 功能 |
|---|---|
| **Preprocessor** | 输入刚体命名/编号、关节类型和连接关系、关节数据、几何外形、仿真时间/误差容差、输出格式 |
| **Kinematic Analysis Program** | 组装方程/声明不可行设计/识别冗余约束/执行位置-速度-加速度分析 |
| **Postprocessor** | 打印数值结果/绘制曲线/生成终端动画或录像 |

**分析程序内部结构（Fig. 4.1.2 ANALYSIS → JUNCTION → MODULES）：**

```
┌─────────────┐
│  ANALYSIS    │ 控制分析阶段、分配任务、传递结果
│  (主控制器)   │
└──────┬──────┘
       │ 通过 flags（整数）指示当前阶段
       ▼
┌─────────────┐
│  JUNCTION    │ 从各模块收集数据、组装成系统级数组
│  (数据组装器) │
└──────┬──────┘
       │ 调用对应的体/关节模块
       ▼
┌─────────────┐
│  MODULES     │ 评估体信息、关节方程/Jacobian、速度/加速度右端项
│  (模块库)    │
└─────────────┘
```

**详细五阶段流程（Fig. 4.1.3）：**

| 阶段 | ANALYSIS 侧 | JUNCTION/MODULES 侧 |
|------|-------------|---------------------|
| **Input & Setup** | 读数据、分配模块任务、确定数组维度/地址 | 统计广义坐标数、统计并确定 Jacobian 非零条目地址 |
| **Assembly & Feasibility** | 分配模块任务、执行装配最小化、识别冗余约束 | 评估约束方程、评估 Jacobian |
| **Position Analysis** | 分配模块任务、迭代求解位置 | 评估约束方程、评估 Jacobian |
| **Velocity Analysis** | 分配模块任务、求解速度 | 评估 Jacobian、评估速度方程右端 $\nu$ |
| **Acceleration Analysis** | 分配模块任务、求解加速度 | 评估加速度方程右端 $\gamma$ |

**关键设计洞察**：速度和加速度分析阶段的 **Jacobian 是同一个**（在位置分析最后一次迭代时已计算好），Modules 在加速度阶段只需提供右端项 $\gamma$。

---

### §4.2 约束方程与 Jacobian 的评估

本节展示约束方程和 Jacobian 如何在代码中**以非零条目形式高效评估和存储**。

**运动学三级分析中的三个线性系统**：

- **Newton-Raphson 迭代**（Eq. 4.2.1）：$\Phi_\mathbf{q}^{(i+1)}\Delta\mathbf{q}^{(i)} = -\Phi^{(i)}$
- **速度方程**（Eq. 4.2.2）：$\Phi_\mathbf{q}\dot{\mathbf{q}} = -\Phi_t \equiv \boldsymbol{\nu}$
- **加速度方程**（Eq. 4.2.3）：$\Phi_\mathbf{q}\ddot{\mathbf{q}} = -[(\Phi_\mathbf{q}\dot{\mathbf{q}})_\mathbf{q}\dot{\mathbf{q}} + 2\Phi_{\mathbf{q}t}\dot{\mathbf{q}} + \Phi_{tt}] \equiv \boldsymbol{\gamma}$

**Jacobian 稀疏性——转动副示例**（Eq. 4.2.4-4.2.5, Fig. 4.2.1）：

转动副涉及两个刚体 $i$ 和 $j$，产生 2 行约束，每行 Jacobian 只在 6 列中可能非零，实际只有 8 个非零条目。对 15 体系统，每个转动副行仅约 10% 非零。

**四连杆 Jacobian**（Example 4.2.1, Eq. 4.2.6）：12×12 矩阵中只有 **34 个非零**（24%）。

**结论**：利用稀疏结构存储和操作 Jacobian 可显著节省内存和计算时间。

---

### §4.3 系统装配

**问题定义**：给定约束方程 $\Phi(\mathbf{q}, t_0) = 0$（Eq. 4.3.1）和初始估计 $\mathbf{q}^0$，找到装配构型 $\mathbf{q}^a$。

**Newton-Raphson 的三种行为**（Example 4.3.1，两体滑块-曲柄机构）：

| Case | 参数 | 行为 | 收敛速度 |
|------|------|------|---------|
| 1 | $t_0=0$, $q^{(0)}=2$ | 正常收敛（Jacobian 非奇异） | **二次收敛**（3次迭代） |
| 2 | $t_0=\pi/4$, $q^{(0)}=1$ | 收敛到奇异解 $q=\sqrt{2}/2$ | **仅线性收敛**（20+次迭代） |
| 3 | $t_0=3\pi/8$, $q^{(0)}=1$ | 无解，发散 | **永不收敛** |

**装配最小化方法**（当 Newton-Raphson 不可靠时）：

目标函数（Eq. 4.3.2）：

$$\psi(\mathbf{q}, t_0, r) = (\mathbf{q} - \mathbf{q}^0)^T(\mathbf{q} - \mathbf{q}^0) + r\Phi^T(\mathbf{q}, t_0)\Phi(\mathbf{q}, t_0)$$

- 第一项：最小化与初始估计的偏差（"就近"原则）
- 第二项：约束违反的惩罚，权重为 $r$
- **惩罚参数递增策略**：从较小 $r$ 开始逐步增大，最终 $\mathbf{q}^a = \lim_{r\to\infty}\mathbf{q}(r)$
- **梯度**（Eq. 4.3.4）只需 $\Phi$ 和 $\Phi_\mathbf{q}$——装配模式可直接**复用运动学分析的模块库**

**共轭梯度算法**（Fletcher-Powell，5 步）：初始化 → 搜索方向 → 线搜索 → 更新坐标和 Hessian 近似 → 收敛检查。

---

### §4.4 线性方程求解与矩阵分解

运动学分析的每个阶段最终都归结为线性方程组的求解：

| 运动学阶段 | 对应的线性方程 |
|-----------|-------------|
| 位置分析（每次 N-R 迭代） | $\Phi_\mathbf{q}\Delta\mathbf{q} = -\Phi$ |
| 速度分析 | $\Phi_\mathbf{q}\dot{\mathbf{q}} = \boldsymbol{\nu}$ |
| 加速度分析 | $\Phi_\mathbf{q}\ddot{\mathbf{q}} = \boldsymbol{\gamma}$ |

#### §4.4.1 高斯方法

**选主元策略对比**：

| 策略 | 行交换 | 列交换 | 数值稳定性 | 额外开销 |
|------|--------|--------|----------|---------|
| 无选主元 | 无 | 无 | 最差 | 无 |
| 行选主元 | 有 | 无 | 好 | 低 |
| 全选主元 | 有 | 有 | 最好 | 中等 |

**非方阵消元**（$m$ 方程，$n$ 未知数，$m < n$）：消元后变为 $\mathbf{Uu} + \mathbf{Rv} = \hat{\mathbf{b}}$（Eq. 4.4.8），自然划分出从属变量 $\mathbf{u}$ 和独立变量 $\mathbf{v}$。

**秩判定与相容性**：消元后全零行数 = $m - r$（秩缺）。相容条件：$\hat{\mathbf{b}}_{m-r} = \mathbf{0}$。

**关键洞察**——非方阵消元自然将广义坐标 $\mathbf{q}$ 划分为独立坐标和从属坐标，正是运动学自由度的代数表现。

#### §4.4.2 L-U 分解

$\mathbf{A} = \mathbf{LU}$（Eq. 4.4.13）将求解分为两步三角回代：

$$\mathbf{Ax} = \mathbf{b} \implies \underbrace{\mathbf{Ly} = \mathbf{b}}_{\text{前向回代}} + \underbrace{\mathbf{Ux} = \mathbf{y}}_{\text{后向回代}}$$

**Crout 方法**（Eq. 4.4.20）：递归原地分解，L 和 U 覆盖 A 的存储位置。

**对运动学的关键优势**：所有三个阶段共享同一个 Jacobian $\Phi_\mathbf{q}$。**一次 LU 分解，三次回代**分别求 $\Delta\mathbf{q}$（位置迭代）、$\dot{\mathbf{q}}$（速度）、$\ddot{\mathbf{q}}$（加速度）。

---

### §4.5 Newton-Raphson 方法

**单变量推导**（Eq. 4.5.3-4.5.5）：Taylor 展开 → 忽略高阶项 → 迭代公式 $q^{(i+1)} = q^{(i)} - \Phi(q^{(i)})/\Phi_q(q^{(i)})$

**二次收敛**（Eq. 4.5.6）：$|q^{(k+1)} - q^*| < c|q^{(k)} - q^*|^2$，前提是 Jacobian 非奇异。

**四种几何行为**：

| 图 | 情况 | 行为 |
|---|------|------|
| Fig. 4.5.1 | 正常（根非奇异） | 快速收敛 |
| Fig. 4.5.2 | 根在拐点 | 可能发散（切线交替跳跃） |
| Fig. 4.5.3 | 多个根 | 初值决定收敛到哪个根 |
| Fig. 4.5.4 | 局部极值附近 | 切线近水平 → 跳出很远 → 可能发散 |

**多变量推广**（Eq. 4.5.7-4.5.8）：

$$\Phi_\mathbf{q}(\mathbf{q}^{(i)})\Delta\mathbf{q}^{(i)} = -\Phi(\mathbf{q}^{(i)}), \quad \mathbf{q}^{(i+1)} = \mathbf{q}^{(i)} + \Delta\mathbf{q}^{(i)}$$

终止条件：所有 $|\Phi_k| \leq \varepsilon_e$ 且所有 $|q_k^{(i)} - q_k^{(i-1)}| \leq \varepsilon_s$。

**关键联系**：每次迭代归结为求解线性方程组 $\Phi_\mathbf{q}\Delta\mathbf{q} = -\Phi$——正是 §4.4 LU 分解的用武之地。

---

### §4.6 冗余约束的检测与消除

**问题**：用户建模时可能引入冗余约束，导致 Jacobian 秩亏。DADS 的解决方案是**分析前自动检测并消除**。

**两阶段检测**：

**阶段 1——运动学约束冗余**（步骤 1-4）：对 $\Phi_\mathbf{q}^K$ 做全选主元高斯消元，秩 $nh'$ = 非零行数，$\Phi^{KR}$（零行）为冗余。列交换确定独立/从属坐标。

**阶段 2——驱动约束冗余**（步骤 5-6）：追加驱动约束到独立运动学约束下方再做消元（限制列交换仅通过 $\Phi_\mathbf{q}^K$ 列），零行 = 冗余驱动约束。

**6 步冗余约束消除算法**：

```
1. 装配系统（§4.3 最小化方法）
2. 评估运动学 Jacobian Φ_q^K
3. 全选主元高斯消元 → 确定秩 nh'，消除冗余 Φ^KR
4. 报告独立坐标选择和 DOF = 3nb - nh' = d
5. 追加驱动约束，受限高斯消元 → 检测冗余驱动
6. 若 nh' + d' < nc → 告知用户需补充驱动约束
```

**Example 4.6.1**（四连杆平行四边形 + 距离约束）：
- **非奇异构型**（60°）：秩缺 1 → 距离约束冗余（真冗余）
- **展平构型**（0°）：秩缺 2 → 一个真冗余 + 一个孤立奇异点（扰动后秩恢复）

---

## 工程应用与实例

| 图号/例题号 | 名称 | 类型 | 关键知识点 |
|------------|------|------|-----------|
| Fig. 4.1.1 | DADS computational flow | 流程图 | Preprocessor → Analysis → Postprocessor |
| Fig. 4.1.2 | DADS kinematic analysis structure | 结构图 | ANALYSIS → JUNCTION → MODULES |
| Fig. 4.1.3 | DADS kinematic analysis flow | 详细流程图 | 五阶段 ANALYSIS/MODULES 分工 |
| Fig. 4.2.1 | Jacobian entries for revolute joint | 稀疏图 | 12 条目中仅 8 非零 |
| Ex. 4.2.1 + Fig. 4.2.2 | Four-bar mechanism | Jacobian 构造 | 12×12 矩阵仅 34 非零（24%） |
| Ex. 4.3.1 + Fig. 4.3.1 | Two-body slider-crank | N-R 行为 | 二次/线性/发散三种模式 |
| Table 4.3.1-4.3.3 | Slider-crank iteration results | 数值结果 | 三种收敛行为的完整数据 |
| Ex. 4.4.1 | 3×3 Gaussian elimination | 算例 | 前向消元 + 回代 |
| Ex. 4.4.2 | 4×4 with row pivoting | 算例 | 行选主元策略 |
| Ex. 4.4.3 | 3×3 with full pivoting | 算例 | 全选主元（行列交换） |
| Ex. 4.4.4 | 3×5 rank determination | 算例 | 非方阵消元 → 秩与变量划分 |
| Ex. 4.4.5 | 3×3 LU factorization | 算例 | Crout 原地分解 + 两步回代 |
| Fig. 4.5.1-4.5.4 | N-R geometric behavior | 概念图 | 正常收敛/拐点/多根/极值附近 |
| Ex. 4.6.1 + Fig. 4.6.1 | Parallelogram + distance constraint | 冗余检测 | 真冗余 vs 孤立奇异点 |

---

## 与全书的关系

**向前连接（本章使用的前置知识）：**
- Ch.3 §3.2-3.5：所有约束类型的 $\Phi$、$\Phi_\mathbf{q}$、$\boldsymbol{\nu}$、$\boldsymbol{\gamma}$ 表达式（本章 §4.2 直接调用）
- Ch.3 §3.6：位置/速度/加速度分析的理论框架（本章 §4.1 的 DADS 流程图直接实现之）
- Ch.3 §3.7：奇异构型的概念（本章 §4.6 的冗余约束检测直接处理之）

**向后连接（本章为后续章节提供的基础）：**
- Ch.5（三维运动学）：相同的计算架构和数值方法，扩展到空间坐标
- Ch.8-10（动力学）：Newton-Raphson、LU 分解、装配最小化等数值工具被复用于动力学方程求解
- Ch.5, Ch.10：装配最小化的大规模系统应用实例
