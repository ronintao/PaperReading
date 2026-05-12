---
type: source
id: intermediate-dynamics-haug
pdf_path: ../Related/IntermediateDynamics.pdf
url: https://doi.org/10.1017/9781009089494
tags:
  - multibody-dynamics
  - analytical-mechanics
  - textbook
  - year/1992-01
  - venue/Prentice-Hall
created: 2026-05-11
last_updated: 2026-05-12
authors:
  - Edward J. Haug
aliases:
  - Intermediate Dynamics
---

## Essence

> [!abstract]
> **One-Sentence Summarization**: 系统性建立了**多体系统约束动力学的变分方程和矩阵 DAE 表述**，在笛卡尔坐标下严格证明了约束反力通过约束 Jacobian 转置与 Lagrange 乘子相关联，并给出了解的存在唯一性定理。
> **Contribution**: 作为多体动力学领域的经典教科书，首次在教学体系中**完整推导了约束力 $F^C = -\Phi_r^T\lambda$ 的显式关系**（Eq. 3.2.9），明确指出约束力分量数多于 Lagrange 乘子分量数，两者并非直接相等，并给出了**约束动力学存在唯一性定理**（Constrained Dynamic Existence Theorem）在笛卡尔坐标和广义坐标下的证明。

## Factors

### Context

**多体系统动力学**需要同时处理运动方程和约束方程，形成微分-代数方程组（DAE）。核心困难在于：约束力作为未知量出现在运动方程中，需要与 Lagrange 乘子建立联系才能封闭求解。本书是 **Edward J. Haug** 在 Iowa 大学计算机辅助设计中心的研究成果系统化教学总结，面向机械工程和计算力学领域。

### Related Work

- **经典分析力学**（Lagrange, Hamilton）：建立了广义坐标和 Lagrange 方程框架，但对约束力的处理停留在消去阶段
- **D'Alembert 原理**：可直接计算约束力，但难以与系统化计算框架结合
- **Wittenburg, Nikravesh 等**：同期发展多体动力学计算方法，侧重于不同坐标选择和数值算法

### Gap

此前缺乏一个**从变分原理出发、系统性推导约束力与 Lagrange 乘子关系**的完整理论框架。教科书中通常直接引入 Lagrange 方程，而不深入讨论乘子的物理含义及其与实际约束力的精确关系。

### Proposal

本书采用**变分方程方法**，从虚功原理和 Lagrange 乘子定理出发，先在笛卡尔坐标下推导约束力表达式，再建立矩阵形式的约束运动方程（DAE），并证明了解的存在唯一性。进而将理论推广到广义坐标表述。

## Architecture

> [!info] 符号约定
> $\Phi$ 表示**约束方程本身**（向量值函数），下标表示求偏导：$\Phi_r = \frac{\partial \Phi}{\partial \mathbf{r}}$ 是约束的 **Jacobian 矩阵**，$\Phi_r^T$ 是其转置。二者的区别是理解约束力公式的关键——$F^C = -\Phi_r^T\lambda$ 中，$\Phi_r^T$ 将 $m$ 维乘子空间映射到 $3N$ 维物理力空间。

### 整体结构：约束力-乘子关系的推导逻辑

本书第 3 章 "Variational Methods for Dynamics of Systems Modeled as Particles" 是核心内容所在。推导分三个层次递进：

```
[Layer 1: 粒子对之间的约束力] (Sec. 3.2, Eqs. 3.2.1-3.2.9)
  Newton 第三定律: F_ij^C = -F_ji^C
  完整约束: Φ^ij(r_i, r_j, t) = 0
  虚功为零: δr_i^T F_ij^C + δr_j^T F_ji^C = 0  (Eq. 3.2.8)
  Lagrange 乘子定理:
    F_ij^C = -Φ_{r_i}^{ijT} λ^{ij}     (Eq. 3.2.9, holonomic)
    F_ij^C = -B^{ijT} μ^{ij}            (Eq. 3.2.10, differential)
         │
         ▼
[Layer 2: 系统级 Lagrange 乘子运动方程] (Sec. 3.2, Eq. 3.2.12)
  m_i r̈_i + Σ Φ_{r_i}^{ijT} λ^{ij} + Σ B^{ijT} μ^{ij} = F_i^A
         │
         ▼
[Layer 3: 矩阵 DAE 形式] (Sec. 3.4, Eqs. 3.4.4-3.4.7)
  笛卡尔坐标:
    M r̈ + Φ_r^T λ = F^A              (Eq. 3.4.4)
    [M   Φ_r^T] [r̈]   [F^A]
    [Φ_r   0  ] [λ ] = [γ  ]          (Eq. 3.4.7)
         │
         ▼
[Layer 4: 广义坐标推广] (Sec. 3.4, Eq. 3.4.15+)
  r = r(q) 参数化
  [M̂  Φ_q^T] [ĉ]   
  [Φ_q  0  ] [b̂] = 0                 (Eq. 3.4.22)
  + Constrained Dynamic Existence Theorem
```

### 约束力的 Lagrange 乘子表达（Eq. 3.2.9）

对于粒子 $i$ 和 $j$ 之间的完整约束 $\Phi^{ij}(\mathbf{r}_i, \mathbf{r}_j, t) = 0$，理想约束力不做虚功：

$$\delta\mathbf{r}_i^T \mathbf{F}_{ij}^C + \delta\mathbf{r}_j^T \mathbf{F}_{ji}^C = 0$$

由 Lagrange 乘子定理：

$$\mathbf{F}_{ij}^C = -\Phi_{\mathbf{r}_i}^{ijT} \boldsymbol{\lambda}^{ij}, \quad \mathbf{F}_{ji}^C = -\Phi_{\mathbf{r}_j}^{ijT} \boldsymbol{\lambda}^{ij}$$

> [!note] 为什么约束力分量数多于乘子分量数？
> 若粒子 $i$、$j$ 之间有 $k$ 个约束（$k=1$ 或 $2$），则 $\lambda^{ij}$ 只有 $k$ 个分量，但约束力 $\mathbf{F}_{ij}^C$ 有 3 个分量。**降维的原因**是 Eq. 3.2.9 强制约束力正交于约束面——这正是理想约束的物理含义。因此 **Lagrange 乘子不是约束力本身，而是约束力在约束法方向上的投影分量**。

### 矩阵 DAE 形式（Eq. 3.4.7）

将所有粒子的运动方程和约束方程组装为：

$$\begin{bmatrix} \mathbf{M} & \Phi_r^T \\ \Phi_r & \mathbf{0} \end{bmatrix} \begin{bmatrix} \ddot{\mathbf{r}} \\ \boldsymbol{\lambda} \end{bmatrix} = \begin{bmatrix} \mathbf{F}^A \\ \boldsymbol{\gamma} \end{bmatrix}$$

其中 $\mathbf{M} = \text{diag}(m_1\mathbf{I}, \ldots, m_{nb}\mathbf{I})$ 为质量矩阵，$\boldsymbol{\gamma}$ 为约束加速度方程右端项。

> [!note] 存在唯一性条件
> 当质量矩阵 $\mathbf{M}$ 正定且约束 Jacobian $\Phi_r$ 满秩时，系数矩阵非奇异，加速度 $\ddot{\mathbf{r}}$ 和 Lagrange 乘子 $\boldsymbol{\lambda}$ 的解**存在且唯一**。Haug 通过构造齐次方程 $\mathbf{Mc} + \mathbf{J}^T\mathbf{b} = 0$, $\mathbf{Jc} = 0$，利用 $\mathbf{M}$ 的正定性证明 $\mathbf{c} = 0$，再由 $\mathbf{J}$ 满秩得 $\mathbf{b} = 0$（Eqs. 3.4.12-3.4.14）。

### 广义坐标推广

当笛卡尔坐标通过 $\mathbf{r} = \mathbf{r}(\mathbf{q})$ 参数化为广义坐标时，**Constrained Dynamic Existence Theorem** 同样成立：

$$\begin{bmatrix} \hat{\mathbf{M}} & \Phi_q^T \\ \Phi_q & \mathbf{0} \end{bmatrix} \begin{bmatrix} \hat{\mathbf{c}} \\ \hat{\mathbf{b}} \end{bmatrix} = \mathbf{0}$$

条件是参数化 $\mathbf{r}(\mathbf{q})$ 非奇异且 $\Phi_q$ 或 $\mathbf{J}$ 满秩。

> [!note] 为什么 Haug 没有在广义坐标下给出约束力的显式表达？
> Haug 在笛卡尔坐标下建立了 $F^C = -\Phi_r^T\lambda$ 的关系，在广义坐标下给出了矩阵 DAE 形式，但**没有推导广义坐标下约束力与 $\lambda$ 的显式对应关系**。这正是 Yao & Ren (2010) 后续工作填补的空白——他们推导出 $F^C = -(r_q^T)^{-1}\phi_q^T\lambda$ 并给出了一一对应条件 $r_q = -\phi_q$。

## Evidence

本书作为教科书，通过多个算例验证理论：

| 算例 | 内容 | 关键结果 |
|------|------|---------|
| Example 3.2.1 | 哑铃模型（两质点+无质量杆） | 拉力约束力 $F^C = 2\lambda$（非 $\lambda$ 本身） |
| Example 3.4.1 | 简单摆（笛卡尔 DAE 形式） | 5×5 矩阵系统完整求解 $\ddot{x}, \ddot{y}, \ddot{z}, \lambda_1, \lambda_2$ |
| Example 3.4.3 | 轮轴系统（非完整约束） | 矩阵行列式 $-m^2 \neq 0$，始终非奇异 |

哑铃算例（Example 3.2.1）直接证明了 **$\lambda$ 不等于约束力**：单位长度杆的拉力是 $2\lambda$ 而非 $\lambda$，因为约束 Jacobian 的元素为 $2(r_2 - r_1)$。

## Critical Analysis

### Novel Insight

- **Insight**: **约束力的维度低于物理力的维度**——$k$ 个约束只产生 $k$ 个乘子分量，但对应 3 个力分量
  - *Prior*: 经典力学教学中通常将约束力与乘子等同，或回避两者关系的精确讨论
  - *Update*: Haug 明确了**降维源于理想约束的正交性**——约束力被约束 Jacobian 转置限制在约束法方向上

- **Insight**: 矩阵 DAE 形式 (Eq. 3.4.7) 将约束多体动力学统一为**标准线性代数问题**
  - *Prior*: 约束力的求解依赖于针对具体问题的 D'Alembert 原理推导
  - *Update*: **任何约束系统**都可组装为统一的鞍点矩阵系统，直接数值求解

### Fundamental Limitations

- **Limitation**: **仅建立了笛卡尔坐标下约束力与乘子的显式关系**
  - *Root cause*: 在广义坐标下，从约束 Jacobian $\Phi_q$ 到物理约束力的映射需要额外的**接触点位置参数化** $r_q$，而 Haug 的框架中未引入此概念
  - *Also affects*: 所有基于 Lagrange 方程处理关节摩擦的多体动力学方法
  - *Implication*: **工程实际中广泛使用广义坐标**，缺乏该坐标下的显式关系限制了理论的直接工程应用

### Research Frontier

- **Direction**: **广义坐标下约束力的显式 Lagrange 乘子表达**
  - *Prerequisite*: 需要建立接触点位置矢量对广义坐标的 Jacobian $r_q$
  - *Closest attempt*: [constraint-reaction-forces-lagrange-multipliers-mbs](constraint-reaction-forces-lagrange-multipliers-mbs.md) 推导了 $F^C = -(r_q^T)^{-1}\phi_q^T\lambda$，**填补了此空白**

## Relations

**Temporal context:** Haug (1992) 是多体系统计算动力学领域的奠基性教科书，建立了从变分原理到矩阵 DAE 的完整理论框架。Yao & Ren (2010) 直接引用本书第 3 章的笛卡尔坐标约束力表达（Eq. 3.2.9）作为出发点，将其推广到广义坐标。演化链：**Haug(1992)** → Peng et al.(2008) → [constraint-reaction-forces-lagrange-multipliers-mbs](constraint-reaction-forces-lagrange-multipliers-mbs.md)(2010)。

- **[constraint-reaction-forces-lagrange-multipliers-mbs](constraint-reaction-forces-lagrange-multipliers-mbs.md)** (*builds_on*): Yao & Ren 以 Haug 的笛卡尔坐标结果 $F^C = -\Phi_r^T\lambda$ 为基础，**推广到广义坐标并给出一一对应条件**

## Transferable Inspirations

- **从具体到抽象再到具体**的理论构建模式：先在最自然的坐标（笛卡尔）下建立基本关系，再通过参数化映射推广到更一般的表述，最后通过算例验证
- **矩阵 DAE 视角**统一了看似不同的约束动力学问题——这种"标准化"思路可迁移到其他含约束的物理建模问题

## Open Questions

- Haug 的 DAE 框架在处理奇异构型（约束 Jacobian 失秩）时如何正则化？
- 本书的变分方程方法能否直接推广到含摩擦的非理想约束系统？
