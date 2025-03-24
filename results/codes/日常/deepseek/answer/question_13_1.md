以下是满足要求的Python代码，生成包含三个折线图和三个平滑面积图的组合图表：

```python
import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子保证可重复性
np.random.seed(42)

# 创建数据
x_line = np.linspace(0, 10, 100)
x_area = np.linspace(0, 10, 500)

# 生成折线图数据（带噪声）
y_line1 = 0.5 * x_line + np.random.normal(0, 1, x_line.shape)
y_line2 = 0.1 * x_line**2 + np.random.normal(0, 3, x_line.shape)
y_line3 = 0.05 * x_line**3 + np.random.normal(0, 5, x_line.shape)

# 生成平滑面积图数据（不使用三角函数）
y_area1 = 50 * np.exp(-(x_area-5)**2/5)  # 高斯曲线
y_area2 = -0.5*(x_area-5)**3 + 50       # 三次多项式
y_area3 = 2*(x_area-5)**2 + 20          # 二次函数

# 设置颜色
line_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 蓝、橙、绿
area_colors = ['#d62728', '#9467bd', '#8c564b']  # 红、紫、棕

# 创建画布
plt.figure(figsize=(12, 7))

# 绘制面积图（先绘制保证在底层）
for i, (y, color) in enumerate(zip([y_area1, y_area2, y_area3], area_colors)):
    plt.fill_between(x_area, y, 0, color=color, alpha=0.3, label=f'Area {i+1}')
    plt.plot(x_area, y, color=color, alpha=0.6, lw=1)  # 添加半透明边界线

# 绘制折线图（后绘制显示在上层）
for i, (y, color) in enumerate(zip([y_line1, y_line2, y_line3], line_colors)):
    plt.plot(x_line, y, color=color, lw=2, label=f'Line {i+1}')

# 添加图表元素
plt.title('Combined Line Charts and Area Charts', fontsize=14)
plt.xlabel('X Axis', fontsize=12)
plt.ylabel('Y Axis', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper left', frameon=False)

# 调整坐标轴范围
plt.xlim(0, 10)
plt.ylim(0, 80)

plt.tight_layout()
plt.show()
```

**代码特点：**
1. 使用指数函数、多项式函数生成平滑曲线
2. 折线图数据加入正态分布噪声模拟真实数据
3. 面积图使用500个数据点保证平滑度
4. 颜色方案来自Matplotlib默认调色板
5. 面积图添加半透明边界线提升可读性
6. 折线图绘制在面积图上方保证可见性
7. 包含完整的图表元素（标题、坐标轴、图例、网格）

**生成图表说明：**
- 三个面积图分别呈现钟形曲线、S型曲线和抛物线形态
- 三个折线图分别展示线性、二次方和三次方增长趋势
- 所有曲线均使用不同颜色区分
- 面积图使用半透明填充避免遮挡折线图

运行此代码需要安装以下Python库：
- NumPy
- Matplotlib

可以通过以下命令安装依赖：
```bash
pip install numpy matplotlib
```