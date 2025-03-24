为了计算矩阵的特征值和特征向量，可以使用NumPy库中的`numpy.linalg.eig`函数。以下是一个完整的Python程序示例：

```python
import numpy as np

# 定义示例矩阵
matrix = np.array([[4, 2],
                  [1, 3]])

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# 输出结果
print("矩阵：")
print(matrix)

print("\n特征值：")
print(eigenvalues)

print("\n特征向量（每一列对应一个特征值）：")
print(eigenvectors)

print("\n详细分解：")
for i in range(len(eigenvalues)):
    print(f"特征值 {i+1}: {eigenvalues[i]:.4f}")
    print(f"对应的特征向量: {eigenvectors[:, i]}\n")
```

**代码解释：**

1. **导入库**：使用`numpy`进行矩阵运算。
2. **定义矩阵**：示例矩阵为`[[4, 2], [1, 3]]`，可根据需要修改。
3. **计算特征值和特征向量**：`np.linalg.eig`返回两个数组，分别是特征值（`eigenvalues`）和特征向量（`eigenvectors`）。
4. **输出结果**：
   - 原始矩阵。
   - 所有特征值。
   - 特征向量矩阵，每一列对应一个特征值。
   - 逐个显示每个特征值及其对应的特征向量。

**示例输出：**

```
矩阵：
[[4 2]
 [1 3]]

特征值：
[5. 2.]

特征向量（每一列对应一个特征值）：
[[ 0.89442719 -0.70710678]
 [ 0.4472136   0.70710678]]

详细分解：
特征值 1: 5.0000
对应的特征向量: [0.89442719 0.4472136 ]

特征值 2: 2.0000
对应的特征向量: [-0.70710678  0.70710678]
```

**注意事项：**
- 确保矩阵是方阵（行数和列数相等），否则会报错。
- 特征向量是归一化的单位向量。
- 修改`matrix`的值即可计算不同矩阵的特征值和特征向量。