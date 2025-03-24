以下是一个使用NumPy读取CSV文件并转换为NumPy数组的Python程序：

```python
import numpy as np

# 指定CSV文件路径
filename = 'data.csv'  # 替换为你的文件路径

# 使用genfromtxt读取CSV文件，分隔符为逗号
# 如果CSV有标题行，设置skip_header=1跳过首行
data = np.genfromtxt(filename, delimiter=',', skip_header=0)

print("生成的NumPy数组：")
print(data)
```

**步骤说明：**
1. 导入NumPy库。
2. 设置CSV文件的路径（替换`data.csv`为实际路径）。
3. 使用`np.genfromtxt`读取文件，指定分隔符（如逗号）。
4. 若CSV包含标题行，设置`skip_header=1`跳过首行。
5. 输出转换后的NumPy数组。

**注意事项：**
- 如果数据包含非数值类型（如字符串），需使用`dtype`参数指定数据类型。
- 处理缺失值时，`genfromtxt`默认用`nan`填充，可用`filling_values`参数自定义。
- 若数据格式整齐且无非数值内容，可用`np.loadtxt(filename, delimiter=',')`替代。

此方法无需额外依赖库，适合基础CSV转换需求。