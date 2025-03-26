import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False

# 示例数据
labels = ['日常使用', '深度学习', '经典算法', 'ACM竞赛']  # 四个指标
categories = ['ChatGPT', 'DeepSeek', 'kimi', 'doubao']  # 四个评测对象
data = [
    [105.3, 97.1,98, 38.5],  # 模型A
    [104, 100, 98, 22.2],   # 模型B
    [104, 82.9, 92, 3.7],   # 模型C
    [100, 91.4, 87, 3.7]    # 模型D
]

# 计算雷达图角度
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]  # 闭合图形

# 创建画布
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# 设置极坐标参数
ax.set_theta_offset(np.pi / 2)  # 初始角度
ax.set_theta_direction(-1)      # 顺时针方向
ax.set_rlabel_position(0)       # 半径标签位置
ax.set_ylim(0, 140)            # 半径范围（100基础分 + 20额外分 + 余量）

# 绘制网格和标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.tick_params(axis='x', pad=20)  # 调整标签距离

# 自定义网格样式
ax.grid(color='gray', linestyle=':', linewidth=0.8, alpha=0.8)

# 颜色列表
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# 绘制每个模型的数据
for i in range(4):
    # 闭合数据
    values = data[i] + data[i][:1]
    
    # 绘制雷达图
    ax.plot(angles, values, color=colors[i], linewidth=2, label=categories[i])
    ax.fill(angles, values, color=colors[i], alpha=0.15)
    
    # 添加数据标签（带智能偏移）
    for j in range(len(labels)):
        angle = angles[j]
        value = data[i][j]
        
        # 根据角度调整标签位置
        offset_dict = {
            0: (0.15, -0.15),    # 右侧
            np.pi/2: (0, 0.2),   # 上方
            np.pi: (-0.15, 0),   # 左侧
            3*np.pi/2: (0, -0.2) # 下方
        }
        
        # 获取最近的基准角度
        base_angle = min([0, np.pi/2, np.pi, 3*np.pi/2], key=lambda x: abs(x - angle))
        dx, dy = offset_dict[base_angle]
        
        ax.text(angle + dx*np.pi/8,  # X偏移
                value + 5 + dy*15,    # Y偏移
                str(value), 
                color=colors[i],
                ha='center',
                va='center',
                fontsize=10,
                bbox=dict(facecolor='white', edgecolor=colors[i], boxstyle='round,pad=0.2'))

# 添加图例
plt.legend()#loc='upper right', bbox_to_anchor=(1.25, 1.1))

# 添加标题
plt.title('模型能力评估雷达图', pad=30)

# 显示图形
plt.tight_layout()
plt.savefig('DeepSeek.png')
plt.show()