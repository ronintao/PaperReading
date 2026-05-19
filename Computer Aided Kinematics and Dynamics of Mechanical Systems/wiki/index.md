---
type: index
title: "Computer Aided Kinematics and Dynamics of Mechanical Systems, Volume I: Basic Methods"
wiki_language: zh-CN
last_updated: 2026-05-19
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
- [Ch.8 Planar Dynamic Modeling and Analysis](ch8-planar-dynamic-modeling.md) — Part One收官：曲柄滑块(压缩机)飞轮惯量参数研究与失速能量分析、快回机构(牛头刨床)飞轮-循环频率反直觉关系、螺旋弹簧涌浪波与碰撞振颤(单侧弹簧/阻尼器)、气门挺杆弹簧设计准则(负反力=分离失效)
- [Ch.9 Spatial Cartesian Kinematics](ch9-spatial-cartesian-kinematics.md) — Part Two 起点：空间向量+tilde 算子、方向余弦矩阵 A、角速度 ω/ω'、Euler 参数（无奇异姿态广义坐标）、6 类基本运动副+7 类复合关节+4 类驱动约束、位置/速度/加速度三段统一求解（系数矩阵复用）
- [Ch.10 Spatial Kinematic Modeling and Analysis](ch10-spatial-kinematic-modeling.md) — 空间建模核心：约束冗余识别（制造缺陷测试）、空间曲柄滑块（球铰+转动圆柱副消冗余、锁死临界）、空间四连杆（两种等效模型验证）、空气压缩机（9体/62约束/偏置角参数研究）
- [Ch.11 Dynamics of Spatial Systems](ch11-spatial-dynamics.md) — 空间动力学核心：变分Newton-Euler方程（陀螺项ω̃'J'ω'）、惯性属性（主轴/平行轴定理/复合体）、两种约束DAE形式（Newton-Euler一阶混合Eq.11.3.11 vs Euler参数二阶Eq.11.3.29）、TSDA/RSDA力元广义力、关节反力公式（Eq.11.5.6）、DADS混合积分算法


