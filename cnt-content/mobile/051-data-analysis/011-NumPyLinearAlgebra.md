# 数据分析 线性代数

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 矩阵创建

**基本写法：从列表创建矩阵**
`np.array([[<行1>], [<行2>]])`

```python
# 从嵌套列表创建矩阵
A = np.array([[1, 2], [3, 4]])
```

---

**基本写法：创建单位矩阵**
`np.eye(<n>)`

```python
# 创建 3x3 单位矩阵
I = np.eye(3)
```

---

**基本写法：创建全零矩阵**
`np.zeros((<行>, <列>))`

```python
# 创建 2x3 全零矩阵
Z = np.zeros((2, 3))
```

---

**基本写法：创建全一矩阵**
`np.ones((<行>, <列>))`

```python
# 创建 2x2 全一矩阵
O = np.ones((2, 2))
```

---

**基本写法：创建对角矩阵**
`np.diag(<一维数组>)`

```python
# 创建对角矩阵
D = np.diag([1, 2, 3])
```

---

## 矩阵运算

**基本写法：矩阵乘法**
`<矩阵A> @ <矩阵B>`

```python
# 矩阵乘法（推荐使用 @ 运算符）
C = A @ B
```

---

**基本写法：使用 dot 函数**
`np.dot(<矩阵A>, <矩阵B>)`

```python
# 使用 dot 函数进行矩阵乘法
C = np.dot(A, B)
```

---

**基本写法：矩阵转置**
`<矩阵>.T`

```python
# 矩阵转置
A_T = A.T
```

---

**基本写法：矩阵求逆**
`np.linalg.inv(<矩阵>)`

```python
# 求矩阵的逆
A_inv = np.linalg.inv(A)
```

---

**基本写法：矩阵行列式**
`np.linalg.det(<矩阵>)`

```python
# 计算行列式
det = np.linalg.det(A)
```

---

**基本写法：矩阵的迹**
`np.trace(<矩阵>)`

```python
# 计算矩阵的迹（对角线元素之和）
tr = np.trace(A)
```

---

## 线性方程组

**基本写法：求解线性方程组**
`np.linalg.solve(<系数矩阵>, <常数向量>)`

```python
# 求解 Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
```

---

**基本写法：最小二乘法求解**
`np.linalg.lstsq(<系数矩阵>, <常数向量>, rcond=None)`

```python
# 最小二乘法求解超定方程组
x, residuals, rank, sv = np.linalg.lstsq(A, b, rcond=None)
```

---

## 特征值与特征向量

**基本写法：计算特征值和特征向量**
`np.linalg.eig(<矩阵>)`

```python
# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)
```

---

**基本写法：计算奇异值分解**
`np.linalg.svd(<矩阵>)`

```python
# 奇异值分解（SVD）
U, S, Vt = np.linalg.svd(A)
```

---

## 向量运算

**基本写法：向量点积**
`np.dot(<向量a>, <向量b>)`

```python
# 向量点积
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
dot_product = np.dot(v1, v2)
```

---

**基本写法：向量内积**
`np.inner(<向量a>, <向量b>)`

```python
# 向量内积
inner = np.inner(v1, v2)
```

---

**基本写法：向量外积**
`np.outer(<向量a>, <向量b>)`

```python
# 向量外积
outer = np.outer(v1, v2)
```

---

**基本写法：向量范数**
`np.linalg.norm(<向量>, ord=<范数类型>)`

```python
# 计算 L2 范数（欧几里得范数）
norm = np.linalg.norm(v1)
# 计算 L1 范数
norm_l1 = np.linalg.norm(v1, ord=1)
```

---

**基本写法：计算矩阵范数**
`np.linalg.norm(<矩阵>, ord=<范数类型>)`

```python
# 计算矩阵的 Frobenius 范数
fro_norm = np.linalg.norm(A, ord="fro")
```

---

## 矩阵分解

**基本写法：LU 分解**
`scipy.linalg.lu(<矩阵>)`

```python
# LU 分解（需要 scipy）
from scipy.linalg import lu
P, L, U = lu(A)
```

---

**基本写法：QR 分解**
`np.linalg.qr(<矩阵>)`

```python
# QR 分解
Q, R = np.linalg.qr(A)
```

---

**基本写法：Cholesky 分解**
`np.linalg.cholesky(<矩阵>)`

```python
# Cholesky 分解（矩阵需为正定对称矩阵）
L = np.linalg.cholesky(A)
```

---

## 矩阵秩与条件数

**基本写法：计算矩阵的秩**
`np.linalg.matrix_rank(<矩阵>)`

```python
# 计算矩阵的秩
rank = np.linalg.matrix_rank(A)
```

---

**基本写法：计算条件数**
`np.linalg.cond(<矩阵>)`

```python
# 计算条件数（衡量矩阵的稳定性）
condition = np.linalg.cond(A)
```

---

## 广义逆矩阵

**基本写法：计算伪逆矩阵**
`np.linalg.pinv(<矩阵>)`

```python
# 计算伪逆矩阵（Moore-Penrose 伪逆）
A_pinv = np.linalg.pinv(A)
```

---

## 张量运算

**基本写法：张量缩并**
`np.tensordot(<张量A>, <张量B>, axes=<维度>)`

```python
# 张量缩并运算
T1 = np.random.rand(2, 3, 4)
T2 = np.random.rand(4, 5)
result = np.tensordot(T1, T2, axes=([2], [0]))
```

---

**基本写法：爱因斯坦求和约定**
`np.einsum(<下标表达式>, <数组1>, <数组2>)`

```python
# 使用 einsum 进行矩阵乘法
C = np.einsum("ij,jk->ik", A, B)
# 计算矩阵的迹
trace = np.einsum("ii->i", A)
```

---

## 线性代数应用

**换行写法：线性回归求解**
`X = np.column_stack([np.ones(<n>), <特征>])`
`beta = np.linalg.lstsq(X, <目标>, rcond=None)[0]`

```python
# 使用最小二乘法求解线性回归
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
X = np.column_stack([np.ones(5), x])
beta = np.linalg.lstsq(X, y, rcond=None)[0]
```

---

**换行写法：主成分分析降维**
`A_centered = <数据> - <数据>.mean(axis=0)`
`U, S, Vt = np.linalg.svd(A_centered)`
`components = Vt[:<n>]`

```python
# 使用 SVD 进行 PCA 降维
data = np.random.rand(100, 5)
data_centered = data - data.mean(axis=0)
U, S, Vt = np.linalg.svd(data_centered)
components = Vt[:2]
```
