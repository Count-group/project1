import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 评测对象和指标
objects = ['ChatGPT', 'DeepSeek', 'kimi', 'doubao']
indicators = ['日常使用', '深度学习', '经典算法', 'ACM竞赛']

# 模拟评测数据 (每个维度的基础分最高100分，额外分最高20分)
data = {
    'ChatGPT': [105.3, 97.1,98, 38.5],
    'DeepSeek': [104, 100, 98, 22.2],
    'kimi': [104, 82.9, 92, 3.7],
    'doubao': [100, 91.4, 87, 3.7]
}

# 计算每个指标的角度
angles = np.linspace(0, 2 * np.pi, len(indicators), endpoint=False).tolist()

# 使雷达图闭合
angles += angles[:1]
for obj in objects:
    data[obj] += data[obj][:1]

# 创建雷达图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# 绘制每个评测对象的雷达图
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
for i, obj in enumerate(objects):
    values = data[obj]
    ax.plot(angles, values, label=obj, color=colors[i], linewidth=2)
    ax.fill(angles, values, color=colors[i], alpha=0.25)
    
    # 添加数值标签
    for j, value in enumerate(values[:-1]):
        angle = angles[j]
        # 调整标签位置以避免重叠
        if angle > np.pi/2 and angle < 3*np.pi/2:
            ha = 'right'
        else:
            ha = 'left'
        ax.text(angle, value + 2, str(value), color=colors[i], ha=ha, fontsize=9)

# 设置雷达图的标签和标题
ax.set_yticklabels([])  # 隐藏y轴刻度标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(indicators)
ax.set_title('评测结果雷达图', fontsize=16, pad=20)

# 添加图例
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.9))

# 添加网格线
ax.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.tight_layout()
plt.savefig('kimi.png')
plt.show()