import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 生成 3 组折线图数据
x_line = np.linspace(0, 10, 10)
y_line1 = x_line ** 2
y_line2 = x_line ** 1.5
y_line3 = x_line ** 0.5

# 生成 3 组面积图数据
x_area = np.linspace(0, 10, 10)
y_area1 = x_area * 2
y_area2 = x_area * 3
y_area3 = x_area * 4

# 对面积图数据进行平滑处理
x_smooth = np.linspace(x_area.min(), x_area.max(), 300)
f1 = interp1d(x_area, y_area1, kind='cubic')
y_area1_smooth = f1(x_smooth)
f2 = interp1d(x_area, y_area2, kind='cubic')
y_area2_smooth = f2(x_smooth)
f3 = interp1d(x_area, y_area3, kind='cubic')
y_area3_smooth = f3(x_smooth)

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制折线图
ax.plot(x_line, y_line1, label='Line 1', color='blue')
ax.plot(x_line, y_line2, label='Line 2', color='red')
ax.plot(x_line, y_line3, label='Line 3', color='green')

# 绘制面积图
ax.fill_between(x_smooth, y_area1_smooth, alpha=0.3, color='orange', label='Area 1')
ax.fill_between(x_smooth, y_area2_smooth, alpha=0.3, color='purple', label='Area 2')
ax.fill_between(x_smooth, y_area3_smooth, alpha=0.3, color='brown', label='Area 3')

# 添加标题和标签
ax.set_title('Line and Area Chart')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# 添加图例
ax.legend()

# 显示图形
plt.show()
    