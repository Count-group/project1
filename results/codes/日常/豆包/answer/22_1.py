def calculate_iou(rect1, rect2):
    # 提取矩形 1 的坐标
    x1, y1, x2, y2 = rect1
    # 提取矩形 2 的坐标
    x3, y3, x4, y4 = rect2

    # 计算交集的坐标
    x_inter1 = max(x1, x3)
    y_inter1 = max(y1, y3)
    x_inter2 = min(x2, x4)
    y_inter2 = min(y2, y4)

    # 计算交集的宽度和高度
    width_inter = max(0, x_inter2 - x_inter1)
    height_inter = max(0, y_inter2 - y_inter1)

    # 计算交集的面积
    area_inter = width_inter * height_inter

    # 计算矩形 1 的面积
    area_rect1 = (x2 - x1) * (y2 - y1)
    # 计算矩形 2 的面积
    area_rect2 = (x4 - x3) * (y4 - y3)

    # 计算并集的面积
    area_union = area_rect1 + area_rect2 - area_inter

    # 避免除零错误
    if area_union == 0:
        return 0

    # 计算交并比
    iou = area_inter / area_union
    return iou


# 示例使用
rect1 = [0, 0, 2, 2]
rect2 = [1, 1, 3, 3]
iou = calculate_iou(rect1, rect2)
print(f"两个矩形的交并比为: {iou}")
    