---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 1
title: "Elements of Computer-Aided Kinematics and Dynamics"
pages: 1-17
sections:
  - "1.1 Scope of Mechanical System Kinematics and Dynamics"
  - "1.2 Conventional Methods of Kinematic and Dynamic Analysis"
  - "1.3 Objective of Computational Kinematics and Dynamics"
  - "1.4 Guide to the Text Contents"
created: 2026-05-14
last_updated: 2026-05-14
---

# Chapter 1: Elements of Computer-Aided Kinematics and Dynamics

## 章节定位

第一章是全书的**导论章节**（pp.1-17），不包含正式的数学推导。其核心目的是：
1. 定义学科范围（机械系统运动学与动力学）
2. 通过12个工程实例展示应用广度
3. 对比传统方法与计算方法的差异，论证计算方法的必要性
4. 以滑块-曲柄为例预览两种坐标方法
5. 概述全书章节组织

---

## 概念定义

### 核心概念

**Mechanical System（机械系统）** [p.1]
> A collection of interconnected rigid bodies that can move relative to one another, consistent with joints that limit relative motion of pairs of bodies.
>
> 由关节连接的互联刚体集合，刚体可相对运动，关节限制成对刚体间的相对运动。

**特征**：大幅运动（large amplitude motion）导致**几何非线性**，反映在约束的代数方程和运动的微分方程中。

---

**Kinematic Analysis（运动学分析）** [p.2]
> Concerns the motion of a mechanical system independent of forces that produce the motion. Typically, the time history of position or relative position of one or more bodies in the system is prescribed. Time histories of position, velocity, and acceleration of the remaining bodies are then determined by solving systems of nonlinear algebraic equations for position and linear algebraic equations for velocity and acceleration.
>
> 与力无关的运动分析。规定部分构件的位置/相对位置时间历程，通过求解非线性代数方程（位置）和线性代数方程（速度、加速度）确定其余构件的运动。

---

**Dynamic Analysis（动力学分析）** [p.2]
> Concerns the motion of the system that is due to the action of applied forces. A special case of dynamic analysis is the determination of an equilibrium position of the system under the action of forces that are independent of time. The motion of the system, under the action of applied forces, is required to be consistent with kinematic relations that are imposed on the system by joints that connect bodies in the system. The equations of dynamics are differential equations or a combination of differential and algebraic equations.
>
> 由施加力引起的系统运动。特殊情况为静力平衡分析。运动须满足关节施加的运动学约束。方程为微分方程或微分-代数方程的组合。

---

**Inverse Dynamic Analysis（逆动力学分析）** [p.2]
> A hybrid form of kinematic and dynamic analysis in which the time history of positions or relative positions of one or more bodies in the system is prescribed, leading to complete determination of position, velocity, and acceleration of the system from the equations of kinematics. The equations of motion of the system are then solved, with known position, velocity, and acceleration, as algebraic equations to determine the forces that are required to generate the prescribed motion.
>
> 运动学与动力学的混合形式。已知运动历程→先由运动学方程求解完整的位置/速度/加速度→再将运动方程作为代数方程求解所需的力。

---

**Compliant Elements（柔顺元件）** [p.2]
> An important class of forces that act in a mechanical system is associated with compliant elements, such as coil springs, leaf springs, tires, shock absorbers, and a multitude of other deformable components that have reaction forces and moments associated with them. Forces due to compliant elements act between bodies in the system and are functions of their relative position and velocity.
>
> 弹簧、减震器、轮胎等可变形构件，产生的力/力矩是构件间相对位置和速度的函数。

---

**Slider-Crank Mechanism（滑块-曲柄机构）** [p.3]
> The crankshaft-connecting rod-piston assembly. The basic purpose of this mechanism is to transfer forces that are induced by combustion of fuel on the pistons into torques that act about the axis of rotation of the crankshaft.
>
> 曲轴-连杆-活塞组件。该机构的基本用途是将燃料在活塞上燃烧产生的力转化为作用在曲轴旋转轴上的扭矩。

---

**Four-Bar Linkage（四杆连杆机构）** [p.5]
> A mechanism commonly encountered in mechanical design, such as the vehicle-suspension application (Fig. 1.1.4). Made up of upper and lower control arms that are pivoted in rotational joints in the frame and in the wheel assembly.
>
> 机械设计中常见的机构，如车辆悬架应用（Fig. 1.1.4）。由上、下控制臂组成，分别通过转动副铰接在车架和车轮总成上。

---

**Compound Mechanisms（复合机构）** [p.9]
> Made up from combinations of many of the basic kinematic couplings. Example: the quick-return shaper mechanism (Fig. 1.1.8), which combines gears, rotational joints, and translational joints.
>
> 由多种基本运动副组合而成。例如：快速回程成型机构（Fig. 1.1.8），组合了齿轮、转动副和移动副。

---

**Lagrangian Generalized Coordinate（拉格朗日广义坐标）** [p.14]
> An independent generalized coordinate; the minimum number of variables needed to describe the system configuration. For the slider-crank: the crank angle $\theta$ (as long as $\ell > r$) is the single independent coordinate.
>
> 独立广义坐标。以最少的变量描述系统构型。对滑块-曲柄：在 $\ell > r$ 条件下，曲柄角 $\theta$ 是唯一的独立坐标。

---

**Cartesian Generalized Coordinates（笛卡尔广义坐标）** [p.14]
> Position and orientation coordinates of individual bodies, taken as generalized coordinates. For the slider-crank: $\phi_1$ (crank orientation), $x_2, y_2$ (center of mass of connecting rod), and $\phi_2$ (connecting rod orientation) — four variables constrained by three kinematic constraint equations.
>
> 各构件的位置和姿态坐标作为广义坐标。变量数多于自由度数，需要约束方程补充。

---

**Differential-Algebraic Equations, DAE（微分-代数方程）** [p.15]
> A mixed system of differential-algebraic equations that must be solved to determine the motion of the system. The form of this large number of equations is simple, however, permitting computer generation and solution.
>
> 微分方程与代数约束方程的混合系统。方程数多但形式简单，适合计算机自动生成与求解。

---

## 符号定义

> [!note]
> 第一章的符号均为**示例性引入**，仅在 Sec. 1.3 的滑块-曲柄例子中出现。全书的正式符号体系从第2章开始建立。

### Sec. 1.3 滑块-曲柄模型符号

#### 拉格朗日方法（Fig. 1.3.1）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\theta$ | 标量，角度 | 曲柄角（拉格朗日独立广义坐标） |
| $\psi$ | 标量，角度 | 连杆与水平方向的夹角 |
| $r$ | 标量，长度 | 曲柄半径 |
| $\ell$ | 标量，长度 | 连杆全长 |
| $\ell_1$ | 标量，长度 | 从曲柄铰接点到连杆质心的距离 |
| $x_2, y_2$ | 标量，坐标 | 连杆（body 2）质心在全局坐标系下的位置 |

> **条件**：当 $\ell > r$ 时，$\theta$ 可作为独立广义坐标，$\psi$、$x_2$、$y_2$ 均可由 $\theta$ 解析确定。

#### 笛卡尔坐标方法（Fig. 1.3.2）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\phi_1$ | 标量，角度 | 曲柄（body 1）的角度坐标 |
| $\phi_2$ | 标量，角度 | 连杆（body 2）的角度坐标 |
| $x_2, y_2$ | 标量，坐标 | body 2 质心在全局系下的位置坐标 |
| $A_1$ | 点 | 曲柄上与连杆的铰接点 |
| $A_2$ | 点 | 连杆上与曲柄的铰接点（$A_1 = A_2$ 为转动副约束） |
| $B_2$ | 点 | 连杆上与滑块连接的点 |

> **关系**：4个笛卡尔广义坐标 $(\phi_1, x_2, y_2, \phi_2)$ 受3个代数约束方程约束（2个来自转动副 $A_1 = A_2$，1个来自滑块 $B_2$ 的 $y$ 坐标为零）。

### 其他零散符号

| 符号 | 出现位置 | 含义 |
|------|---------|------|
| $\omega$ | Fig. 1.1.3 飞球调速器 | 转轴角速度 |
| $s$ | Fig. 1.1.3 飞球调速器 | 套筒沿轴向的位移 |
| $q_1 \sim q_7$ | Fig. 1.1.9 机器人操纵器 | 7个自由度（$q_1$ 基座旋转，$q_2$ 枢轴臂旋转，$q_3$ 伸缩臂平移，$q_4$ 腕部旋转，$q_5$ 腕部俯仰，$q_6$ 手部旋转，$q_7$ 手指开合） |

---

## 核心论点

### 三种分析类型的对比

| 分析类型 | 已知量 | 求解量 | 方程类型 |
|---------|--------|--------|---------|
| 运动学分析 | 部分构件的运动历程 | 其余构件的位置、速度、加速度 | 非线性代数（位置）+ 线性代数（速度/加速度） |
| 动力学分析 | 外力 + 初始条件 | 系统完整运动 + 约束力 | 微分方程 或 微分-代数方程 |
| 逆动力学分析 | 完整运动历程 | 产生该运动所需的力 | 先运动学方程（代数）→ 再运动方程（代数） |

### 力的分类体系

作用在机械系统上的力按来源分为：
1. **重力**（Gravitational Force）：恒定，垂直地表
2. **气动力**（Aerodynamic Forces）：与环境交互
3. **摩擦力与阻尼力**（Friction and Damping）：与构件相对运动相关
4. **柔顺元件力**（Compliant Element Forces）：弹簧、减震器等，是相对位置和速度的函数
5. **控制力**（Control Forces）：电气和液压反馈控制子系统产生

### 传统方法 vs 计算方法

| 维度 | 传统方法（"巧妙公式化"） | 计算方法（"系统化"） |
|------|---|---|
| **思路** | 针对特定系统利用技巧简化 | 统一框架处理所有系统 |
| **变量** | 最小独立变量集（Lagrangian） | 冗余变量 + 约束方程（Cartesian） |
| **推导** | 人工推导，依赖技巧和直觉 | 计算机自动生成 |
| **适用性** | 仅限简单系统（3-4 DOF） | 几乎无限制 |
| **方程规模** | 小 | 大（代价） |
| **可扩展性** | 差 | 好 |
| **类比** | 手工解电路 | 有限元 / SPICE 电路仿真 |

### 两种坐标方法的对比

| 特性 | 相对坐标法 | 笛卡尔坐标法（本书采用） |
|------|-----------|----------------------|
| 发展时期 | 1960s-1970s初 [15-17] | 1970s末 [18-20] |
| 变量数目 | 最小集（= DOF数） | 冗余（$3n_b$ 平面 / $7n_b$ 空间） |
| 拓扑分析 | 需要 | **不需要** |
| 约束/力施加 | 复杂 | **简单直观** |
| 通用性 | 受限 | **几乎无限制** |
| 方程规模 | 小 | 大 |
| 软件实现 | 复杂 | **模块化、易实现** |

---

## 工程应用实例总览

第一章通过12幅图示覆盖了机械系统的典型应用：

### 基本机构

| 图号 | 机构 | 类型 | 应用 | 关键知识点 |
|------|------|------|------|-----------|
| Fig. 1.1.1 | V-8 发动机截面 | 滑块-曲柄 + 凸轮从动件 | 内燃机 | 多种运动副共存 |
| Fig. 1.1.2 | 冲压机构 | 滑块-曲柄 | 金属冲压 | 力的放大（小力矩→大冲压力） |
| Fig. 1.1.3 | 飞球调速器 | 空间滑块-曲柄 | 发动机转速控制 | 离心力平衡 + 反馈控制 |
| Fig. 1.1.4 | 悬架连杆 | 四杆机构 | 车辆悬架 | 弹簧/阻尼柔顺元件 |
| Fig. 1.1.5 | 雨刮器机构 | 双四杆连杆 | 汽车雨刮 | 曲柄旋转→摇臂往复 |
| Fig. 1.1.6 | 物料搬运机构 | 四杆连杆 | 工厂自动化 | 尺寸设计的重要性 |
| Fig. 1.1.7 | 齿轮对 | 齿轮传动 | 速度/力矩变换 | 齿轮比关系 |

### 复合机构

| 图号 | 机构 | 类型 | 应用 | 关键知识点 |
|------|------|------|------|-----------|
| Fig. 1.1.8 | 快速回程成型机 | 齿轮+四杆+滑块 | 金属切削 | 切削慢速、回程快速 |
| Fig. 1.1.9 | 机器人操纵器 | 串联开链，9体7DOF | 工业机器人 | 多自由度空间运动 |
| Fig. 1.1.10 | 汽车整车 | 复合空间机构 | 车辆动力学 | 前/后悬架系统 |
| Fig. 1.1.11 | McPherson支柱前悬 | 空间机构 | 前轮悬架 | 球铰+移动副+拉杆 |
| Fig. 1.1.12 | 汽车悬架示意 | 空间机构 | 前+后悬架总成 | 拖臂后悬架 |

---

## Sec. 1.3 滑块-曲柄建模对比（核心预览）

本节以简化的滑块-曲柄（Fig. 1.3.1, 1.3.2）为例，预览了全书的两条技术路线：

### 拉格朗日方法（传统）

- 选取曲柄角 $\theta$ 为唯一独立广义坐标
- 在 $\ell > r$ 条件下，通过三角关系解析确定 $\psi$、$x_2$、$y_2$
- 推导出**单个高度非线性的二阶ODE**
- 缺点：推导复杂，难以推广

### 笛卡尔坐标方法（本书采用）

- 将两个刚体视为**解耦的**（Fig. 1.3.2）
- 4个广义坐标：$\phi_1, x_2, y_2, \phi_2$
- 3个代数约束方程：
  - 转动副约束（$A_1 = A_2$）：2个方程
  - 滑块约束（$B_2$ 的 $y$ 坐标为零）：1个方程
- 用 Lagrange 乘子法得到：**4个二阶微分方程 + 3个代数约束方程 + 3个 Lagrange 乘子**
- 构成 **DAE（微分-代数方程组）**
- 优点：形式简单统一，适合计算机自动生成与求解

> **核心洞察**：方程数量更多，但每个方程的形式简单且可模块化生成——这正是"系统化方法"的核心优势。

---

## 全书结构导读（Sec. 1.4）

### Part One: 平面系统 (Chapters 2-8)

| 章 | 内容 | 作用 |
|----|------|------|
| Ch.2 | 平面向量、矩阵和微分学 | **数学基础**：向量代数矩阵表示、微分、虚位移 |
| Ch.3 | 平面笛卡尔运动学公式化 | **约束方程库**：标准约束、位置/速度/加速度方程 |
| Ch.4 | 运动学分析的计算方法 | **数值方法**：方程组装、矩阵运算、Newton-Raphson |
| Ch.5 | 平面运动学建模与分析 | **应用**：DADS代码实例，含病态模型分析 |
| Ch.6 | 平面动力学方程推导 | **理论核心**：Newton定律→虚功→Lagrange乘子法 |
| Ch.7 | 运动方程数值求解 | **DAE求解**：坐标分区、数值积分、约束稳定化 |
| Ch.8 | 平面动力学建模与分析 | **应用**：设计变量对动力学性能的影响 |

### Part Two: 空间系统 (Chapters 9-12)

| 章 | 内容 | 作用 |
|----|------|------|
| Ch.9 | 空间位置与姿态理论 | Euler参数、旋转矩阵、空间运动学基础 |
| Ch.10 | 空间运动学建模与分析 | 空间关节库、运动学求解、DADS实例 |
| Ch.11 | 空间多体运动方程推导 | 空间虚功原理、空间DAE |
| Ch.12 | 空间动力学建模与分析 | 车辆动力学等工程实例 |

> **组织逻辑**：先平面后空间——平面分析复杂度低，概念更易掌握；空间系统是平面系统的**解析和代数扩展**，方法论完全一致。有空间系统经验的读者可直接跳到Part Two。

---

## 与全书的关系

第一章引入的概念和方法论框架在后续章节中的对应关系：

| 第一章概念 | 后续展开位置 |
|-----------|------------|
| 机械系统定义、关节约束 | Ch.3（平面约束库）、Ch.9-10（空间约束库） |
| 运动学分析三级求解 | Ch.3-4（公式化+计算方法）、Ch.10 |
| 动力学分析、DAE | Ch.6-7（推导+求解）、Ch.11-12 |
| 逆动力学分析 | Ch.6（静力平衡+逆动力学方法） |
| 柔顺元件力 | Ch.6, 8（弹簧/阻尼器建模） |
| 拉格朗日 vs 笛卡尔坐标 | Ch.3 vs Ch.6（系统性对比） |
| DADS 软件 | Ch.5, 8, 10, 12（应用实例） |
