---
type: chapter-notes
parent: computer-aided-kinematics-and-dynamics
chapter: 2
title: "Planar Vectors, Matrices, and Differential Calculus"
pages: 20-47
sections:
  - "2.1 Geometric Vectors"
  - "2.2 Matrix Algebra"
  - "2.3 Algebraic Vectors"
  - "2.4 Transformation of Coordinates"
  - "2.5 Vector and Matrix Differentiation"
  - "2.6 Velocity and Acceleration of a Point Fixed in a Moving Frame"
created: 2026-05-14
last_updated: 2026-05-14
---

# Chapter 2: Planar Vectors, Matrices, and Differential Calculus

## 章节定位

第二章是 Part One（平面系统）的**数学基础工具章**（pp.20-47），为 Ch.3-8 全部平面运动学和动力学分析提供核心数学记号和运算框架。本章的核心目标是：将传统的**几何向量分析**系统地转化为**代数向量（矩阵）表示**，使之适合公式推导和计算机实现。章节内容从几何向量出发，经矩阵代数和代数向量，建立坐标变换理论，最后发展向量/矩阵微分学和运动体上点的速度/加速度公式。本章不涉及约束方程和运动学求解（Ch.3-4），也不涉及动力学（Ch.6），但所有后续推导都建立在本章的记号和恒等式之上。假设读者具备基本的线性代数和微积分知识。

---

## 概念定义

### Sec. 2.1 几何向量

**Geometric Vector（几何向量）** [p.20]
> The geometric vector $\vec{a}$ in Fig. 2.1.1, beginning at point $A$ and ending at point $B$, is defined as the directed line segment from $A$ to $B$.
>
> 从点 $A$ 到点 $B$ 的有向线段。

---

**Magnitude of a Vector（向量的模/大小）** [p.20]
> The magnitude of a vector $\vec{a}$ is its length and is denoted by $a$ or $|\vec{a}|$.
>
> 向量 $\vec{a}$ 的长度，记为 $a$ 或 $|\vec{a}|$。

---

**Negative of a Vector（向量的负）** [p.20]
> The negative of a vector is obtained by multiplying the vector by $-1$. It is a vector with the same magnitude but opposite direction.
>
> 将向量乘以 $-1$ 得到，具有相同大小但方向相反。

---

**Unit Vector（单位向量）** [p.20]
> A unit vector, that is, a vector having a magnitude of 1 unit, in the direction $\vec{a} \neq \vec{0}$ is $(1/a)\vec{a}$.
>
> 大小为1的向量，方向与 $\vec{a}$ 相同，表达式为 $(1/a)\vec{a}$。

---

**Parallelogram Rule（平行四边形法则）** [p.20]
> Two vectors $\vec{a}$ and $\vec{b}$ are added according to the parallelogram rule.
>
> 两向量按平行四边形法则相加。

---

**Right-Hand Orthogonal Reference Frame（右手正交参考系）** [p.21]
> Orthogonal reference frames are used extensively in representing vectors. Use in this text is limited to right-hand orthogonal reference frames; that is, the $y$ axis is oriented $\pi/2$ rad counterclockwise from the $x$ axis. Such frames are called Cartesian reference frames.
>
> 本书使用的正交参考系，$y$ 轴在 $x$ 轴逆时针方向 $\pi/2$ 处。此类参考系称为笛卡尔参考系。

---

**Cartesian Components（笛卡尔分量）** [p.21]
> A vector $\vec{a}$ can be resolved into components $a_x$ and $a_y$ along the $x$ and $y$ axes of a Cartesian reference frame. These components are called the Cartesian components of the vector.
>
> 向量 $\vec{a}$ 沿笛卡尔参考系的 $x$ 和 $y$ 轴的分量 $a_x$ 和 $a_y$。

---

**Scalar Product / Dot Product（标量积/点积）** [p.22]
> The scalar product (or dot product) of two vectors $\vec{a}$ and $\vec{b}$ is defined as the product of the magnitudes of the vectors and the cosine of the angle between them; that is, $\vec{a} \cdot \vec{b} = ab\cos\theta(\vec{a}, \vec{b})$.
>
> 两向量模的乘积再乘以它们之间夹角的余弦：$\vec{a} \cdot \vec{b} = ab\cos\theta(\vec{a}, \vec{b})$。

---

**Orthogonal Vectors（正交向量）** [p.22]
> Two nonzero vectors are said to be orthogonal vectors if their scalar product is zero.
>
> 标量积为零的两个非零向量称为正交向量。

---

**Perpendicular Vector（垂直向量）** [p.23]
> It is often helpful to define a vector that is perpendicular to a given vector $\vec{a}$, has the same length as $\vec{a}$, and is oriented $\pi/2$ rad counterclockwise from $\vec{a}$. This vector is denoted as $\vec{a}^\perp$ and is written as $\vec{a}^\perp = -a_y\vec{i} + a_x\vec{j}$.
>
> 与 $\vec{a}$ 垂直、等长、且在 $\vec{a}$ 逆时针方向 $\pi/2$ 处的向量，记为 $\vec{a}^\perp = -a_y\vec{i} + a_x\vec{j}$。

---

### Sec. 2.2 矩阵代数

**Matrix（矩阵）** [p.24]
> A matrix is a rectangular array of numbers, taken here to be real. If it has $m$ rows and $n$ columns, the dimension of the matrix is said to be $m \times n$. A matrix is denoted by a boldface capital letter if $m$ and $n$ are greater than 1.
>
> 实数的矩形阵列。若有 $m$ 行 $n$ 列，则维度为 $m \times n$。用粗体大写字母表示。

---

**Column Matrix（列矩阵）** [p.25]
> A matrix with only one column is called a column matrix and is denoted by a boldface lowercase letter; for example, **a**.
>
> 只有一列的矩阵，用粗体小写字母表示。

---

**Row Matrix（行矩阵）** [p.25]
> A matrix with only one row is called a row matrix and is denoted by a boldface lowercase letter.
>
> 只有一行的矩阵，用粗体小写字母表示。

---

**Transpose of a Matrix（矩阵的转置）** [p.24]
> The transpose of a matrix is formed by interchanging rows and columns and is designated by the superscript $T$. Thus, if $a_{ij}$ is the $i$-$j$ element of matrix **A**, $a_{ji}$ is the $i$-$j$ element of its transpose $\mathbf{A}^T$.
>
> 交换行和列得到的矩阵，用上标 $T$ 表示。若 $a_{ij}$ 是 **A** 的 $i$-$j$ 元素，则 $a_{ji}$ 是 $\mathbf{A}^T$ 的 $i$-$j$ 元素。

---

**Square Matrix（方阵）** [p.25]
> A square matrix has an equal number of rows and columns.
>
> 行数和列数相等的矩阵。

---

**Diagonal Matrix（对角矩阵）** [p.25]
> A diagonal matrix is a square matrix with $a_{ij} = 0$ for $i \neq j$ and at least one nonzero diagonal term. An $n \times n$ diagonal matrix **A** can be represented as $\mathbf{A} \equiv \text{diag}[a_{11}, a_{22}, \ldots, a_{nn}]$.
>
> 非对角元素全为零、且至少一个对角元素非零的方阵。

---

**Identity Matrix（单位矩阵）** [p.25]
> The $n \times n$ identity matrix, denoted **I** or $\mathbf{I}_n$, is a diagonal matrix with $a_{ii} = 1$, $i = 1, \ldots, n$.
>
> 所有对角元素为1的对角矩阵，记为 **I** 或 $\mathbf{I}_n$。

---

**Zero Matrix（零矩阵）** [p.25]
> A zero matrix of any dimension, designated as **0**, has $a_{ij} = 0$, for all $i$ and $j$.
>
> 所有元素均为零的矩阵，记为 **0**。

---

**Matrix Product（矩阵乘积）** [p.26]
> Let **A** be an $m \times p$ matrix and **B** be a $p \times n$ matrix. The matrix product of **A** and **B** is defined as the $m \times n$ matrix $\mathbf{C} = \mathbf{AB}$, where $c_{ij} = \sum_{k=1}^{p} a_{ik}b_{kj}$.
>
> 设 **A** 为 $m \times p$ 矩阵，**B** 为 $p \times n$ 矩阵，乘积 $\mathbf{C} = \mathbf{AB}$ 是 $m \times n$ 矩阵，元素 $c_{ij} = \sum_{k=1}^{p} a_{ik}b_{kj}$。

**特征**：矩阵乘法**不满足交换律** $\mathbf{AB} \neq \mathbf{BA}$（Eq. 2.2.11），但满足结合律 $(\mathbf{AB})\mathbf{C} = \mathbf{A}(\mathbf{BC})$ 和分配律 $(\mathbf{A}+\mathbf{B})\mathbf{C} = \mathbf{AC}+\mathbf{BC}$。

---

**Symmetric Matrix（对称矩阵）** [p.27]
> If $a_{ij} = a_{ji}$, for all $i$ and $j$, the square matrix $\mathbf{A} = [a_{ij}]$ is called a symmetric matrix; that is, $\mathbf{A} = \mathbf{A}^T$.
>
> 所有元素满足 $a_{ij} = a_{ji}$ 的方阵，即 $\mathbf{A} = \mathbf{A}^T$。

---

**Skew-Symmetric Matrix（反对称矩阵）** [p.27]
> If $a_{ij} = -a_{ji}$, for all $i$ and $j$, **A** is called a skew-symmetric matrix; that is, $\mathbf{A} = -\mathbf{A}^T$. Note that in this case $a_{ii} = 0$, for all $i$.
>
> 所有元素满足 $a_{ij} = -a_{ji}$ 的方阵，即 $\mathbf{A} = -\mathbf{A}^T$，且对角元素全为零。

---

**Linearly Dependent / Independent（线性相关/线性无关）** [p.27-28]
> A set of column matrices $\mathbf{a}_j$, $j = 1, \ldots, m$, is called linearly dependent if there are constants $\alpha_j$, $j = 1, \ldots, m$, that are not all zero such that $\sum_{j=1}^{m} \alpha_j\mathbf{a}_j = \mathbf{0}$. If a set of column matrices is not linearly dependent, it is called linearly independent. Equivalently, column matrices $\mathbf{a}_j$ are linearly independent if and only if $\sum \alpha_j\mathbf{a}_j = \mathbf{0}$ implies that $\alpha_j = 0$, $j = 1, \ldots, m$.
>
> 若存在不全为零的常数 $\alpha_j$ 使得 $\sum \alpha_j\mathbf{a}_j = \mathbf{0}$，则称列矩阵组线性相关。否则称为线性无关。等价地，列矩阵组线性无关当且仅当 $\sum \alpha_j\mathbf{a}_j = \mathbf{0}$ 蕴含所有 $\alpha_j = 0$。

---

**Rank（秩）** [p.29]
> The row rank (column rank) of a matrix is defined as the largest number of linearly independent rows (columns) in the matrix. The row and column ranks of any matrix are equal, hence defining the rank of the matrix. The rank of a matrix is also equal to the dimension of the largest square submatrix (obtained by deleting rows and columns) with nonzero determinant.
>
> 矩阵中线性无关的最大行数（列数），行秩=列秩。也等于最大非奇异子方阵的阶数。

---

**Full Rank（满秩）** [p.29]
> A square matrix with linearly independent rows (columns) is said to have full rank.
>
> 行（列）线性无关的方阵。

---

**Singular Matrix（奇异矩阵）** [p.29]
> When a square matrix does not have full rank, it is called a singular matrix.
>
> 不满秩的方阵。

---

**Nonsingular Matrix（非奇异矩阵）** [p.29]
> A square matrix **A** of full rank is called a nonsingular matrix. For such a matrix, there is an inverse, denoted by $\mathbf{A}^{-1}$, such that $\mathbf{AA}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$.
>
> 满秩的方阵。此类矩阵存在逆矩阵 $\mathbf{A}^{-1}$，满足 $\mathbf{AA}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$。

---

**Orthogonal Matrix（正交矩阵）** [p.29]
> A special nonsingular matrix that arises often in kinematics is called an orthogonal matrix, with the property that $\mathbf{A}^T\mathbf{A} = \mathbf{AA}^T = \mathbf{I}$. That is, $\mathbf{A}^{-1} = \mathbf{A}^T$.
>
> 满足 $\mathbf{A}^T\mathbf{A} = \mathbf{AA}^T = \mathbf{I}$ 的非奇异方阵。其逆等于转置：$\mathbf{A}^{-1} = \mathbf{A}^T$。

**特征**：正交矩阵在运动学中频繁出现，因为**旋转变换矩阵是正交的**，使得逆变换极其高效。

---

### Sec. 2.3 代数向量

**Algebraic Representation of a Vector / Algebraic Vector（向量的代数表示/代数向量）** [p.30]
> The vector $\vec{a}$ is thus uniquely defined by its Cartesian components, which may be written using matrix notation as $\mathbf{a} = [a_x, a_y]^T$. This is the algebraic representation of a vector in the $x$-$y$ Cartesian reference frame. An algebraic vector is defined as a column matrix.
>
> 向量 $\vec{a}$ 由其笛卡尔分量唯一确定，可用矩阵记号写为 $\mathbf{a} = [a_x, a_y]^T$。这是向量在 $x$-$y$ 笛卡尔参考系中的代数表示。代数向量定义为列矩阵。

**特征**：几何向量与同一平面内的 $2\times 1$ 代数向量一一对应，此后在 Part One 中不再区分。

---

**n Vector（n 维向量）** [p.30]
> An algebraic vector with $n$ components is called an $n$ vector. For example, the algebraic vectors $\mathbf{a} = [a_x, a_y]^T$, $\mathbf{b} = [b_x, b_y]^T$, and $\mathbf{c} = [c_x, c_y]^T$ may be combined to form the 6-vector $\mathbf{d} = [a_x, a_y, b_x, b_y, c_x, c_y]^T = [\mathbf{a}^T, \mathbf{b}^T, \mathbf{c}^T]^T$.
>
> 含 $n$ 个分量的代数向量称为 $n$ 维向量。可将多个2维向量堆叠为更高维向量。

---

**Orthogonal Rotation Matrix $\mathbf{R}$（正交旋转矩阵 $\mathbf{R}$）** [p.31]
> The matrix $\mathbf{R}$ is the orthogonal rotation matrix: $\mathbf{R} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$. The operation $\mathbf{Ra} = \mathbf{a}^\perp$ rotates a vector **a** by an angle $\pi/2$ counterclockwise.
>
> 正交旋转矩阵 $\mathbf{R} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$。运算 $\mathbf{Ra} = \mathbf{a}^\perp$ 将向量 **a** 逆时针旋转 $\pi/2$。

**特征**：$\mathbf{R}^T\mathbf{R} = \mathbf{I}$（正交），$\mathbf{RR} = -\mathbf{I}$（旋转 $\pi$ 后反向）。连续施加 $\mathbf{R}$：$\mathbf{R}^2\mathbf{a} = -\mathbf{a}$，$\mathbf{R}^3\mathbf{a} = -\mathbf{a}^\perp$，$\mathbf{R}^4\mathbf{a} = \mathbf{a}$（回到原位）。

---

### Sec. 2.4 坐标变换

**Rotation Transformation Matrix $\mathbf{A}$（旋转变换矩阵 $\mathbf{A}$）** [p.33]
> The vectors **s** and **s'** are related by the matrix transformation $\mathbf{s} = \mathbf{As'}$, where **A** is the planar rotation transformation matrix: $\mathbf{A} = \mathbf{A}(\phi) \equiv \begin{bmatrix} \cos\phi & -\sin\phi \\ \sin\phi & \cos\phi \end{bmatrix}$.
>
> 向量 **s**（$x$-$y$ 系）和 **s'**（$x'$-$y'$ 系）通过矩阵变换 $\mathbf{s} = \mathbf{As'}$ 关联，其中 $\mathbf{A}(\phi) = \begin{bmatrix} \cos\phi & -\sin\phi \\ \sin\phi & \cos\phi \end{bmatrix}$ 是平面旋转变换矩阵。

**特征**：$\mathbf{A}$ 是正交矩阵（$\mathbf{A}^T\mathbf{A} = \mathbf{I}$），故逆变换为 $\mathbf{s'} = \mathbf{A}^T\mathbf{s}$（Eq. 2.4.7）。

---

**Relative Transformation Matrix $\mathbf{A}_{ij}$（相对变换矩阵 $\mathbf{A}_{ij}$）** [p.34]
> $\mathbf{A}_{ij}$ is the transformation matrix from the $x'_j$-$y'_j$ frame to the $x'_i$-$y'_i$ frame: $\mathbf{A}_{ij} = \mathbf{A}_i^T\mathbf{A}_j = \mathbf{A}(\phi_j - \phi_i)$.
>
> 从 $x'_j$-$y'_j$ 坐标系到 $x'_i$-$y'_i$ 坐标系的变换矩阵：$\mathbf{A}_{ij} = \mathbf{A}_i^T\mathbf{A}_j$，等价于按相对角度 $\phi_j - \phi_i$ 旋转。

---

**Generalized Coordinates（广义坐标）** [p.36]
> Thus, angles $\theta_1$ and $\theta_2$ are not independent; that is, they must satisfy the constraint equation of Eq. 2.4.15. These variables are typical of generalized coordinates that are used to define the geometry of a mechanism.
>
> 用于定义机构几何的变量（如角度 $\theta_1$、$\theta_2$），它们不一定独立，可能受约束方程限制。

---

### Sec. 2.5 向量与矩阵微分

**Matrix Calculus Notation（矩阵微积分记号）** [p.38]
> Let $\mathbf{q} = [q_1, \ldots, q_k]^T$ be a $k$ vector of real variables, $a(\mathbf{q})$ be a scalar differentiable function of **q**, and $\mathbf{\Phi}(\mathbf{q}) = [\Phi_1(\mathbf{q}), \ldots, \Phi_n(\mathbf{q})]^T$ be an $n$ vector of differentiable functions of **q**. Using $i$ as row index and $j$ as column index, the following matrix calculus notations are defined: $a_\mathbf{q} \equiv \frac{\partial a}{\partial \mathbf{q}} \equiv \left[\frac{\partial a}{\partial q_j}\right]_{1 \times k}$ and $\mathbf{\Phi}_\mathbf{q} \equiv \frac{\partial \mathbf{\Phi}}{\partial \mathbf{q}} \equiv \left[\frac{\partial \Phi_i}{\partial q_j}\right]_{n \times k}$.
>
> 标量函数对向量变量的导数为**行矩阵**（$1 \times k$），向量函数对向量变量的导数为**矩阵**（$n \times k$，即 Jacobian 矩阵）。下标记号 $\mathbf{\Phi}_\mathbf{q}$ 表示偏导矩阵。

**特征**：注意标量函数对向量的导数 $a_\mathbf{q}$ 是**行矩阵**（而非列矩阵），这是本书少数使用行矩阵的场合。

---

**Product Rule of Differentiation（乘积求导法则）** [p.39]
> The partial derivative of the scalar product of two $n$ vector functions $\mathbf{g}(\mathbf{q})$ and $\mathbf{h}(\mathbf{q})$ is: $(\mathbf{g}^T\mathbf{h})_\mathbf{q} = \mathbf{h}^T\mathbf{g}_\mathbf{q} + \mathbf{g}^T\mathbf{h}_\mathbf{q}$ (Eq. 2.5.13).
>
> 两个向量函数标量积的偏导：$(\mathbf{g}^T\mathbf{h})_\mathbf{q} = \mathbf{h}^T\mathbf{g}_\mathbf{q} + \mathbf{g}^T\mathbf{h}_\mathbf{q}$。

**特征**：注意 $(\mathbf{g}^T\mathbf{h})_\mathbf{q} \neq \mathbf{g}_\mathbf{q}^T\mathbf{h} + \mathbf{g}^T\mathbf{h}_\mathbf{q}$——直觉上的"乘积法则"在矩阵微积分中形式不同。

---

**Chain Rule of Differentiation（链式求导法则）** [p.40]
> If $\mathbf{\Phi}(\mathbf{g})$ and $\mathbf{g} = \mathbf{g}(\mathbf{q})$ are vector functions, the chain rule in matrix calculus form is: $\mathbf{\Phi}_\mathbf{q} = \mathbf{\Phi}_\mathbf{g}\mathbf{g}_\mathbf{q}$ (Eq. 2.5.14).
>
> 复合向量函数的链式法则的矩阵形式：$\mathbf{\Phi}_\mathbf{q} = \mathbf{\Phi}_\mathbf{g}\mathbf{g}_\mathbf{q}$。

---

### Sec. 2.6 运动坐标系中的速度与加速度

**Matrix $\mathbf{B}$（矩阵 $\mathbf{B}$）** [p.41]
> From Eq. 2.4.4, $\dot{\mathbf{A}} = \dot{\phi}\frac{d}{d\phi}\mathbf{A} = \dot{\phi}\begin{bmatrix} -\sin\phi & -\cos\phi \\ \cos\phi & -\sin\phi \end{bmatrix} \equiv \dot{\phi}\mathbf{B}$. The matrix **B** is the derivative of the rotation transformation matrix **A** with respect to the angle $\phi$.
>
> $\mathbf{B} \equiv \frac{d\mathbf{A}}{d\phi} = \begin{bmatrix} -\sin\phi & -\cos\phi \\ \cos\phi & -\sin\phi \end{bmatrix}$，即旋转变换矩阵 **A** 对角度 $\phi$ 的导数。

**特征**：$\mathbf{B} = \mathbf{AR} = \mathbf{RA}$（Eq. 2.6.5, 2.6.6），$\dot{\mathbf{B}} = -\dot{\phi}\mathbf{A}$（Eq. 2.6.8），$\frac{d}{d\phi}\mathbf{B} = -\mathbf{A}$。矩阵 **B** 在全书运动学和动力学推导中极为频繁。

---

## 符号定义

> [!note]
> 本章建立了 Part One（Ch.2-8）的**正式符号体系**。这里的符号将在后续所有平面分析章节中持续使用。

### 几何向量与基本运算（Sec. 2.1）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\vec{a}, \vec{b}, \vec{c}$ | 几何向量 | 平面几何向量 |
| $a = \lVert\vec{a}\rVert$ | 标量 | 向量 $\vec{a}$ 的模 |
| $\vec{i}, \vec{j}$ | 单位向量 | $x$ 轴和 $y$ 轴的单位坐标向量 |
| $a_x, a_y$ | 标量 | 向量 $\vec{a}$ 在 $x$、$y$ 方向的分量 |
| $\theta(\vec{a}, \vec{b})$ | 标量，角度 | 从 $\vec{a}$ 到 $\vec{b}$ 的逆时针角度 |
| $\vec{a}^\perp$ | 几何向量 | 与 $\vec{a}$ 垂直（逆时针 $\pi/2$）的等长向量 |

### 矩阵代数（Sec. 2.2）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{A}, \mathbf{B}, \mathbf{C}$ | 矩阵 | 一般矩阵（$m \times n$） |
| $\mathbf{a}, \mathbf{b}$ | 列矩阵 | 列向量 |
| $\mathbf{A}^T$ | 矩阵 | **A** 的转置 |
| $\mathbf{I}$（或 $\mathbf{I}_n$） | 方阵 | $n \times n$ 单位矩阵 |
| $\mathbf{0}$ | 矩阵 | 零矩阵 |
| $\mathbf{A}^{-1}$ | 方阵 | **A** 的逆矩阵（仅对非奇异矩阵存在） |

### 代数向量与旋转矩阵（Sec. 2.3）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{a} = [a_x, a_y]^T$ | $2 \times 1$ 列矩阵 | 向量 $\vec{a}$ 的代数表示 |
| $\mathbf{a}^\perp = [-a_y, a_x]^T$ | $2 \times 1$ 列矩阵 | 垂直向量的代数表示 |
| $\mathbf{R} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ | $2 \times 2$ 正交矩阵 | 逆时针旋转 $\pi/2$ 的正交旋转矩阵 |

> **关系**：$\mathbf{a}^\perp = \mathbf{Ra}$，$\mathbf{R}^T\mathbf{R} = \mathbf{I}$，$\mathbf{RR} = -\mathbf{I}$。

### 坐标变换（Sec. 2.4）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\phi$ | 标量，角度 | $x'$ 轴相对于 $x$ 轴的逆时针旋转角 |
| $\mathbf{s} = [s_x, s_y]^T$ | $2 \times 1$ 列矩阵 | 向量在 $x$-$y$ 坐标系下的分量 |
| $\mathbf{s'} = [s_{x'}, s_{y'}]^T$ | $2 \times 1$ 列矩阵 | 向量在 $x'$-$y'$ 坐标系下的分量 |
| $\mathbf{A} = \mathbf{A}(\phi)$ | $2 \times 2$ 正交矩阵 | 从 $x'$-$y'$ 到 $x$-$y$ 的旋转变换矩阵 |
| $\mathbf{r}$ | $2 \times 1$ 列矩阵 | 全局坐标系原点到运动体坐标系原点的位移向量 |
| $\mathbf{s'}^P$ | $2 \times 1$ 列矩阵（常向量） | 点 $P$ 在体坐标系下的位置向量 |
| $\mathbf{r}^P$ | $2 \times 1$ 列矩阵 | 点 $P$ 在全局坐标系下的位置向量 |
| $\mathbf{A}_{ij} = \mathbf{A}_i^T\mathbf{A}_j$ | $2 \times 2$ 正交矩阵 | 从 $j$ 体坐标系到 $i$ 体坐标系的相对变换矩阵 |

> **核心关系**：$\mathbf{r}^P = \mathbf{r} + \mathbf{As'}^P$（Eq. 2.4.8）——体上点的全局位置 = 体坐标系原点位置 + 旋转变换后的体内位置向量。这是全书最基本的位置公式。

### 向量与矩阵微分（Sec. 2.5）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\dot{\mathbf{a}} = \frac{d}{dt}\mathbf{a}$ | $2 \times 1$ 列矩阵 | 向量 **a** 的时间导数（速度） |
| $\ddot{\mathbf{a}} = \frac{d^2}{dt^2}\mathbf{a}$ | $2 \times 1$ 列矩阵 | 向量 **a** 的二阶时间导数（加速度） |
| $\mathbf{q} = [q_1, \ldots, q_k]^T$ | $k \times 1$ 列矩阵 | 广义坐标向量 |
| $a_\mathbf{q} = \frac{\partial a}{\partial \mathbf{q}}$ | $1 \times k$ 行矩阵 | 标量函数对广义坐标向量的偏导（梯度行向量） |
| $\mathbf{\Phi}_\mathbf{q} = \frac{\partial \mathbf{\Phi}}{\partial \mathbf{q}}$ | $n \times k$ 矩阵 | 向量函数对广义坐标向量的偏导（**Jacobian 矩阵**） |

> **关系**：$\mathbf{\Phi}_\mathbf{q}$ 即**约束 Jacobian**，是后续 Ch.3 运动学求解和 Ch.6 动力学方程的核心矩阵。

### 运动体上点的速度与加速度（Sec. 2.6）

| 符号 | 类型 | 含义 |
|------|------|------|
| $\mathbf{B} = \frac{d\mathbf{A}}{d\phi}$ | $2 \times 2$ 矩阵 | 旋转变换矩阵 **A** 对角度的导数 |
| $\dot{\mathbf{A}} = \dot{\phi}\mathbf{B}$ | $2 \times 2$ 矩阵 | 旋转变换矩阵的时间导数 |
| $\dot{\mathbf{r}}^P$ | $2 \times 1$ 列矩阵 | 点 $P$ 的速度 |
| $\ddot{\mathbf{r}}^P$ | $2 \times 1$ 列矩阵 | 点 $P$ 的加速度 |
| $\mathbf{s}^{P\perp}$ | $2 \times 1$ 列矩阵 | $\mathbf{As'}^P$ 的垂直向量，即 $\mathbf{Rs}^P$ |

> **核心关系**：
> - 速度：$\dot{\mathbf{r}}^P = \dot{\mathbf{r}} + \dot{\phi}\mathbf{Bs'}^P = \dot{\mathbf{r}} + \dot{\phi}\mathbf{s}^{P\perp}$（Eq. 2.6.4, 2.6.7）
> - 加速度：$\ddot{\mathbf{r}}^P = \ddot{\mathbf{r}} + \ddot{\phi}\mathbf{Bs'}^P - \dot{\phi}^2\mathbf{As'}^P = \ddot{\mathbf{r}} + \ddot{\phi}\mathbf{s}^{P\perp} - \dot{\phi}^2\mathbf{s}^P$（Eq. 2.6.9, 2.6.10）

---

## 核心论点

### 为什么需要代数向量表示

几何向量分析是描述运动几何的传统工具，但**不适合计算机实现**。原因：
1. 几何向量运算（平行四边形法则、图形法求角度）依赖**图形直觉**，无法程序化
2. 向量分量取决于参考系选择，几何形式隐藏了这一依赖

**代数向量（矩阵）表示**将向量运算全部转化为矩阵乘法和加法，具有以下优势：
- **公式操作简便**：矩阵运算规则明确，适合公式推导
- **计算机实现直接**：矩阵运算可直接映射到程序语言
- **维度扩展自然**：从2维向量到 $n$ 维向量（广义坐标）的堆叠仅需简单拼接

### 旋转变换矩阵 A 的核心性质

旋转变换矩阵 $\mathbf{A}(\phi) = \begin{bmatrix} \cos\phi & -\sin\phi \\ \sin\phi & \cos\phi \end{bmatrix}$ 具有以下在后续章节中反复使用的性质：

| 性质 | 公式 | 意义 |
|------|------|------|
| 正交性 | $\mathbf{A}^T\mathbf{A} = \mathbf{I}$ | 逆变换 = 转置，计算极其高效 |
| 逆 = 转置 | $\mathbf{A}^{-1} = \mathbf{A}^T$ | 无需矩阵求逆运算 |
| 导数 = $\mathbf{B}$ | $\frac{d\mathbf{A}}{d\phi} = \mathbf{B}$ | 速度公式的核心 |
| **AR = RA = B** | $\mathbf{AR} = \mathbf{RA} = \mathbf{B}$ | **A**、**B**、**R** 三矩阵的深层关系 |
| $\mathbf{B}$ 的导数 | $\frac{d\mathbf{B}}{d\phi} = -\mathbf{A}$ | 加速度公式中出现 $-\dot{\phi}^2\mathbf{A}$ 项 |

> **关键洞察**：$\mathbf{A}$ 的所有导数都可以在 $\mathbf{A}$ 和 $\mathbf{B}$ 之间循环表达——$\frac{d\mathbf{A}}{d\phi} = \mathbf{B}$，$\frac{d\mathbf{B}}{d\phi} = -\mathbf{A}$，$\frac{d^2\mathbf{A}}{d\phi^2} = -\mathbf{A}$，$\frac{d^3\mathbf{A}}{d\phi^3} = -\mathbf{B}$，$\frac{d^4\mathbf{A}}{d\phi^4} = \mathbf{A}$——与 $\sin$/$\cos$ 的微分循环完全对应。

### 矩阵微积分记号的设计意图

Jacobian 下标记号 $\mathbf{\Phi}_\mathbf{q}$ 是本书约束方程微分的核心记号工具。关键设计考量：
- **标量函数对向量的导数**是**行矩阵**（$1 \times k$），而非列矩阵——这与某些教材的梯度定义（列向量）不同
- **向量函数对向量的导数**是 Jacobian 矩阵（$n \times k$），行标 $i$ 对应函数分量，列标 $j$ 对应变量分量
- 下标记号 $\mathbf{\Phi}_\mathbf{q}$ 避免了繁琐的偏导符号，使**链式法则简洁**：$\mathbf{\Phi}_\mathbf{q} = \mathbf{\Phi}_\mathbf{g}\mathbf{g}_\mathbf{q}$

> **警告**（书中特别强调，p.39）：矩阵微积分的乘积法则形式与标量微积分不同：
> $$(\mathbf{g}^T\mathbf{h})_\mathbf{q} = \mathbf{h}^T\mathbf{g}_\mathbf{q} + \mathbf{g}^T\mathbf{h}_\mathbf{q} \neq \mathbf{g}_\mathbf{q}^T\mathbf{h} + \mathbf{g}^T\mathbf{h}_\mathbf{q}$$
> 正确形式的关键在于**转置的位置**。

### 速度和加速度公式的物理解读

体上固定点 $P$ 的速度和加速度公式（Sec. 2.6）：

$$\dot{\mathbf{r}}^P = \underbrace{\dot{\mathbf{r}}}_{\text{平动}} + \underbrace{\dot{\phi}\mathbf{s}^{P\perp}}_{\text{转动}}$$

$$\ddot{\mathbf{r}}^P = \underbrace{\ddot{\mathbf{r}}}_{\text{平动加速度}} + \underbrace{\ddot{\phi}\mathbf{s}^{P\perp}}_{\text{角加速度（切向）}} - \underbrace{\dot{\phi}^2\mathbf{s}^P}_{\text{向心加速度}}$$

物理解读：
- **速度**由平动分量 $\dot{\mathbf{r}}$ 和转动分量 $\dot{\phi}\mathbf{s}^{P\perp}$ 组成。转动分量垂直于从体坐标系原点到 $P$ 点的向量，大小为 $\dot{\phi} \cdot |\mathbf{s}^P|$
- **加速度**多出**向心加速度项** $-\dot{\phi}^2\mathbf{s}^P$，方向从 $P$ 指向体坐标系原点（向心），大小为 $\dot{\phi}^2 \cdot |\mathbf{s}^P|$
- 这些公式是 Ch.3 速度/加速度约束方程右端项 $\boldsymbol{\nu}$ 和 $\boldsymbol{\gamma}$ 的直接来源

---

## 工程应用与实例

| 例题号 | 名称 | 类型 | 应用 | 关键知识点 |
|--------|------|------|------|-----------|
| Example 2.1.1 | 向量加法 | 代数运算 | — | 分量形式的向量加法 |
| Example 2.1.2 | 标量积投影 | 几何意义 | — | $\vec{u} \cdot \vec{a}$ 是 $\vec{a}$ 在 $\vec{u}$ 方向的投影 |
| Example 2.1.3 | 角度计算 | sgn 函数消歧 | — | 用 $\text{sgn}(\mathbf{a}^{\perp T}\mathbf{b})$ 确定角度符号（Eq. 2.1.15） |
| Example 2.2.1-2.2.6 | 矩阵运算 | 矩阵加/乘/正交 | — | 矩阵乘法非交换，旋转矩阵正交性验证 |
| Example 2.3.1 | $\mathbf{R}$ 矩阵旋转 | 旋转验证 | — | $\mathbf{Ra}$ 将 **a** 逆时针旋转 $\pi/2$，连续施加4次回到原位 |
| **Example 2.4.1** | **双体定位机构** | 坐标变换 | 机械臂 | $\mathbf{r}^P = \mathbf{A}_1\mathbf{s}_1'^Q + \mathbf{A}_1\mathbf{A}_{12}\mathbf{s}_2'^{QP}$（Eq. 2.4.14）：连续旋转变换链 |
| Example 2.4.2 | 相对变换 | 坐标变换 | — | $\mathbf{A}_{12}(\theta_2) = \mathbf{A}(\theta_2)$：相对变换等价于按相对角度旋转 |
| **Example 2.4.3** | **滑块-曲柄机构** | 约束方程 | 内燃机 | 约束方程 $\Phi(\theta_1, \theta_2) = \sin\theta_1 + \ell\sin(\theta_1+\theta_2) = 0$（Eq. 2.4.15）：广义坐标不独立 |
| Example 2.5.1 | 双体定位速度/加速度 | 微分 | 机械臂 | 对 $\mathbf{r}^P$ 直接微分得到速度和加速度 |
| Example 2.5.2 | 滑块-曲柄 Jacobian | 矩阵微积分 | 内燃机 | $\mathbf{\Phi}_\mathbf{q}$ 和 $\mathbf{r}^P_\mathbf{q}$ 的计算 |
| Example 2.5.3 | 滑块-曲柄速度关系 | 约束微分 | 内燃机 | 通过约束方程微分得 $\dot{\theta}_2$ 与 $\dot{\theta}_1$ 的关系（Eq. 2.5.19, 2.5.21） |
| **Example 2.6.1** | **双体定位速度/加速度** | $\mathbf{B}$ 矩阵应用 | 机械臂 | 用 $\mathbf{B}_1$、$\mathbf{B}_{12}$ 推导速度（Eq. 2.6.11）和加速度（Eq. 2.6.12） |

> **贯穿实例**：**滑块-曲柄**和**双体定位机构**从 Sec. 2.4 引入，经 Sec. 2.5 微分，到 Sec. 2.6 速度/加速度分析，贯穿了后四个小节。这种"一个例子走到底"的教学策略使抽象数学工具始终有物理载体。

---

## 与全书的关系

| 本章概念/工具 | 后续展开位置 |
|-------------|------------|
| 旋转变换矩阵 $\mathbf{A}(\phi)$ | Ch.3（约束方程中体上点位置 $\mathbf{r}^P = \mathbf{r} + \mathbf{As'}^P$）、Ch.9（扩展为 Euler 参数的 $3\times3$ 空间旋转矩阵） |
| 矩阵 $\mathbf{B} = d\mathbf{A}/d\phi$ | Ch.3（速度/加速度约束方程右端项 $\boldsymbol{\nu}$、$\boldsymbol{\gamma}$）、Ch.6（动力学方程推导中的速度展开） |
| 正交旋转矩阵 $\mathbf{R}$ | Ch.3（垂直向量的快速计算）、Ch.6（D'Alembert 原理中虚位移展开） |
| Jacobian 记号 $\mathbf{\Phi}_\mathbf{q}$ | Ch.3（约束 Jacobian，Newton-Raphson 求解）、Ch.4（数值方法）、Ch.6（动力学 DAE 的系数矩阵） |
| 乘积法则 $(\mathbf{g}^T\mathbf{h})_\mathbf{q}$ | Ch.6（虚功原理推导中对动能和势能的微分） |
| 链式法则 $\mathbf{\Phi}_\mathbf{q} = \mathbf{\Phi}_\mathbf{g}\mathbf{g}_\mathbf{q}$ | Ch.3（复合约束的 Jacobian 分解）、Ch.5（DADS 约束模块的组合） |
| 约束方程 $\Phi(\theta_1, \theta_2) = 0$（滑块-曲柄） | Ch.3（系统化的约束方程库）、Ch.5（完整的滑块-曲柄建模案例） |
| 速度公式 $\dot{\mathbf{r}}^P = \dot{\mathbf{r}} + \dot{\phi}\mathbf{Bs'}^P$ | Ch.3（速度方程 $\Phi_\mathbf{q}\dot{\mathbf{q}} = \boldsymbol{\nu}$ 的推导） |
| 加速度公式 $\ddot{\mathbf{r}}^P = \ddot{\mathbf{r}} + \ddot{\phi}\mathbf{Bs'}^P - \dot{\phi}^2\mathbf{As'}^P$ | Ch.3（加速度方程 $\Phi_\mathbf{q}\ddot{\mathbf{q}} = \boldsymbol{\gamma}$ 中二次速度项 $\boldsymbol{\gamma}$ 的来源） |
