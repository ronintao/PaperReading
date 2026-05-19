---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 8
title: "Planar Dynamic Modeling and Analysis"
pages: 282-304
sections:
  - "8.1 Modeling and Analysis Techniques"
  - "8.2 Dynamic Analysis of a Slider-Crank Mechanism"
  - "8.3 Dynamic Analysis of a Quick-Return Mechanism"
  - "8.4 Dynamic Analysis of a Coil Spring"
  - "8.5 Dynamic Analysis of a Valve-Lifter Mechanism"
created: 2026-05-18
last_updated: 2026-05-18
---

# Chapter 8: Planar Dynamic Modeling and Analysis

> 本章是 Part One（平面系统）的收官章，与 Ch.5（运动学建模与应用）完全对称。Ch.5 中运动学分析过的同一批机构在本章进行完整的动力学分析。Ch.6 推导的 DAE 方程和 Ch.7 的数值方法在此得到工程应用验证。重点不在于新理论推导，而在于**建模方法论、参数研究和结果解释**——即工程判断能力的培养。所有案例均使用 DADS 代码完成。

## 章节定位

| 维度 | 说明 |
|------|------|
| **前置** | Ch.5 运动学模型（几何/约束数据），Ch.6 动力学方程（DAE，虚功原理，Lagrange 乘子），Ch.7 DAE 数值求解（坐标分区，积分器，平衡分析） |
| **本章** | §8.1 建模方法论 → §8.2 曲柄滑块（压缩机） → §8.3 快回机构（牛头刨床） → §8.4 螺旋弹簧（波传播+碰撞） → §8.5 气门挺杆（凸轮-弹簧设计） |
| **后续** | Part Two（Ch.9-12）将同一方法论推广到空间系统 |

---

## 概念定义

**Equilibrium Analysis（平衡分析）** [p.282]
> An equilibrium position is sought under the action of specified forces.
>
> 在给定外力作用下，求系统的平衡位置。使用 Ch.6 §6.5 的最小总势能方法。

---

**Inverse Dynamic Analysis（逆动力学分析）** [p.282]
> Drivers define the motion of the system and reaction forces are calculated from Lagrange multipliers.
>
> 通过运动学驱动约束确定系统运动，再由 Lagrange 乘子计算维持该运动所需的驱动力矩和约束反力。

---

**Dynamic Analysis（动力学分析/正向动力学分析）** [p.282]
> Transient response to applied forces is predicted by integrating the mixed differential-algebraic equations of motion.
>
> 对混合微分-代数运动方程（DAE）进行数值积分，预测系统在施加力作用下的瞬态响应。

---

**Composite Joints / Massless Links（复合铰/无质量连杆）** [p.282]
> If composite joints, called massless links, are employed in analysis, the engineer must be aware that the mass properties of the couplers are being neglected.
>
> 复合铰（无质量连杆）在分析中忽略了连杆的质量特性。连杆质量可作为集中质量分配到连接体上以改善近似精度。

---

**Lumped Mass Approximation（集中质量近似）** [p.282]
> The mass of a coupler can be distributed as lumped masses at the attachment points on each of the bodies that are connected.
>
> 将连杆质量分配为集中质量，置于连接体上的铰接点处，以改善使用无质量连杆时的近似质量。

---

**Gas Force（气体力/压缩气体力）** [p.284]
> A resisting force due to compression of gas acts on the slider. Figure 8.2.2 defines gas force $F_c$ as a function of position and velocity of the slider.
>
> 当曲柄滑块机构用作压缩机时，压缩气体对滑块施加的阻力。仅在压缩冲程（$\dot{x}_3 > 0$）期间作用。

---

**Lumped Mass Model of a Coil Spring（螺旋弹簧集中质量模型）** [p.294]
> A reasonable model is formed by discretizing the mass and stiffness of the spring. The lumped mass model is constructed by dividing the spring into equal lengths and approximating the mass effects of each component as a lumped mass $m$. The masses are connected by springs with stiffness $k$.
>
> 将连续质量分布的螺旋弹簧离散化为有限个集中质量点，用弹簧连接。每段等长，每个质量块质量 $m$，弹簧刚度 $k$。这是处理分布参数系统（波传播）的经典有限自由度近似。

---

**Surge Wave（涌浪波/应力波）** [p.294]
> Wave propagation in the spring, including reflection characteristics at the left end, is accounted for.
>
> 弹簧内部的应力波（压缩波/拉伸波）传播现象。当冲击载荷施加于弹簧一端时，波从受冲击端传播到固定端，并发生反射。

---

**Chattering（振颤/多次碰撞）** [p.295]
> Since the spring between bodies 6 and 8 is very stiff and bilinear, chattering behavior (multiple, high-frequency contacts) occurs between bodies 6 and 8.
>
> 当两个物体通过非常刚硬的单侧弹簧接触时，发生多次高频率的接触-分离-再接触循环。

---

**Unilateral Spring（单侧弹簧）** [p.295]
> The spring generates no force when its deflection is positive; it generates a very large compressive force when the spring deflection is negative.
>
> 仅在压缩方向起作用的弹簧（接触弹簧）：正变形（分离）时无力，负变形（接触/压缩）时产生很大的压缩力。用于建模碰撞/接触问题。

---

**Unilateral Damper（单侧阻尼器）** [p.298]
> The logic of the unilateral damper is similar to the unilateral spring: no damping force acts when the spring deflection is positive, while a damping force of 200 N·s/m × ℓ acts when the spring deflection is negative.
>
> 仅在接触（压缩）状态下提供阻尼的阻尼器。与单侧弹簧配合使用，减小碰撞时的振颤行为。

---

**Valve Spring（气门弹簧）** [p.300]
> The kinematic model of Section 5.6 is augmented with a valve spring. Inverse dynamic analysis is carried out to assist in the design of the valve spring.
>
> 内燃机气门机构中的回位弹簧。其刚度选择的核心设计准则：在所有工作转速下，凸轮-推杆之间的接触反力必须始终为正（不分离）。

---

**Negative Reaction Force / Cam-Follower Separation（负反力/凸轮-挺杆分离）** [p.300]
> A negative reaction force occurs between the pushrod and the cam... In an actual cam-flat-faced follower, separation would thus occur.
>
> 当推杆反力变为负值时，意味着凸轮与挺杆之间需要拉力维持接触——但实际平面凸轮无法提供拉力，因此发生分离。这是气门弹簧设计的失效判据。

---

## 符号定义

### §8.2 曲柄滑块机构（压缩机）

| 符号 | 类型 | 含义 |
|------|------|------|
| $F_c$ | 标量，力 (N) | 压缩气体对滑块的作用力 |
| $x_3$ | 标量，位移 (m) | 滑块（body 3）的 x 方向位置 |
| $\dot{x}_3$ | 标量，速度 (m/s) | 滑块速度（$>0$ 为压缩冲程） |
| $\phi_1(0)$ | 标量，角度 (rad) | 曲柄初始角度（$= \pi$） |
| $\dot{\phi}_1(0)$ | 标量，角速度 (rad/s) | 曲柄初始角速度（$= 30$） |
| $J_1^1, J_1^2, J_1^3$ | 标量，惯量 (kg·m²) | 飞轮极惯性矩三种取值：225, 450, 900 |

### §8.3 快回机构（牛头刨床）

| 符号 | 类型 | 含义 |
|------|------|------|
| $T_3$ | 标量，力矩 (N·m) | 施加于飞轮（body 3）的驱动力矩 |
| $\dot{\phi}_3$ | 标量，角速度 (rad/s) | 飞轮（曲柄）的角速度 |
| $m_6^1, m_6^2, m_6^3$ | 标量，质量 (kg) | 滑块质量三种取值：25, 50, 100 |
| $J_3^1, J_3^2, J_3^3$ | 标量，惯量 (kg·m²) | 飞轮极惯性矩三种取值：1000, 2000, 4000 |
| $x_6$ | 标量，位移 (m) | 滑块（body 6）的 x 方向位置 |
| $\dot{x}_6$ | 标量，速度 (m/s) | 滑块速度（$\dot{x}_6 < 0$ 为切削冲程） |

### §8.4 螺旋弹簧

| 符号 | 类型 | 含义 |
|------|------|------|
| $m$ | 标量，质量 (kg) | 每个集中质量块的质量（= 2.5 kg） |
| $k$ | 标量，刚度 (N/m) | 弹簧刚度（涌浪波: 200; 碰撞: 50; 参数研究: 30/40/50） |
| $\ell_0$ | 标量，长度 (m) | 弹簧段自由长度（= 0.2 m） |
| $M$ | 标量，质量 (kg) | 冲击重物质量（body 8，= 100 kg） |
| $K$ | 标量，刚度 (N/m) | 单侧弹簧接触刚度（= 1,000,000 N/m） |
| $k_e$ | 标量，刚度 (N/m) | 等效串联弹簧刚度（$= k/6$） |
| $\Delta x_8$ | 标量，位移 (m) | 重物最大侵入位移 |

### §8.5 气门挺杆机构

| 符号 | 类型 | 含义 |
|------|------|------|
| $k$ | 标量，刚度 (N/cm) | 气门弹簧刚度（10, 25, 40 N/cm） |

---

## 核心论点

### §8.1 建模方法论——三大注意事项

本章以 §8.1 开篇，阐明动力学建模的三项关键注意事项：

1. **三种分析模式**：平衡分析、逆动力学分析、动力学分析——对应 Ch.6 中推导的三种问题形式。每种模式回答不同的工程问题。

2. **数据一致性要求**：体坐标系原点**必须**取在质心（centroid），外力必须等效折算为作用于质心的力和力矩。否则 Ch.6 推导的运动方程将产生根本性错误。

3. **复合铰与无质量连杆**：使用复合铰简化建模时，连杆质量被忽略。可通过集中质量近似（将质量分配到两端铰接点）来改善，但不完全等价于实际质量分布。

4. **工程判断的重要性**：即使代码无错，错误的输入数据或不良设计仍会产生不合理结果。工程师必须发展对机械动力学行为的**定性理解**，以评估仿真结果的合理性并指导设计改进。

### §8.2 曲柄滑块机构——压缩机动力学

基于 Ch.5 §5.2.1 的运动学模型 1（Tables 5.2.1, 5.2.2），增加惯量数据（Table 8.2.1）进行完整动力学分析。

**惯量数据**

| 刚体 | Body 1（曲柄） | Body 2（连杆） | Body 3（滑块） | Body 4（地面） |
|------|------------|------------|------------|------------|
| 质量 (kg) | 200.0 | 35.0 | 25.0 | 1.0 |
| 极惯性矩 (kg·m²) | 450.0 | 35.0 | 0.02 | 1.0 |

**压缩机气体力**（仅在压缩冲程 $\dot{x}_3 > 0$ 时作用）：

$$F_c = \begin{cases} -\dfrac{282{,}857}{6 - x_3} + 62{,}857, & 1.5 \le x_3 \le 5 \\[6pt] -110{,}000[1 - \sin 2\pi(x_3 - 5.25)], & 5 < x_3 \le 5.5 \end{cases}$$

**平衡分析**（§6.5 最小总势能方法）：

| 条件 | Body 3 位置 $x_3$ (m) | 物理解释 |
|------|----------------------|--------|
| 仅重力 | 2.900 | 连杆质心尽可能低（最小化重力势能） |
| 重力 + 气体力 | 2.6575 | 滑块向左移动（气体力平衡部分势能） |

**逆动力学分析**（§5.2.3 驱动条件，Table 5.2.6 装配位置）：
- 通过 Lagrange 乘子（§6.6）计算维持恒定角速度所需的**驱动力矩**（Fig 8.2.4a）和**曲柄轴承反力** $F_x^{r(1,4)}$, $F_y^{r(1,4)}$（Fig 8.2.4b）
- 驱动力矩在压缩冲程末段急剧增大

**动力学分析——飞轮惯量参数研究**

初始条件：$\phi_1(0) = \pi$，$\dot{\phi}_1(0) = 30$ rad/s。恒定驱动力矩 41,450 N。

| 飞轮惯量 | 能否完成循环 | 循环频率 | 角速度波动 |
|---------|----------|--------|---------|
| $J_1^1 = 225$ kg·m² | **否**（能量不足） | — | 降至 ~5 rad/s 后失速 |
| $J_1^2 = 450$ kg·m² | 是 | ~3.7 cycles/s | 中等 |
| $J_1^3 = 900$ kg·m² | 是 | ~4.2 cycles/s | 最小 |

**失速的能量分析**：飞轮初始动能 + 半周期做功 $= \frac{1}{2}(225)(30^2) + \pi \times 41{,}450 = 231{,}469$ N·m < 压缩半周期所需做功 $260{,}438$ N·m。

**关键观察**：
- 较大飞轮惯量 → 角速度波动更小（**飞轮效应**）
- 滑块行程（位移幅度）相同（由运动学约束决定），但存在**相位差**
- 轴承反力（Fig 8.2.8）：最大惯量对应略大的反力峰值

### §8.3 快回机构——牛头刨床动力学

基于 Ch.5 §5.4.1 的运动学模型 1，用作金属切削牛头刨床（shaper, Fig 1.1.8）。

**惯量数据**

| 刚体 | 1 | 2 | 3（飞轮） | 4 | 5 | 6（滑块） |
|------|---|---|---------|---|---|---------|
| 质量 (kg) | 1.0 | 100.0 | 1000.0 | 5.0 | 30.0 | 50.0 |
| 惯量 (kg·m²) | 1.0 | 100.0 | 2000.0 | 0.05 | 10.0 | 1.5 |

切削力：仅在切削冲程（$\dot{x}_6 < 0$）作用，$x_6 \in [0, 1.7]$ m 时 200,000 N。

**逆动力学分析**（$\dot{\phi}_3 = 2\pi$ rad/s）：
- 驱动力矩的显著变化仅发生在**切削冲程即将开始时**（滑块速度需从正变负）
- 滑块质量越大 → 驱动力矩波动越大（Fig 8.3.2）

**动力学分析——飞轮惯量参数研究**

$m_6 = 50$ kg，$T_3 = 165{,}521$ N·m（选取使一周期做功 $2\pi T_3$ 等于切削做功 $10.4 \times 10^5$ N·m）。

| 飞轮惯量 | 循环频率 |
|---------|--------|
| $J_3^1 = 1000$ kg·m² | ~2.2 cycles/s |
| $J_3^2 = 2000$ kg·m² | ~1.8 cycles/s |
| $J_3^3 = 4000$ kg·m² | ~1.5 cycles/s |

**与 §8.2 压缩机的关键对比**：

| | 压缩机（§8.2） | 牛头刨床（§8.3） |
|---|---|---|
| 飞轮惯量 ↑ 时循环频率 | **↑**（更快） | **↓**（更慢） |
| 载荷特征 | 遍布整个压缩冲程 | 仅部分行程（切削冲程） |
| 原因 | 大惯量维持高速通过阻力段 | 大惯量使平均角速度降低但更稳定 |

轴承反力（Fig 8.3.5）：最小飞轮惯量对应最大反力变化。

### §8.4 螺旋弹簧——波传播与碰撞

本节展示了一个与前面旋转机构截然不同的动力学问题——**分布参数系统的有限自由度近似**。

**§8.4.1 涌浪波（Surge Waves）**

6 个集中质量（$m = 2.5$ kg）通过弹簧（$k = 200$ N/m）串联，左端固定于地面（body 7）。给 body 6 施加初始速度 $\dot{x}_6 = -0.1$ m/s 模拟冲击。

结果（Fig 8.4.2）：即使仅 6 个质量的粗糙模型，也能清晰展现：
- 压缩波从 body 6 向 body 1 传播
- 在左端固定壁处的**反射**
- 更多质量块将产生更逼近实际的波行为

**§8.4.2 碰撞与振颤（Impact and Chattering）**

在 body 6 右端添加重物 $M = 100$ kg（body 8），通过**单侧弹簧**（$K = 10^6$ N/m）建模碰撞接触。

**最大侵入量能量估算**：

$$\frac{1}{2}M(\dot{x}_8)^2 \approx \frac{1}{2}k_e(\Delta x_8)^2, \quad k_e = k/6$$

$$\Delta x_8 = \sqrt{\frac{M}{k_e}} \cdot |\dot{x}_8| = \sqrt{\frac{6}{50}} \times 0.1 = 0.346 \text{ m}$$

动态仿真结果：$\Delta x_8 = 0.327$ m（差异来自集中质量的动能分配）。

**弹簧刚度参数研究**（碰撞与分离）：

| 弹簧刚度 $k$ (N/m) | 分离时间 (s) | 分离位置 (m) | 振颤周期 |
|-------------------|-----------|-----------|--------|
| 50 | ~11.8 | ~1.27 | 最短 |
| 40 | ~13.4 | ~1.27 | 中等 |
| 30 | ~15.3 | ~1.27 | 最长 |

**关键观察**：
- 刚度 ↑ → 波速 ↑ → 振颤周期 ↓ → 分离更早
- 分离位置 ~1.27 m > 静平衡位置 1.2 m（弹簧自身质量 15 kg 的动能额外推动 body 6）
- 分离位置与刚度无关（由能量守恒决定）

**加入单侧阻尼器**（200 N·s/m × ℓ，仅接触时有效）：
- 振颤的相对位移和周期均减小
- 分离位置和时间与无阻尼情况近似相同

### §8.5 气门挺杆机构——弹簧设计准则

使用 Ch.5 §5.6 的凸轮驱动气门机构模型，增加气门弹簧进行**逆动力学分析**，核心目的是辅助弹簧设计。

**建模数据**（TABLE 8.5.1，注意单位为 g 和 g·cm²）

| 刚体 | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|
| 质量 (g) | 1.0 | 30.0 | 120.0 | 150.0 | 60.0 |
| 惯量 (g·cm²) | 1.0 | 15.0 | 2250.0 | 1800.0 | 800.0 |

标称凸轮转速：3000 rpm = $100\pi$ rad/s。

**弹簧刚度参数研究**（Fig 8.5.1，3000 rpm）：

| 弹簧刚度 $k$ (N/cm) | 推杆反力是否出现负值 | 结论 |
|---------------------|-----------------|------|
| 10 | **是**（$t \approx 0.01$ s） | 不可接受——凸轮-挺杆分离 |
| 25 | 否 | 可接受 |
| 40 | 否 | 可接受 |

**转速参数研究**（Fig 8.5.2，$k = 25$ N/cm）：

| 转速 (rpm) | 推杆反力是否出现负值 | 结论 |
|-----------|-----------------|------|
| 1500 | 否 | 可接受 |
| 3000 | 否 | 可接受 |
| 4500 | **是** | 不可接受——需更大 $k$ |

**设计准则**：气门弹簧刚度 $k$ 的选择必须保证在**最高工作转速**下推杆反力始终为正（凸轮-挺杆不分离）。这是一个**转速-刚度交叉约束**：$k$ 过小 → 高速时惯性力超过弹簧回复力 → 分离；$k$ 过大 → 弹簧力增大 → 摩擦损失增大、磨损加剧。

---

## 工程应用与实例

| 图号/表号 | 名称 | 类型 | 应用 | 关键知识点 |
|---------|------|------|------|-----------|
| Table 8.2.1-8.2.4 | 曲柄滑块惯量与平衡 | 数据表 | 压缩机 | 惯量数据；重力/气体力下平衡位置差异 |
| Fig 8.2.4 | 逆动力学结果 | 曲线图 | 压缩机 | 驱动力矩和轴承反力由 Lagrange 乘子直接给出 |
| Fig 8.2.5-8.2.8 | 动力学参数研究 | 曲线图 | 压缩机 | 飞轮惯量对角速度波动、循环频率、轴承反力的影响；$J_1^1$ 失速的能量分析 |
| Table 8.3.1-8.3.2 | 快回机构惯量与平衡 | 数据表 | 牛头刨床 | 6体系统惯量；重力下平衡 |
| Fig 8.3.2 | 逆动力学力矩 | 曲线图 | 牛头刨床 | 滑块质量对驱动力矩的影响 |
| Fig 8.3.3-8.3.5 | 动力学参数研究 | 曲线图 | 牛头刨床 | 飞轮惯量与循环频率的反直觉关系（与压缩机对比） |
| Fig 8.4.1-8.4.2 | 弹簧集中质量模型与涌浪波 | 示意图+曲线 | 弹簧 | 6 质量即可捕捉波传播和反射 |
| Fig 8.4.3-8.4.4 | 碰撞模型与单侧弹簧 | 示意图 | 碰撞 | 单侧弹簧建模碰撞；能量估算最大侵入量 |
| Fig 8.4.7-8.4.9 | 振颤（有/无阻尼） | 曲线图 | 碰撞 | 阻尼减小振颤幅度和周期，不改变分离条件 |
| Table 8.5.1 | 气门挺杆惯量数据 | 数据表 | 内燃机 | g 级质量，g·cm² 级惯量 |
| Fig 8.5.1-8.5.2 | 推杆反力 vs 弹簧刚度/转速 | 曲线图 | 内燃机 | 负反力 = 凸轮分离失效准则；刚度-转速交叉约束 |
| DADS Projects 8.1-8.5 | 练习题 | 项目 | 综合 | Film follower / Web cutter / Rack-pinion / 逆→正动力学对比 |

---

## 与全书的关系

| 本章概念 | 前置来源 | 后续展开 |
|---------|--------|--------|
| 三种分析模式 | Ch.6 §6.3（DAE）、§6.5（平衡）、§6.6（逆动力学） | Ch.12（空间系统的同三种模式） |
| 飞轮惯量参数研究 | Ch.6（质量矩阵 $\mathbf{M}$） | Ch.12（空间惯性张量的影响） |
| Lagrange 乘子 → 约束反力 | Ch.6 §6.6（Eqs. 6.6.8-6.6.9） | Ch.12（空间约束反力） |
| 最小总势能平衡 | Ch.6 §6.5 / Ch.7 §7.5 | Ch.12（空间平衡分析） |
| 集中质量弹簧模型 | Ch.2（向量/矩阵）、Ch.6（弹簧力元） | 柔性多体动力学（超出本书范围） |
| 单侧弹簧/接触建模 | 本章首次引入 | 非光滑动力学（超出本书范围） |
| 气门弹簧负反力准则 | Ch.5 §5.6（凸轮运动学）、Ch.6（Lagrange 乘子） | 工程实践（弹簧设计规范） |
| Part One → Part Two 过渡 | Ch.2-8（平面系统方法论完整闭环） | Ch.9-12（空间系统：Euler 参数、空间约束、空间动力学、应用） |
