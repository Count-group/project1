import numpy as np
import matplotlib.pyplot as plt


# 评测对象
objects = ['ChatGPT', 'DeepSeek', 'kimi', 'doubao']
# 评测指标
metrics = ['日常使用', '深度学习', '经典算法', 'ACM竞赛']
# 评测结果，每个对象在各指标上的得分
scores = [
    [105.3, 97.1,98, 38.5],
    [104, 100, 98, 22.2],
    [104, 82.9, 92, 3.7],
    [100, 91.4, 87, 3.7]
]

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300
# 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]

# 创建画布
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 颜色列表
colors = ['b', 'g', 'r', 'c']

# 绘制雷达图
for i, score in enumerate(scores):
    score += score[:1]
    ax.plot(angles, score, color=colors[i], linewidth=2, label=objects[i])
    ax.fill(angles, score, color=colors[i], alpha=0.25)

    # 标记数值
    for j, angle in enumerate(angles[:-1]):
        # 根据不同的对象微调位置
        offset = 0.05 * i - 0.1
        ax.text(angle + offset, score[j], str(score[j]), ha='center', va='center', color=colors[i])

# 设置坐标轴标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(metrics)

# 设置极坐标的范围
ax.set_ylim(0, 120)

# 添加图例
ax.legend()#loc='upper right', bbox_to_anchor=(1.3, 1.1)
plt.savefig('doubao.png')
# 显示图形
plt.show()
    