---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 5
title: "Planar Kinematic Modeling and Analysis"
pages: 153-198
sections:
  - "5.1 Modeling and Analysis Techniques"
  - "5.2 Kinematic Analysis of a Slider-Crank Mechanism"
  - "5.3 Kinematic Analysis of a Four-Bar Mechanism"
  - "5.4 Kinematic Analysis of a Quick-Return Mechanism"
  - "5.5 Kinematic Analysis of a Gear-Slider Mechanism"
  - "5.6 Kinematic Analysis of a Valve-Lifter Mechanism"
created: 2025-07-27
last_updated: 2025-07-27
---

# Chapter 5: Planar Kinematic Modeling and Analysis

> 本章将第2-4章建立的理论和数值方法应用于五个递进复杂的平面机构案例——曲柄滑块、四连杆、快回机构、齿轮-滑块和气门挺杆——展示了笛卡尔坐标法的通用建模流程和 DADS 代码的完整使用方法。

## 概念定义

**Kinematic Modeling（运动学建模）** [p.153]
> Kinematic modeling of a mechanism involves the selection of bodies that make up the mechanism, kinematic constraints that act between pairs of bodies, and time-dependent kinematic drivers. A key requirement of kinematic modeling is that the combination of bodies, kinematic constraints, and drivers must have no free degrees of freedom. That is, the number of generalized coordinates in the model must equal the number of independent constraint equations.
>
> 运动学建模涉及选择组成机构的刚体、作用于刚体对之间的运动学约束以及时间相关的运动学驱动器。运动学建模的关键要求是刚体、约束和驱动器的组合不能有自由度剩余，即模型中广义坐标的数目必须等于独立约束方程的数目。

---

**Body-Fixed Reference Frame（体固连参考系）** [p.154]
> Once the bodies that make up a system model have been selected, a body-fixed reference frame must be attached to each body. Since kinematic analysis is not concerned with forces and inertias, the locations of the origins of body-fixed reference frames are arbitrary. They can be located at points that make the model easy to develop. If subsequent dynamic analysis is anticipated, however, body-fixed reference frames with their origins at centers of mass should be selected (see Chapter 6).
>
> 一旦选定了系统模型的刚体，必须为每个刚体附加一个体固连参考系。由于运动学分析不涉及力和惯性，体固连系原点的位置是任意的，可以选在便于建模的点。但如果预期后续需要动力学分析，则应将原点选在质心处（见第6章）。

---

**Kinematic Modeling Recipe（运动学建模配方/步骤）** [pp.154-155]
> To assist the engineer in modeling, the following *kinematic modeling recipe* is suggested, making use of theoretical information and intuition to arrive at a reasonable model:
> 1. Draw a clear diagram of the system to be modeled and select and name or number bodies and kinematic joints between pairs of bodies. As preliminary checks on reasonableness of the model:
>    (a) Count *nh* constraints; calculate $d = 3nb - nh$; check $d \leq 0$ or $d$ matches anticipated DOF.
>    (b) Inspect the model for feasibility: "Can the system be assembled with manufacturing imperfection?"
> 2. Presuming redundant constraints have been eliminated, define $d = 3nb - nh$ drivers to specify the motion. Repeat step 1b for driving constraints.
> 3. Make drawings of each body, defining body-fixed $x'$-$y'$ frames and data for joints and drivers.
> 4. Use a reasonable sketch or diagram to estimate initial position and orientation variables for assembly.
>
> 为辅助工程师建模，建议使用以下运动学建模配方，结合理论信息和直觉建立合理模型：
> 1. 画出系统清晰图示，选择和编号刚体及运动副；初步检查：(a) 计数约束 $nh$，计算 $d=3nb-nh$，检查 $d$ 是否 $\leq 0$ 或与预期自由度匹配；(b) 检查可行性——存在制造公差时系统能否装配。
> 2. 消除冗余约束后，定义 $d$ 个驱动器来指定运动，再次检查驱动约束的可行性和冗余性。
> 3. 画出每个刚体的详图，定义体坐标系和关节/驱动器的数据。
> 4. 利用草图估计初始位置和姿态变量，用于装配分析。

---

**Composite Joint（复合铰）** [p.159]
> In model 2, the connecting rod $BC$ is modeled as a composite revolute-revolute joint and no ground body is introduced. The advantage of the composite joint is that it reduces the dimension of the matrices that must be handled by eliminating three generalized coordinates that would normally be required for the connecting rod.
>
> 在模型2中，连杆 $BC$ 被建模为复合转动-转动铰，不引入地面刚体。复合铰的优势在于通过消除连杆通常需要的三个广义坐标，减小了矩阵维度。

---

**Lock-up Configuration（锁死构型）** [p.168]
> As shown analytically in Example 3.7.3, the slider-crank mechanism will *lock up* if the crank arm (body 1) is longer than the connecting rod (body 2). Figure 5.2.14 shows the velocity and acceleration of the slider for a simulation with the length of the slider reduced to $\ell_5 = 1.9$, which is shorter than the length of the crank. Note that as $t$ approaches 0.074 s both the velocity and acceleration of the slider approach infinity.
>
> 若曲柄臂长于连杆，曲柄滑块机构将发生锁死。Fig. 5.2.14 显示了连杆长度缩短至 $\ell_5 = 1.9$（短于曲柄）时的模拟结果。当 $t$ 趋近 0.074 s 时，速度和加速度都趋近无穷大。

---

**Bifurcation Point（分叉点）** [p.157]
> Thus, $\phi_1 = \omega t^* = \pi/2$ is a bifurcation point and the constraint Jacobian that contains the driver must be singular. It is interesting that this physical reasoning shows that the $15 \times 15$ Jacobian matrix is singular, without evaluating its determinant or calculating its rank using Gaussian elimination.
>
> $\phi_1 = \omega t^* = \pi/2$ 是一个分叉点，包含驱动器的约束 Jacobian 矩阵必须是奇异的。物理推理不需要计算行列式或用高斯消元法求秩，即可判定 $15\times 15$ 的 Jacobian 矩阵奇异。

---

**Quick-Return Mechanism（快回机构）** [p.175]
> The quick-return mechanism of Fig. 5.4.1 that represents a shaper is considered. With counterclockwise rotation of the crank (body 3), cutting occurs as the tool (body 6) moves to the left through the workpiece. The quick-return stroke of the tool occurs as it moves to the right.
>
> 快回机构代表一台牛头刨床。曲柄逆时针旋转时，刀具向左穿过工件进行切削。刀具向右运动时发生快速回程。

---

**Dwell（驻留/停歇）** [p.183]
> Of further interest, note the nearly constant position of the slider (called *dwell*) during the period 0.5 to 0.6 s. This period would permit an auxiliary mechanism to lift the tool from the workpiece, prior to the return stroke.
>
> 在 $t = 0.5 \sim 0.6$ s 期间，滑块位置几乎不变（称为"驻留"），此时可以利用辅助机构将刀具从工件上抬起，然后再进行回程。

---

**Gear Set Joint（齿轮副约束）** [p.186]
> Two gear set joints: Gear 2–Gear 3, Gear 3–Gear 4. Each provides 1 constraint.
>
> 齿轮副约束（详见 §4.9）提供1个约束方程，将两个齿轮的角度通过传动比耦合。

---

**Distance Constraint（距离约束）** [p.186]
> Three distance constraints: Gear 2–Gear 3, Gear 3–Gear 4, Gear 4–Slider.
>
> 距离约束确保齿轮中心间距恒定（保持啮合），是齿轮建模中与齿轮副约束配合使用的必要约束。

---

**Cam-Flat-Faced Follower Joint（凸轮-平面从动件约束）** [p.191-192]
> A simple circular cam-flat-faced follower is shown in Fig. 5.6.1, with the cam center offset from the pivot at point $B$ in ground to induce follower motion due to imposed angular motion of the cam.
>
> 圆形凸轮的圆心与枢轴 $B$ 偏心，旋转时推动平面从动件做往复运动。偏心量 $e$ 决定气门升程。

---

**Eccentricity（偏心量）** [p.194]
> The eccentricity of the circular cam used in this study is varied from the nominal value $e_1 = 0.25$ cm to $e_2 = 0.35$ cm and $e_3 = 0.45$ cm.
>
> 偏心量是圆形凸轮的关键设计参数：凸轮圆心到枢轴 $B$ 的距离。增大偏心量会增加气门升程和速度/加速度幅值。

## 符号定义

### 通用建模符号

| 符号 | 类型 | 含义 |
|------|------|------|
| $nb$ | 标量，整数 | 模型中的刚体数目 |
| $nh$ | 标量，整数 | 独立约束方程的数目 |
| $nc$ | 标量，整数 | 广义坐标数目，$nc = 3nb$（平面） |
| $d$ | 标量，整数 | 自由度数，$d = 3nb - nh$ |

### §5.2 曲柄滑块机构

| 符号 | 类型 | 含义 |
|------|------|------|
| $\phi_1 = \pi/4 + \omega t$ | 驱动约束 | 曲柄转角 |
| $\omega_1 = 2\pi$, $\omega_2 = 4\pi$ | 标量，角速度 | 两种驱动速度 |
| $\ell_1 = 3.5$, $\ell_2 = 2.5$, $\ell_3 = 2.2$, $\ell_4 = 2.1$ | 标量，长度 | 四个连杆长度取值 |
| $x, \dot{x}, \ddot{x}$ | 标量 | 滑块的位置、速度、加速度 |

### §5.3 四连杆机构

| 符号 | 类型 | 含义 |
|------|------|------|
| $\phi_1 = \pi/2 + 2\pi t$ | 驱动约束 | 曲柄转角 |
| $\phi_3$, $\dot{\phi}_3$, $\ddot{\phi}_3$ | 标量 | 从动杆角度、角速度、角加速度 |
| $E$ | 点 | 连杆上的轨迹追踪点 |
| $\ell_1 = 3$, $\ell_2 = 2.5$, $\ell_3 = 2.2$, $\ell_4 = 2.1$ | 标量，长度 | 四个从动杆长度取值 |

### §5.4 快回机构

| 符号 | 类型 | 含义 |
|------|------|------|
| $\phi_3 = 0.44 + \omega t$ | 驱动约束 | 曲柄角度驱动 |
| $\omega_1 = 2\pi$, $\omega_2 = 4\pi$ | 标量，角速度 | 两种驱动速度 |
| $\ell_1 = 1.5$, $\ell_2 = 1.25$, $\ell_3 = 1.0$ | 标量，长度 | 三个曲柄长度设计参数 |

### §5.5 齿轮-滑块机构

| 符号 | 类型 | 含义 |
|------|------|------|
| $R_2 = 0.2$, $R_3 = 0.1$, $R_4 = 0.4$ | 标量，长度 | 三个齿轮的半径 |
| $\phi_2 = 4\pi t$ | 驱动约束 | 齿轮2角速度驱动 |
| $\phi_5 = \theta$ | 驱动约束 | 行程控制杆固定角度 |
| $\theta_1 = -0.1047$, $\theta_2 = 0$, $\theta_3 = 0.5236$ | 标量，角度 | 三个行程控制角度 |

### §5.6 气门挺杆机构

| 符号 | 类型 | 含义 |
|------|------|------|
| $\phi_2 = 40\pi t$ | 驱动约束 | 凸轮以 20 rev/s 旋转 |
| $e_1 = 0.25$, $e_2 = 0.35$, $e_3 = 0.45$ cm | 标量，长度 | 凸轮偏心量 |
| $R = 1.25$ cm | 标量，长度 | 凸轮半径 |
| $y_5$, $\dot{y}_5$, $\ddot{y}_5$ | 标量 | 气门杆位置、速度、加速度 |

## 核心论点

### §5.1 Modeling and Analysis Techniques — 运动学建模的四步方法论

本节提出了运动学建模的**四步通用方法论（Kinematic Modeling Recipe）**，核心思想是在使用 DADS 等计算机代码之前，先用**物理直觉**进行合理性检查：

1. **自由度计数检查**：$d = 3nb - nh$
2. **可行性检查**："若存在制造公差，系统能否装配？"
3. **物理推理判断奇异性**——Example 5.1.1 展示了通过物理直觉判断 Jacobian 奇异性

> **核心洞察**（Example 5.1.1 五杆平行四边形）：当 $\ell_3 = 1 + \epsilon$ 时，$\epsilon > 0$ 正常运行，$\epsilon = 0$ 时 $\phi_1 = \pi/2$ 为分叉点，$\epsilon < 0$ 时锁死。物理推理可以不计算 $15 \times 15$ Jacobian 的行列式即判定其奇异性。

### §5.2 Kinematic Analysis of a Slider-Crank Mechanism

#### 两种建模方案的等价性

| 比较项 | Model 1 | Model 2 |
|--------|---------|---------|
| 刚体数 | 4 | 2 |
| 广义坐标 $nc$ | 12 | 6 |
| 约束数 $nh$ | 11 | 5 |
| DOF | 1 | 1 |
| 连杆处理 | 独立刚体 | 复合 revolute-revolute joint |

两种模型给出**完全相同的分析结果**。Model 2 通过复合铰减小矩阵维度。

#### 装配分析的陷阱

若初始估计有符号错误（如滑块 $x$ 坐标取负），算法仍收敛，但收敛到一个**物理上不合理的构型**（连杆翻到地面下方）。必须目视检查装配结果。

#### DADS 分析结果

**驱动速度的影响**（$\omega_1 = 2\pi$ vs $\omega_2 = 4\pi$）：
- 位置：行程长度相同
- 速度：最大速度比约 2:1
- 加速度：最大加速度比约 **4:1**

> **关键发现**：速度翻倍导致加速度增至4倍（二次速度项 $\dot{\mathbf{q}}^2$ 主导），对轴承载荷影响远大于对位移和速度的影响。

**连杆长度的影响**（$\ell_1 = 3.5 \to \ell_4 = 2.1$）：
- 位置敏感度低，速度中等，**加速度极度敏感**——连杆缩短接近锁死构型时加速度急剧增大

#### §5.2.5 Lock-up Configuration

$\ell_5 = 1.9$（短于曲柄长度2）时，$t \approx 0.074$ s 锁死，速度和加速度趋于无穷大。

### §5.3 Kinematic Analysis of a Four-Bar Mechanism

#### Model 对比

| 比较项 | Model 1 | Model 2 |
|--------|---------|---------|
| 刚体数 | 4 | 3 |
| 广义坐标 $nc$ | 12 | 9 |
| 约束数 $nh$ | 11 | 8 |
| DOF | 1 | 1 |

#### 三个分析维度

1. **连杆点 $E$ 轨迹**（Fig. 5.3.5）：$\ell \to 2$ 时轨迹在最右端出现极端曲率——奇异性前兆
2. **从动杆角度 $\phi_3$ vs 曲柄角度 $\phi_1$**（Fig. 5.3.6）：$\ell \to 2$ 时出现极端变化
3. **从动杆角速度/角加速度 vs 时间**（Figs. 5.3.7-5.3.8）：加速度比角速度敏感性更强

> **跨案例统一结论**：**加速度对设计参数的敏感度远高于位置和速度**，源于加速度方程中 $\dot{\mathbf{q}}$ 的二次项和 Jacobian 接近奇异时 $\Phi_\mathbf{q}^{-1}$ 范数的急剧增大。

#### §5.3.5 Lock-up

从动杆缩短至 $\ell_3 = 1.9$ 时，$t \approx 0.18$ s 锁死。

### §5.4 Kinematic Analysis of a Quick-Return Mechanism

#### 建模复杂度跃升

| 比较项 | Model 1 | Model 2 |
|--------|---------|---------|
| 刚体数 | 6 | 4 |
| 广义坐标 $nc$ | 18 | 12 |
| 约束数 $nh$ | 17 | 11 |
| DOF | 1 | 1 |
| 简化方式 | — | $DE$ → R-R 复合铰, $C$ → R-T 复合铰 |

#### 关键发现

**速度/加速度倍增效应**：驱动速度倍增时，位移不变，峰值速度 ×2，峰值加速度 ×4。

**快回特性**（$\omega_1$ 驱动）：
- 切削行程占周期 **70%**，回程占 **30%**
- 切削时速度近似恒定
- $t = 0.5 \sim 0.6$ s 出现驻留

**设计变量分析**：曲柄长度减小 → 行程略减，切削/回程比不变，**峰值加速度显著降低**。

### §5.5 Kinematic Analysis of a Gear-Slider Mechanism

#### 最丰富的约束类型组合

| 约束类型 | 约束方程数 |
|---------|---------|
| 转动副 ×3 | 6 |
| 齿轮副 ×2 | 2 |
| 距离约束 ×3 | 3 |
| 移动副 ×1 | 2 |
| 地面约束 ×1 | 3 |
| **合计** | **16** |

$nc = 18$，**DOF = 2**（输入齿轮转速 + 行程控制杆角度）

#### 双驱动与行程控制

- $\phi_2 = 4\pi t$（齿轮恒速）+ $\phi_5 = \theta$（行程控制）
- $\theta$ 改变行程幅值，但速度/加速度的**归一化形状**保持一致

### §5.6 Kinematic Analysis of a Valve-Lifter Mechanism

#### 最多样的约束类型

| 约束类型 | 约束方程数 |
|---------|---------|
| 凸轮-平面从动件 ×1 | 1 |
| 转动副 ×2 | 4 |
| 移动副 ×2 | 4 |
| R-T 复合铰 ×2 | 2 |
| 地面约束 ×1 | 3 |
| **合计** | **14** |

$nc = 15$（5体），**DOF = 1**

#### 偏心量参数研究

三个偏心量（$e_1 = 0.25, e_2 = 0.35, e_3 = 0.45$ cm）：
- 位置/速度/加速度幅值均与偏心量近似成正比
- 圆形凸轮产生近似正弦的周期响应
- 实际发动机使用带凸角的近圆凸轮，产生更短开启持续角和明确的升程-停歇响应

### DADS Projects 概要

| 题号 | 机构 | 刚体数 | 关键约束类型 | 分析要求 |
|------|------|--------|-----------|--------|
| 5.1 | 薄膜从动件 | 4 | 转动副+凸轮 | 轨迹、速度、加速度，讨论奇异性 |
| 5.2 | 裁布机构 | 4 | 转动副 | 刀尖速度匹配分析 |
| 5.3 | 齿条-小齿轮 | 4→3 | 齿轮副+距离约束 | 完整模型 vs R-R 简化模型对比 |

## 本章五个案例的复杂度递进总结

| 案例 | 刚体 | DOF | 约束类型数 | 核心约束 | 新增分析维度 |
|------|------|-----|---------|---------|-----------|
| §5.2 曲柄滑块 | 4→2 | 1 | 3 | 转动+移动+地面 | 装配陷阱、速度/长度参数 |
| §5.3 四连杆 | 4→3 | 1 | 3 | 转动+地面(+R-R) | 连杆点轨迹、输入-输出函数 |
| §5.4 快回机构 | 6→4 | 1 | 4 | 转动+移动+R-R+R-T | 快回特性、驻留、设计变量 |
| §5.5 齿轮-滑块 | 6 | 2 | 5 | 齿轮+距离+转动+移动+地面 | 双驱动、行程控制 |
| §5.6 气门挺杆 | 5 | 1 | 6 | 凸轮+转动+移动+R-T+地面 | 凸轮参数（偏心量） |

> **章节核心结论**：笛卡尔坐标法的"约束库组装"思想具有强大的扩展能力——从最简单的4体/3种约束到6体/6种约束，建模方法论完全一致，只是约束方程数量增加。**加速度对设计参数的极端敏感性**是贯穿全章的核心发现，根源在于加速度方程的二次速度项和 Jacobian 在奇异附近的范数增长。

## 工程应用与实例

| 图号/表号 | 名称 | 类型 | 应用 | 关键知识点 |
|---------|------|------|------|-----------|
| Example 5.1.1 | 五杆平行四边形 | 方法论演示 | 建模检查 | DOF计数、分叉点、物理推理 |
| Fig. 5.2.1-5.2.14 | 曲柄滑块全流程 | 完整案例 | 内燃机 | 两种模型、装配、驱动、分析、锁死 |
| Fig. 5.3.1-5.3.9 | 四连杆全流程 | 完整案例 | 悬架/雨刮器 | 轨迹、传递函数、参数敏感性、锁死 |
| Fig. 5.4.1-5.4.9 | 快回机构全流程 | 完整案例 | 牛头刨床 | 快回比、驻留、加速度倍增 |
| Fig. 5.5.1-5.5.4 | 齿轮-滑块 | 完整案例 | 可变行程传动 | 双驱动、齿轮约束、行程控制 |
| Fig. 5.6.1-5.6.5 | 气门挺杆 | 完整案例 | 发动机配气 | 凸轮约束、偏心量参数 |
| Tables 5.2.1-5.6.5 | 全部数据表 | DADS 输入 | 通用 | 关节数据、装配结果 |
| Fig. P5.1-P5.3 | DADS 习题 | 综合练习 | 多种机构 | 建模+分析+物理解释 |
