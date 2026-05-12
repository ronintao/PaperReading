---
type: source
id: constraint-reaction-forces-lagrange-multipliers-mbs
pdf_path: "../Constraint Reaction Forces and Lagrange Multipliers in Multi-Body Systems.pdf"
url: https://doi.org/10.4028/www.scientific.net/AMR.97-101.2824
tags:
  - multibody-dynamics
  - analytical-mechanics
  - year/2010-03
  - venue/AMR
created: 2026-05-11
last_updated: 2026-05-12
authors:
  - Wenli Yao
  - Yongsheng Ren
aliases:
  - Constraint Reaction Forces and Lagrange Multipliers in Multi-Body Systems
---

## Essence

> [!abstract]
> **One-Sentence Summarization**: 本文推导了多体系统中**约束反力与 Lagrange 乘子之间的显式关系**，在完全笛卡尔坐标和广义坐标两种描述下分别给出表达式，并确定了两者一一对应的充要条件。
> **Contribution**: 将 Edward (1992) 仅在笛卡尔坐标下的结果推广到**更一般的 Lagrange 广义坐标系统**，推导出 $F^C = -(r_q^T)^{-1}\phi_q^T\lambda$ 的显式表达，并证明了**当约束方程与接触点位置表达形式一致时**（即 $r_q = -\phi_q$），约束反力与 Lagrange 乘子一一对应。

## Factors

### Context

**多体系统动力学**是复杂机械系统（车辆、制造装备、机器人、航空航天）设计与控制的重要理论基础。当系统中存在**干摩擦、接触、碰撞等非光滑因素**时，传统动力学方法遇到困难——摩擦力的计算需要法向约束反力的显式表达，而标准的 Lagrange 方程只给出 Lagrange 乘子。

### Related Work

- **D'Alembert 原理方法**：可直接计算约束反力，但难以与多体系统动力学的系统化建模框架结合
- **Edward (1992)**：在完全笛卡尔坐标下证明了约束反力与 Lagrange 乘子的关系 $F^C = -\phi_r^T\lambda$，但仅限于笛卡尔坐标描述
- **Peng et al. (2008)**：通过广义笛卡尔坐标和约束方程的偏方法求解多体系统约束力
- **Schiehlen et al. (2006)**：讨论了非光滑多体系统的计算方法所面临的困难

### Gap

文献中常**将 Lagrange 乘子直接等同于约束反力**，但正如 Eq.5 所示 $F^C = -\phi_r^T\lambda$，两者并非总是相等——乘子需经过约束 Jacobian 矩阵变换才得到约束力。更重要的是，**缺乏在独立广义坐标下约束反力的显式表达**，这使得在标准 Lagrange 框架中直接处理摩擦力等非光滑问题变得困难。

### Proposal

本文针对更一般的 Lagrange 系统，推导出**广义坐标下约束反力的显式表达式** $F^C = -(r_q r_q^T)^{-1} r_q \phi_q^T \lambda$，其中 $r_q$ 是接触点位置矢量对广义坐标的 Jacobian。进一步给出了**约束力与 Lagrange 乘子一一对应的条件**：当 $r_q = -\phi_q$ 时成立。通过曲柄滑块机构的数值算例验证了方法的正确性。

## Architecture

### 整体结构：推导逻辑总览

> [!info] 符号约定
> $\phi$（或 $\Phi$）表示**约束方程本身**（向量值函数），下标表示求偏导：$\phi_r = \frac{\partial \phi}{\partial \mathbf{r}}$ 是约束对笛卡尔坐标的 **Jacobian 矩阵**，$\phi_q = \frac{\partial \phi}{\partial \mathbf{q}}$ 是约束对广义坐标的 Jacobian。$\Phi$/$\phi$ 本身不是 Jacobian，而是约束方程；$\Phi_r$/$\phi_q$ 才是 Jacobian。

本文的推导包含两个层次——先在完全笛卡尔坐标下建立基本表达，再推广到独立广义坐标下，最终给出一一对应条件。

```
输入: N 粒子离散系统 + 约束方程 φ(r,t)=0
         │
         ▼
[Step 1: 笛卡尔坐标下的约束反力]
  虚位移条件: φ_r δr = 0
  理想约束力定义: δr^T F^C = 0
  Lagrange 乘子定理 ──→ F^C = -φ_r^T λ  ... (Eq.5)
         │
         ▼
[Step 2: 广义坐标下的约束反力]
  广义坐标 q, 约束 φ(q,t)=0
  接触点位置参数化: r_C = r_C(q)
  虚位移映射: δr_C = r_q δq  ... (Eq.7)
  理想约束 + Lagrange 乘子定理
    ──→ r_q^T F^C = -φ_q^T λ  ... (Eq.10)
  左乘 r_q, 若 r_q 满秩:
    ──→ F^C = -(r_q r_q^T)^{-1} r_q φ_q^T λ  ... (Eq.11)
         │
         ▼
[Step 3: 一一对应条件]
  当 r_q = -φ_q 时: F^C = λ（一一对应）
         │
         ▼
[验证: 曲柄滑块机构算例]
  θ, ϕ 为广义坐标
  第一类 Lagrange 方程求解 λ
  验证 F_C = λ = 0.7698 N（与 D'Alembert 原理一致）
```

### 笛卡尔坐标下的约束反力表达

对含 $N$ 个质点的离散系统，位置矢量 $\mathbf{r} = [x_1, \ldots, x_{3N}]^T$，运动学约束为 $\boldsymbol{\phi}(\mathbf{r}, t) = 0$。**理想约束力**的定义是对所有满足 $\phi_r \delta\mathbf{r} = 0$ 的虚位移，约束力不做虚功。

$$F^C = -\phi_r^T \lambda$$

> [!note] 为什么这不意味着 $\lambda$ 就是约束力？
> 约束力 $F^C$ 与乘子 $\lambda$ 之间隔着**约束 Jacobian 的转置** $\phi_r^T$。只有当 $\phi_r$ 为单位矩阵（约束方程即坐标本身）时两者才数值相等。文献中直接令 $F^C = \lambda$ 的做法**在一般情况下是错误的**。

### 广义坐标下的约束反力表达

当系统具有 $n$ 个自由度，采用广义坐标 $\mathbf{q} = [q_1, \ldots, q_l]^T$ 描述，且有 $k$ 个独立约束。关键引入**接触点位置矢量** $\mathbf{r}_C$ 对广义坐标的参数化，建立虚位移映射：

$$\delta\mathbf{r}_C^T = (r_q \delta\mathbf{q})^T = \delta\mathbf{q}^T r_q^T$$

结合理想约束定义和 Lagrange 乘子定理，得到：

$$F^C = -(r_q r_q^T)^{-1} r_q \phi_q^T \lambda = -(r_q^T)^{-1} \phi_q^T \lambda$$

> [!note] 为什么需要 $r_q$ 满秩？
> 矩阵 $r_q r_q^T$ 的可逆性是从 Eq.10 解出 $F^C$ 的必要条件。物理上要求**接触点位置矢量对广义坐标的 Jacobian 是满秩的**，即接触点的运动能被广义坐标完全描述。

### 一一对应条件

当约束方程的形式与接触点位置表达式关于广义坐标的形式一致时：

$$r_q = -\phi_q \implies F^C = \lambda$$

> [!note] 实际意义
> 这意味着通过**合理选择广义坐标**，可以使约束方程的结构天然满足此条件，从而**无需额外计算就能从 Lagrange 乘子直接读出约束反力**。在曲柄滑块算例中，选择 $\theta$ 和 $\varphi$ 作为广义坐标后，约束 $y_C = r\sin\theta - l\cos\varphi = \text{const}$ 恰好满足此条件。

### 曲柄滑块验证算例

![曲柄滑块系统](figures/constraint-reaction-forces-lagrange-multipliers-mbs/figure_1.png)

> Figure 1 展示了曲柄滑块机构：曲柄 AB 上施加力矩 M，连杆 BC 质量忽略，滑块 C 受法向约束。

![广义坐标定义](figures/constraint-reaction-forces-lagrange-multipliers-mbs/figure_2.png)

> Figure 2 展示了系统的广义坐标选取：$\theta$（曲柄角）和 $\varphi$（连杆角）。

系统动能：

$$T = \frac{2}{3}mr^2\dot{\theta}^2 + \frac{1}{2}ml^2\dot{\varphi}^2 + mrl\sin(\varphi - \theta)\dot{\theta}\dot{\varphi}$$

约束方程：

$$y_C = r\sin\theta - l\cos\varphi = \text{const}$$

使用第一类 Lagrange 方程（Eq.14），取参数 $m=1\text{kg}$，$r=1\text{m}$，$l=\sqrt{3}\text{m}$，$\theta=\pi/3$，$\dot{\theta}=1\text{rad/s}$，$\varphi=\pi/3$，$\dot{\varphi}=-1/3\text{rad/s}$，$g=9.8\text{m/s}^2$，求得：

$$F_C = \lambda = 0.7698 \text{ N}$$

与 D'Alembert 原理计算结果一致，验证了一一对应条件的正确性。

## Evidence

| 验证项 | 方法 | 结果 |
|--------|------|------|
| 曲柄滑块法向约束力 | 第一类 Lagrange 方程求解 $\lambda$ | $F_C = \lambda = 0.7698$ N |
| 与 D'Alembert 原理对比 | 独立计算 | 结果一致 |
| 一一对应条件验证 | 检查 $r_q = -\phi_q$ | 约束 $y_C = r\sin\theta - l\cos\varphi$ 满足条件 |

本文仅提供了单一算例验证，未进行大规模数值实验或多种机构的对比测试。

## Critical Analysis

### Novel Insight

- **Insight**: **Lagrange 乘子并非总是等于约束反力**，两者之间存在约束 Jacobian 矩阵的变换关系
  - *Prior*: 动力学教科书和文献中普遍将两者直接等同使用
  - *Update*: 明确了**等价关系仅在特定坐标选择下成立**（$r_q = -\phi_q$），提供了判断准则

- **Insight**: 通过**合理选择广义坐标**可以构造出乘子与约束力一一对应的系统
  - *Prior*: 广义坐标的选择主要考虑简化运动方程，未关注其对约束力计算的影响
  - *Update*: 坐标选择新增了一个**工程实用判据**：使约束方程形式与接触点位置表达一致

### Fundamental Limitations

- **Limitation**: **一一对应条件的可实现性**受限于系统几何拓扑
  - *Root cause*: 条件 $r_q = -\phi_q$ 本质上要求约束方程和接触点参数化在广义坐标下**结构相同**，但对复杂空间机构（如并联机器人），这种坐标选择可能不存在
  - *Also affects*: 所有基于 Lagrange 乘子处理非光滑因素的多体动力学方法
  - *Implication*: **方法的适用范围局限于几何结构较简单的平面机构**，复杂三维系统需要其他途径

- **Limitation**: **数值验证的深度不足**
  - *Root cause*: 仅用一个二自由度平面机构（曲柄滑块）验证，未涉及**高自由度、三维、含摩擦的动态仿真**
  - *Also affects*: 方法在实际工程应用中的可信度
  - *Implication*: 该方法的**数值稳定性和计算效率**在复杂系统中的表现完全未知

### Research Frontier

- **Direction**: **含干摩擦的多体系统统一动力学建模**
  - *Prerequisite*: 需要将本文的约束力显式表达嵌入到摩擦力模型（如 Coulomb 摩擦锥）中，建立完整的非光滑动力学方程
  - *Closest attempt*: Schiehlen et al. (2006) 讨论了非光滑多体系统计算方法的困难，但**缺乏约束力与乘子关系的显式利用**

- **Direction**: **自动坐标选择算法**——自动判断并构造满足 $r_q = -\phi_q$ 的广义坐标
  - *Prerequisite*: 需要符号计算框架能够自动分析约束方程和接触点参数化的结构等价性
  - *Closest attempt*: 暂无直接尝试

## Relations

**Temporal context:** 本文 (2010) 是 Edward (1992) 在笛卡尔坐标下约束力-乘子关系工作的广义坐标推广，发表于 Advanced Materials Research 会议论文集。同期 Schiehlen et al. (2006) 讨论了非光滑多体动力学的计算挑战，Peng et al. (2008) 探索了广义笛卡尔坐标下的约束力求解。本文填补了两者之间的理论空白：**在独立广义坐标下给出约束反力的显式 Lagrange 乘子表达**。

- **Edward (1992)** (*builds_on*): Edward 在完全笛卡尔坐标下给出 $F^C = -\phi_r^T\lambda$，本文将此**推广到独立广义坐标**并给出 Eq.11
- **[intermediate-dynamics-haug](intermediate-dynamics-haug.md)** (*builds_on*): Haug 建立了笛卡尔坐标下 $F_{ij}^C = -\Phi_{r_i}^{ijT}\lambda^{ij}$ 的完整证明（Eq. 3.2.9）和矩阵 DAE 框架（Eq. 3.4.7），本文**在此基础上推广到广义坐标**
- **Schiehlen et al. (2006)** (*complements*): 讨论了非光滑多体系统的计算困难，本文提供了**处理非光滑因素所需的约束力显式表达**
- **Peng et al. (2008)** (*contrasts_with*): 采用广义笛卡尔坐标和约束方程偏方法，本文则**在独立广义坐标下直接推导**，方法更简洁

## Transferable Inspirations

- 在建模中，**坐标选择不仅影响方程复杂度，还决定物理量之间的对应关系**——选择坐标时应同时考虑计算效率和物理可解释性
- "常识性"的等价关系（如 $\lambda = F^C$）值得严格审视，**隐藏的变换矩阵可能在特殊情况下引发错误**

## Open Questions

- 对于冗余约束（$\phi_r$ 不满秩）的系统，该框架如何修改？
- 能否将一一对应条件推广到非完整约束（速度级约束）？
- 该理论在有限元法与多体动力学耦合的柔性系统中如何应用？
