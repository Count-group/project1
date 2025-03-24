为了计算两个矩形的交并比（IoU），我们需要确定它们的交集面积和并集面积。以下是实现这一功能的Python程序：

```python
def calculate_iou(rect1, rect2):
    # 调整矩形坐标，确保x1<=x2，y1<=y2
    x1, y1, x2, y2 = rect1
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    
    x3, y3, x4, y4 = rect2
    x3, x4 = sorted([x3, x4])
    y3, y4 = sorted([y3, y4])
    
    # 计算交集区域的坐标
    left_x = max(x1, x3)
    right_x = min(x2, x4)
    top_y = max(y1, y3)
    bottom_y = min(y2, y4)
    
    # 计算交集面积
    if right_x < left_x or bottom_y < top_y:
        intersection_area = 0
    else:
        intersection_area = (right_x - left_x) * (bottom_y - top_y)
    
    # 计算两个矩形的面积
    area1 = (x2 - x1) * (y2 - y1)
    area2 = (x4 - x3) * (y4 - y3)
    
    # 计算并集面积
    union_area = area1 + area2 - intersection_area
    
    # 计算IoU
    if union_area == 0:
        return 0.0
    else:
        iou = intersection_area / union_area
        return iou

# 示例测试
if __name__ == "__main__":
    # 测试案例1：完全重叠
    rect1 = (0, 0, 2, 2)
    rect2 = (0, 0, 2, 2)
    print("Test Case 1 IoU:", calculate_iou(rect1, rect2))  # 应输出1.0

    # 测试案例2：部分重叠
    rect3 = (0, 0, 2, 2)
    rect4 = (1, 1, 3, 3)
    print("Test Case 2 IoU:", calculate_iou(rect3, rect4))  # 应输出0.142857...

    # 测试案例3：不相交
    rect5 = (0, 0, 1, 1)
    rect6 = (2, 2, 3, 3)
    print("Test Case 3 IoU:", calculate_iou(rect5, rect6))  # 应输出0.0

    # 测试案例4：坐标顺序颠倒
    rect7 = (2, 2, 0, 0)
    rect8 = (1, 1, 3, 3)
    print("Test Case 4 IoU:", calculate_iou(rect7, rect8))  # 应输出0.142857...
```

### 实现说明：
1. **坐标调整**：确保输入的矩形坐标转换为左上角和右下角格式，无论输入顺序如何。
2. **交集计算**：通过比较两个矩形的边界来确定交集区域。
3. **面积计算**：分别计算两个矩形的面积、交集面积及并集面积。
4. **交并比计算**：根据交集和并集面积的比值得到IoU，处理除零情况返回0。

该程序能够正确处理不同输入顺序及各种相交情况，确保计算结果的准确性。