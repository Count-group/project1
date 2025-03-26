import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（确保你电脑安装了SimHei字体，否则请自行替换为合适的中文字体）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义4个评测指标
categories = ['日常使用', '深度学习', '经典算法', 'ACM竞赛']
N = len(categories)

# 角度设置：每个指标均分圆周，最后一个点与第一个点重合以闭合图形
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# 构造样例数据，每个评测对象在各指标的分数 = 基础分+额外分（最高分别100和20）
data = {
    'ChatGPT': [105.3, 97.1,98, 38.5],
    'DeepSeek': [104, 100, 98, 22.2],
    'kimi': [104, 82.9, 92, 3.7],
    'doubao': [100, 91.4, 87, 3.7]
}

# 设置画布和极坐标子图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)       # 让第一个指标在图的顶部
ax.set_theta_direction(-1)           # 让指标顺时针排列

# 设置每个指标的标签
plt.xticks(angles[:-1], categories, fontsize=12)
# 设置径向标签（这里直接显示分数刻度，最高为120分）
ax.set_rlabel_position(0)
plt.yticks([20, 40, 60, 80, 100, 120], ["20", "40", "60", "80", "100", "120"], color="grey", size=10)
plt.ylim(0, 120)

# 定义4个不同的颜色（也可以换成其他你喜欢的颜色）
colors = ['b', 'r', 'g', 'm']

# 绘制每个评测对象的雷达图
for idx, (label, scores) in enumerate(data.items()):
    # 复制数据，并将第一个点添加到末尾，以闭合多边形
    values = scores[:]
    values += values[:1]
    
    # 绘制雷达图的边界和填充色
    ax.plot(angles, values, color=colors[idx], linewidth=2, linestyle='solid', label=label)
    ax.fill(angles, values, color=colors[idx], alpha=0.25)
    
    # 标记每个点的分数
    for angle, value in zip(angles, values):
        # 根据角度判断文本显示方向，避免数字贴边重叠
        angle_deg = angle * 180 / np.pi
        if 90 <= angle_deg <= 270:
            ha = "right"
            dx = -5  # 向左偏移
        else:
            ha = "left"
            dx = 5   # 向右偏移
        # 纵向略微上移，避免和点重合
        dy = 3
        
        # 添加文本标记
        ax.text(angle + 0.01, value + 0.5, str(value), size=10,
                horizontalalignment=ha, verticalalignment="center",
                color=colors[idx], weight='bold')

# 添加图例和标题
fig.legend()#loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("评测结果雷达图", size=15, color='black', y=1.1)
plt.savefig('chatGPT.png')
plt.show()
