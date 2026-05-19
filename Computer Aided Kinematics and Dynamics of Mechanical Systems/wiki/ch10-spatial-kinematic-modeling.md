---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 10
title: "Spatial Kinematic Modeling and Analysis"
pages: 393-415
sections:
  - "10.1 Modeling and Analysis Techniques"
  - "10.2 Kinematic Analysis of a Spatial Slider-Crank Mechanism"
  - "10.3 Kinematic Analysis of a Spatial Four-Bar Mechanism"
  - "10.4 Kinematic Analysis of an Air Compressor"
created: 2026-05-19
last_updated: 2026-05-19
---

# Chapter 10: Spatial Kinematic Modeling and Analysis

## 章节定位

本章是 Part Two（空间系统）的**核心应用章节**，与 Part One 中 Ch.5（Planar Kinematic Modeling and Analysis）完全对应。Ch.9 建立了空间运动学的理论框架（Euler 参数、运动副约束方程库、三段求解流程），本章将其付诸实践，通过三个工程案例展示空间系统建模中的关键技术：

1. **约束冗余的识别与处理**（§10.1）——空间系统独有的核心挑战
2. **正确的关节建模策略**（§10.2-10.4）——用球铰、复合关节和距离约束替代冗余的转动副
3. **参数研究与设计优化**（§10.2.4, §10.4.4）——连杆长度/偏置角对性能的影响

本章不涉及动力学（属于 Ch.11-12），也不涉及数值方法的细节（Ch.4/7已覆盖），专注于建模策略和运动学结果的验证。

---

## 概念定义

**Constraint Redundancy（约束冗余）** [p.393]
> In spatial systems, it is easy to implement what appear to be proper constraints, only to find that redundancies exist.
>
> 在空间系统中，看起来合理的约束很容易实际上存在冗余——即约束方程的数量超过了独立约束的数量。这是平面系统与空间系统建模的**核心差异**。

---

**Manufacturing Imperfection Test（制造缺陷测试）** [p.393]
> As an alternative check on redundancy, the *manufacturing imperfection test* outlined in step 1(b) of the procedure suggested in Section 5.1 can be applied.
>
> 作为冗余性的替代检查方法，可以应用 §5.1 中步骤 1(b) 所建议的"制造缺陷测试"——即假设机构的制造存在微小偏差（轴线不平行、点不共面等），观察系统能否仍然装配，从而识别隐含的冗余约束。若不能装配→存在冗余。

---

**Lock-up Configuration（锁死构型）** [p.399]
> Lock-up occurs when the length of the connecting rod is less than 0.2362 m, as shown in Fig. 10.2.2.
>
> 锁死构型发生在连杆长度小于临界值（此例为 0.2362 m）时，机构无法完成完整运动循环，Jacobian 奇异。

---

**Spherical-Spherical Composite Joint（球-球复合关节）** [p.404]
> In model 2 (Fig. 10.3.2), link BC is modeled as the coupler in a spherical-spherical composite joint. The length of the link is the distance between points P₁ and P₂.
>
> 球-球复合关节将一根连杆简化为两端球铰之间的距离约束（仅1个方程），省去了将连杆建模为独立刚体所需的7个广义坐标和额外约束。连杆长度即为两球心之间的固定距离。

---

**Joint Reference Triad（关节参考三点组）** [p.396]
> To define a kinematic joint, six points (three points on each body) are chosen, depending on the type of joint that is intended. These points, P_i, Q_i, R_i, P_j, Q_j, and R_j, defined in their respective centroidal body-fixed reference frames on bodies i and j, form joint reference triads.
>
> 为定义运动副，在每个体上选取三个点（P, Q, R），它们在体固坐标系中给出。P 定位关节位置，向量 PQ 定义关节 z" 轴（旋转轴或滑动方向），R 定义 x" 轴方向。六个点完整定义一个运动副的几何。

---

**Offset Angle（偏置角）** [p.409]
> The disk is connected to the rotor by a revolute joint whose axis of rotation is perpendicular to the disk and 30° from the axis of the rotor. Canting of the disk generates reciprocating motion of the pistons.
>
> 偏置角是指盘片旋转轴与转子旋转轴之间的夹角。盘片因偏置而产生"摆动"（wobble），将转子的旋转运动转化为活塞的往复运动。偏置角越大，活塞行程、速度和加速度峰值越大。

---

**Position Absolute Constraint（位置绝对约束）** [p.409]
> The disk is prevented from rotating by an x position absolute constraint at point O, which models a slot in the disk through which a bar parallel to the global y axis passes.
>
> 位置绝对约束固定某体上某点的一个坐标分量（此处为 x 坐标），物理上对应盘片中的槽与固定导杆配合，阻止盘片绕自身轴旋转。

---

## 符号定义

### 通用符号

| 符号 | 类型 | 含义 |
|------|------|------|
| $nc$ | 标量，整数 | 广义坐标总数（= 7 × 体数） |
| $nh$ | 标量，整数 | 约束方程总数 |
| $\text{DOF} = nc - nh$ | 标量，整数 | 自由度 |
| $P_i, Q_i, R_i$ | 三维向量（体坐标系） | 体 $i$ 上的关节参考三点 |
| $\mathbf{P}_i\mathbf{Q}_i$ | 向量 | 定义关节 z" 轴方向 |
| $R_i$ | 点 | 定义关节 x" 轴方向 |

### §10.2 空间曲柄滑块

| 符号 | 类型 | 含义 |
|------|------|------|
| $\ell$ | 标量，长度 | 连杆长度（参数研究变量：0.3, 0.27, 0.24 m） |
| $\omega_0 = 2\pi$ rad/s | 标量，角速度 | 曲柄转速 |
| $\theta = 2\pi t$ | 时间函数 | 驱动约束（曲柄匀速旋转 1 rev/s） |
| $\ell_{crit} = 0.2362$ m | 标量，长度 | 锁死临界连杆长度 |

### §10.3 空间四连杆

| 符号 | 类型 | 含义 |
|------|------|------|
| Link 1 (AB) | 体①，长度 2.0 | 输入杆（曲柄） |
| Link 2 (BC) | 体②，长度 12.19 | 耦合杆 |
| Link 3 (CD) | 体③ | 输出杆（摇杆） |
| Ground (AD) | 体④ | 机架 |
| $\theta = \pi t$ | 时间函数 | 驱动约束（$\omega_0 = \pi$ rad/s，0.5 rev/s） |

### §10.4 空气压缩机

| 符号 | 类型 | 含义 |
|------|------|------|
| Ground ① | 体 | 机架/气缸壁 |
| Rotor ② | 体 | 转子 |
| Disk ③ | 体 | 斜盘（wobble plate） |
| Piston 1~6 ④~⑨ | 体 | 六个活塞 |
| $R = 0.2$ m | 标量 | 盘片上连杆附着点的圆周半径 |
| $L = 0.5$ m | 标量 | 连杆长度（球-球距离约束） |
| offset angle | 标量 | 盘片轴与转子轴夹角（参数：20°, 30°, 40°） |
| $\theta = 62.832t$ | 时间函数 | 转子驱动（600 rpm = $20\pi$ rad/s） |
| $O$ | 点（体③） | 位置绝对约束点（$x_O = 0$） |

---

## 核心论点

### §10.1 建模与分析技术——约束冗余

**核心命题**：空间系统建模的关键挑战不是写约束方程本身（与平面完全一致），而是**识别和处理约束冗余**。

**Example 10.1.1**（空间曲柄滑块，Fig. 10.1.1）完整分析：

| 项目 | 计数 |
|------|------|
| 4 体 × 7 坐标 | $nc = 28$ |
| 3 转动副 × 5 + 1 移动副 × 5 + 6 地面 + 4 Euler | $nh = 30$ |
| 表观 DOF = 28 - 30 | **-2** |
| 实际 DOF | **1** |
| **冗余约束数** | **3** |

冗余来源：
1. 三个转动副轴线平行 → A, B 处的平行性自动保证 C 处平行 → **2 个冗余**
2. 共面运动要求 → C 处 z 坐标约束自动满足 → **1 个冗余**

**制造缺陷测试**验证（Fig. 10.1.2）：
- 将 A 处轴线微偏 → C 处无法对齐 → 无法装配 → 确认冗余
- 中心点偏离 y-z 平面 → 第3个冗余度

**错误的"修复"（Fig. 10.1.3）**：
- 用圆柱副替代 C 处转动副 + 用绝对约束替代移动副
- 计数正确（DOF=1），但引入了**非期望的额外自由度**（体3绕圆柱副轴自转）
- **教训：仅靠约束计数不够，必须结合制造缺陷测试**

### §10.2 空间曲柄滑块——正确建模与参数研究

**正确模型**（Fig. 10.2.1）的关键技巧：

| 关节 | 类型 | 约束数 | 替代的原始关节 |
|------|------|--------|-------------|
| A（曲柄-地面）| 转动副 | 5 | — |
| B（曲柄-连杆）| **球铰** | 3 | 转动副(5) |
| C（连杆-滑块）| **转动-圆柱副** | 3 | 转动副(5) |
| D（滑块-地面）| 移动副 | 5 | — |
| B-C 距离 | **距离约束** | 1 | — |

总约束 27（而非30），DOF = 28 - 27 = 1，无冗余。

**策略**：用球铰(3) + 转动-圆柱副(3) + 距离约束(1) 合计 7 个约束，替代两个转动副(10)，净减 3 个约束——恰好消除 3 个冗余。

**参数研究**（连杆长度 $\ell$ = 0.3, 0.27, 0.24 m）：
- $\ell$ 越短 → 运动越不对称 → 速度/加速度峰值越高
- $\ell < 0.2362$ m → **锁死**（Jacobian 奇异，Newton-Raphson 不收敛）
- $\ell = 0.24$ m（接近临界）→ 加速度峰值 ~13 m/s²（接近奇异的"放大效应"）

### §10.3 空间四连杆——等效建模验证

两种建模方案的对比：

| 特性 | Model 1（4体） | Model 2（3体） |
|------|--------------|--------------|
| 体数 | 4 | 3 |
| 广义坐标 $nc$ | 28 | 21 |
| 关节组合 | Rev-Univ-Sph-Rev | Rev-SphSph-Rev |
| 约束数 $nh$ | 27 | 20 |
| DOF | 1 | 1 |
| 计算规模 | 较大 | **较小**（减少 25%） |
| 运动学结果 | 基准 | **完全一致** |

**关键结论**：当连杆两端均为球铰（或等效的万向节+球铰组合允许自转）时，可以用球-球复合关节替代独立体建模，结果完全等价但计算量显著减小。

### §10.4 空气压缩机——大型系统的系统化建模

**系统规模**：9 体、63 坐标、62 约束、DOF=1

**建模策略总结**：

| 连接 | 关节类型 | 约束数 | 理由 |
|------|---------|--------|------|
| Rotor-Ground (A) | 转动副 | 5 | 标准旋转 |
| Disk-Rotor (B) | 转动副（轴倾斜） | 5 | 产生摆动 |
| Disk-Pistons ×6 | 球-球复合关节 | 6×1=6 | 连杆简化 |
| Pistons-Ground ×6 | 移动副 | 6×5=30 | 直线往复 |
| Disk 点O | 位置绝对约束 | 1 | 阻止自转 |
| Ground | 地面约束 | 6 | 固定机架 |
| 所有体 | Euler 归一化 | 9 | 姿态约束 |

**参数研究**（offset angle = 20°, 30°, 40°）：

| 指标 | 20° | 30° | 40° |
|------|-----|-----|-----|
| 活塞行程 | ~0.12 m | ~0.20 m | ~0.32 m |
| 峰值速度 | ~4 m/s | ~6 m/s | ~10 m/s |
| 峰值加速度 | ~200 m/s² | ~400 m/s² | ~800 m/s² |
| 波形 | 近似正弦 | 轻微畸变 | 显著非正弦 |

**设计权衡**：偏置角↑ → 排量↑ → 但动载荷急剧增大（非线性关系）。40°时加速度峰值是20°的4倍。

---

## 工程应用与实例

| 图号/例题号 | 名称 | 类型 | 应用领域 | 关键知识点 |
|------------|------|------|---------|-----------|
| Ex. 10.1.1 / Fig. 10.1.1-10.1.3 | 空间曲柄滑块冗余分析 | 约束诊断 | 方法论 | 平行轴→冗余；制造缺陷测试；错误修复引入额外DOF |
| §10.2 / Fig. 10.2.1 | 空间曲柄滑块（4体） | 完整建模+分析 | DADS 建模 | 球铰+转动圆柱副+距离约束消冗余 |
| Fig. 10.2.2 | 锁死构型 | 奇异分析 | 连杆设计 | $\ell < 0.2362$ m 时锁死 |
| Fig. 10.2.3-10.2.5 | 位置/速度/加速度曲线 | 参数研究 | 设计优化 | 接近奇异时加速度放大 |
| §10.3 / Fig. 10.3.1-10.3.2 | 空间四连杆（两种模型） | 等效验证 | 建模选择 | 4体 vs 3体，球-球替代完全等价 |
| Fig. 10.3.3-10.3.5 | 点B/体3 运动曲线 | 运动分析 | 空间运动特征 | 两模型结果完全一致 |
| §10.4 / Fig. 10.4.1 | 空气压缩机（9体） | 大型系统 | 斜盘式压缩机 | 63坐标/62约束/球-球连杆/位置约束防转 |
| Fig. 10.4.2-10.4.4 | 活塞位置/速度/加速度 | 参数研究 | 压缩机设计 | 偏置角vs行程/载荷权衡 |
| Prob. 10.1 | 3体曲柄滑块 | 习题 | 简化验证 | 球-球替代连杆体→等价 |
| Prob. 10.2 | 15体压缩机 | 习题 | 复杂建模 | 万向节控制连杆自转 |

---

## 与全书的关系

| 本章概念 | 前置章节 | 后续应用 |
|----------|---------|---------|
| 约束冗余识别 | Ch.5 §5.1（平面冗余，制造缺陷测试） | Ch.11-12（空间动力学建模同样需要） |
| 球-球复合关节 | Ch.9 §9.4（空间运动副定义） | Ch.12（空间动力学中的连杆简化） |
| 转动-圆柱副 | Ch.9 §9.4.9（Rev-Cyl 定义与约束方程） | Ch.11（作为标准"积木"） |
| 关节参考三点组 P,Q,R | Ch.9 §9.4（所有运动副的统一描述方式） | Ch.11-12（DADS 输入格式） |
| 装配分析 + Newton-Raphson | Ch.4（N-R 收敛性）；Ch.5（平面装配） | Ch.12（空间动力学初始条件） |
| 锁死/奇异构型 | Ch.5 §5.2-5.4（平面锁死/分叉） | Ch.12（动力学仿真中的奇异处理） |
| 偏置角参数研究 | — | Ch.12（动力学载荷研究） |

**承上启下定位**：
- **承上**：本章直接使用 Ch.9 建立的空间运动副约束方程库和 Ch.4/5 的建模方法论（§5.1 的约束检查流程）
- **启下**：本章的三个模型将在 Ch.12（空间动力学建模与分析）中重新出现——加上质量/惯性张量后进行动力学仿真
- **对应关系**：Ch.5:Ch.3 = Ch.10:Ch.9（理论→应用案例的跨越）
