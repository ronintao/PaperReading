---
type: index
title: "Computer Aided Kinematics and Dynamics of Mechanical Systems, Volume I: Basic Methods"
wiki_language: zh-CN
last_updated: 2026-05-18
---

# 论文解读导航

## 主论文
- [computer-aided-kinematics-and-dynamics](computer-aided-kinematics-and-dynamics.md) (E. J. Haug, 1989, Allyn and Bacon)

## Related 论文解读
（暂无）

## Topic 专题

### 逐章精读笔记
- [Ch.1 Elements of Computer-Aided Kinematics and Dynamics](ch1-elements-of-cakd.md) — 导论：学科范围、工程实例、传统方法vs计算方法、两种坐标方法对比、全书导读
- [Ch.2 Planar Vectors, Matrices, and Differential Calculus](ch2-planar-vectors-matrices-calculus.md) — 数学基础：几何→代数向量、矩阵代数、坐标变换矩阵A/B/R、矩阵微积分记号Φ_q、运动体上点的速度/加速度公式
- [Ch.3 Planar Cartesian Kinematics](ch3-planar-cartesian-kinematics.md) — 核心方法论：平面运动副约束方程库、齿轮/凸轮高副、驱动约束、位置(N-R)/速度/加速度统一求解、奇异构型(lock-up/bifurcation)
- [Ch.4 Numerical Methods in Kinematics](ch4-numerical-methods-kinematics.md) — 数值实现：DADS三层架构、Jacobian稀疏评估、装配最小化(共轭梯度)、高斯消元/LU分解、Newton-Raphson(收敛性分析)、冗余约束自动检测与消除
- [Ch.5 Planar Kinematic Modeling and Analysis](ch5-planar-kinematic-modeling.md) — 五大应用案例：曲柄滑块/四连杆/快回/齿轮-滑块/气门挺杆，建模配方(Recipe)、复合铰简化、装配陷阱、锁死/分叉奇异性、加速度对参数的极端敏感性
- [Ch.6 Dynamics of Planar Systems](ch6-planar-dynamics.md) — 从运动学到动力学的跨越：虚功原理消除内力、广义力(弹簧-阻尼器-作动器)、拉格朗日乘子→DAE(Eq.6.3.18)、逆动力学(运动学确定系统)、最小总势能平衡、约束反力公式(Eqs.6.6.8-6.6.9)
- [Ch.7 Numerical Methods in Dynamics](ch7-numerical-methods-dynamics.md) — DAE数值求解：DADS动力学程序架构、坐标分区DAE→ODE约化与存在性证明、四种DAE算法(坐标分区/直接积分/Baumgarte稳定化/混合算法)、Adams-Bashforth预测器+Adams-Moulton校正器PECE积分、自适应步长阶次控制、最小势能平衡分析
