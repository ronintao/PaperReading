---
type: glossary
parent: computer-aided-kinematics-and-dynamics
title: "术语中英对照表 (Terminology Glossary)"
created: 2026-06-09
last_updated: 2026-06-09
---

# 术语中英对照表（Terminology Glossary）

> 本表用于统一 *Computer Aided Kinematics and Dynamics of Mechanical Systems* 全套阅读笔记的中文译名。
> **规则**：撰写笔记时，术语**首次出现**标注英文原文，如"构型（configuration）"；后续仅用中文。
> 新增术语请追加到对应分类并保持字母序。

## 一、基础概念 (Fundamentals)

| English | 中文（统一译名） | 备注 / 不采用的译法 |
|---------|----------------|--------------------|
| body | 物体 / 刚体 | 上下文明确时用"刚体" |
| body-fixed reference frame | 随体参考系 | 不用"体固定坐标系" |
| configuration | **构型** | **不用**"位形" |
| degrees of freedom (DOF) | 自由度 | $\text{DOF}=nc-nh$ |
| generalized coordinates | 广义坐标 | |
| independent / dependent (coordinates) | 独立 / 非独立（坐标） | **不用**"相依"；约束一般非线性，故也不用"线性相关/无关" |
| kinematics | 运动学 | |
| dynamics | 动力学 | |
| kinematic analysis | 运动学分析 | |
| kinematic synthesis | 运动学综合 | |
| mechanism | 机构 | |
| rigid body | 刚体 | |
| structure | 结构 | 只传载、抗动，区别于机构 |

## 二、关节与约束 (Joints & Constraints)

| English | 中文（统一译名） | 备注 / 不采用的译法 |
|---------|----------------|--------------------|
| joint | **关节** | **不用**"铰""运动副"；首次标注 (joint) |
| physical joint | 物理关节 | |
| geometry of the joint | 关节的几何 | |
| revolute joint | 转动关节 | 首次可标 (revolute joint) |
| translational joint | 移动关节 | |
| gear constraint | 齿轮约束 | |
| cam constraint | 凸轮约束 | |
| composite constraint | 复合约束 | |
| constraint equation | 约束方程 | |
| holonomic constraint | 完整约束 | |
| nonholonomic constraint | 非完整约束 | |
| stationary constraint | 定常约束 | 不显含时间 |
| time-dependent constraint | 时变约束 | 显含时间 |
| absolute constraint | 绝对约束 | 体与地面 |
| relative constraint | 相对约束 | 体与体 |
| driving constraint | 驱动约束 | |
| kinematically driven | 运动学驱动的 | |
| driver | 驱动器 | |

## 三、数学与求解 (Math & Solution)

| English | 中文（统一译名） | 备注 / 不采用的译法 |
|---------|----------------|--------------------|
| Jacobian (matrix) | 雅可比（矩阵） | $\boldsymbol{\Phi}_\mathbf{q}$ |
| singular / nonsingular | 奇异 / 非奇异 | |
| singular configuration | 奇异构型 | |
| determinant | 行列式 | |
| position equation | 位置方程 | |
| velocity equation | 速度方程 | $\boldsymbol{\Phi}_\mathbf{q}\dot{\mathbf{q}}=\boldsymbol{\nu}$ |
| acceleration equation | 加速度方程 | $\boldsymbol{\Phi}_\mathbf{q}\ddot{\mathbf{q}}=\boldsymbol{\gamma}$ |
| chain rule (of differentiation) | 链式法则 | |
| coefficient matrix | 系数矩阵 | |
| Newton–Raphson | 牛顿-拉夫森 | N-R |
| differential-algebraic equations (DAE) | 微分-代数方程 | |
| Lagrange multiplier | 拉格朗日乘子 | |
| reference frame | 参考系 | |
| transformation matrix | 变换矩阵 | $\mathbf{A}(\phi)$ |
| rotation / orientation | 转动 / 朝向 | |

## 四、机构实例 (Mechanism Examples)

| English | 中文（统一译名） | 备注 |
|---------|----------------|------|
| simple pendulum | 单摆 | |
| slider–crank (mechanism) | 曲柄滑块（机构） | |
| crank | 曲柄 | |
| coupler | 耦合体 / 连杆 | |
| linkage | 连杆机构 | |
| four-bar (linkage) | 四连杆（机构） | |
| quick-return | 快回（机构） | |
| cam-follower | 凸轮-挺杆 | |
| slider | 滑块 | |
| slide axis | 滑轨 | |

---

## 维护说明

- 与既有笔记冲突时，**以本表为准**，并回头修订旧笔记（如 `joint` 已从"铰"统一为"关节"、`configuration` 已从"位形"统一为"构型"）。
- 同一英文若在不同语境有不同中文（如 body=物体/刚体、coupler=耦合体/连杆），在"备注"列注明取舍条件。
