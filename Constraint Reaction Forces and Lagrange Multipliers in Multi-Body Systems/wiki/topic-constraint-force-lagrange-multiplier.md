---
type: topic
id: topic-constraint-force-lagrange-multiplier
title: "约束反力与 Lagrange 乘子的关系"
source_papers:
  - constraint-reaction-forces-lagrange-multipliers-mbs
  - intermediate-dynamics-haug
created: 2026-05-12
last_updated: 2026-05-12
---

## 问题描述

在多体系统动力学中，Lagrange 乘子 $\lambda$ 常被直接等同于约束反力 $F^C$，但两者并非总是相等。本专题整理约束反力与 Lagrange 乘子之间的显式关系——从笛卡尔坐标下的基本表达出发，推广到广义坐标系统，并给出两者一一对应的充要条件。

## 符号定义

- $\mathbf{r} = [x_1, \ldots, x_{3N}]^T$：$N$ 个质点的笛卡尔坐标位置矢量
- $\mathbf{q} = [q_1, \ldots, q_l]^T$：系统的广义坐标
- $\boldsymbol{\phi}(\mathbf{r}, t) = 0$：完整约束方程（向量值函数）
- $\phi_r = \frac{\partial \boldsymbol{\phi}}{\partial \mathbf{r}}$：约束对笛卡尔坐标的 Jacobian 矩阵
- $\phi_q = \frac{\partial \boldsymbol{\phi}}{\partial \mathbf{q}}$：约束对广义坐标的 Jacobian 矩阵
- $\lambda$：Lagrange 乘子向量
- $F^C$：约束反力（作用在约束接触点上的实际力）
- $\delta\mathbf{r}$：满足约束的虚位移
- $\mathbf{r}_C = \mathbf{r}_C(\mathbf{q})$：约束接触点的位置矢量
- $r_q = \frac{\partial \mathbf{r}_C}{\partial \mathbf{q}}$：接触点位置对广义坐标的 Jacobian 矩阵

## 核心公式

- **笛卡尔坐标下的约束力**：$F^C = -\phi_r^T \lambda$ —— 约束力等于约束 Jacobian 转置乘以 Lagrange 乘子 [constraint-reaction-forces-lagrange-multipliers-mbs, Eq.5]
- **广义坐标下的约束力**：$F^C = -(r_q r_q^T)^{-1} r_q \, \phi_q^T \lambda$ —— 需要接触点 Jacobian $r_q$ 满秩 [constraint-reaction-forces-lagrange-multipliers-mbs, Eq.11]
- **一一对应条件**：当 $r_q = -\phi_q$ 时，$F^C = \lambda$ —— 约束力与 Lagrange 乘子数值相等 [constraint-reaction-forces-lagrange-multipliers-mbs, §3]

## 关键推导

### Step 1：笛卡尔坐标下的约束反力

对含 $N$ 个质点的离散系统，约束为 $\boldsymbol{\phi}(\mathbf{r}, t) = 0$。虚位移满足 [constraint-reaction-forces-lagrange-multipliers-mbs, Eq.1]：

$$\phi_r \, \delta\mathbf{r} = 0$$

理想约束的定义：约束力对所有满足约束的虚位移不做虚功 [constraint-reaction-forces-lagrange-multipliers-mbs, Eq.3]：

$$\delta\mathbf{r}^T F^C = 0$$

由 Lagrange 乘子定理，约束力可表示为约束 Jacobian 转置与乘子的乘积 [constraint-reaction-forces-lagrange-multipliers-mbs, Eq.5；intermediate-dynamics-haug, Eq.3.2.9]：

$$F^C = -\phi_r^T \lambda$$

注意这里 $F^C \neq \lambda$——两者之间隔着约束 Jacobian 的转置矩阵 $\phi_r^T$。只有当 $\phi_r$ 为单位矩阵时两者才数值相等。

### Step 2：广义坐标下的约束反力

当系统用广义坐标 $\mathbf{q}$ 描述，有 $k$ 个独立约束 $\boldsymbol{\phi}(\mathbf{q}, t) = 0$。引入接触点位置的参数化 $\mathbf{r}_C = \mathbf{r}_C(\mathbf{q})$，虚位移映射为 [constraint-reaction-forces-lagrange-multipliers-mbs, Eq.7]：

$$\delta\mathbf{r}_C = r_q \, \delta\mathbf{q}$$

代入理想约束条件 $\delta\mathbf{r}_C^T F^C = 0$，结合 Lagrange 乘子定理得 [constraint-reaction-forces-lagrange-multipliers-mbs, Eq.10]：

$$r_q^T F^C = -\phi_q^T \lambda$$

左乘 $r_q$，若 $r_q$ 满秩（即 $r_q r_q^T$ 可逆），解出约束力 [constraint-reaction-forces-lagrange-multipliers-mbs, Eq.11]：

$$F^C = -(r_q r_q^T)^{-1} r_q \, \phi_q^T \lambda$$

当 $r_q$ 为方阵且可逆时，进一步简化为：

$$F^C = -(r_q^T)^{-1} \phi_q^T \lambda$$

### Step 3：一一对应条件

当约束方程的形式与接触点位置表达式关于广义坐标的偏导形式一致时 [constraint-reaction-forces-lagrange-multipliers-mbs, §3]：

$$r_q = -\phi_q$$

代入广义坐标表达式，得到：

$$F^C = -(r_q r_q^T)^{-1} r_q \, (-r_q)^T \lambda = (r_q r_q^T)^{-1} (r_q r_q^T) \lambda = \lambda$$

因此 $F^C = \lambda$——约束力与 Lagrange 乘子一一对应。

实际意义：通过合理选择广义坐标，使约束方程的结构天然满足 $r_q = -\phi_q$，即可从 Lagrange 乘子直接读出约束反力。曲柄滑块算例验证了 $F_C = \lambda = 0.7698$ N [constraint-reaction-forces-lagrange-multipliers-mbs, Eq.14]。
