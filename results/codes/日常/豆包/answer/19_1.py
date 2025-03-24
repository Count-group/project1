def line_intersection(line1, line2):
    """
    计算两条直线的交点
    :param line1: 第一条直线的系数 (a1, b1, c1)，表示 a1*x + b1*y + c1 = 0
    :param line2: 第二条直线的系数 (a2, b2, c2)，表示 a2*x + b2*y + c2 = 0
    :return: 交点的坐标 (x, y)，如果两条直线平行则返回 None
    """
    a1, b1, c1 = line1
    a2, b2, c2 = line2
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    x = (b1 * c2 - b2 * c1) / det
    y = (a2 * c1 - a1 * c2) / det
    return x, y


def triangle_area(x1, y1, x2, y2, x3, y3):
    """
    计算由三个点 (x1, y1), (x2, y2), (x3, y3) 围成的三角形的面积
    :param x1: 第一个点的 x 坐标
    :param y1: 第一个点的 y 坐标
    :param x2: 第二个点的 x 坐标
    :param y2: 第二个点的 y 坐标
    :param x3: 第三个点的 x 坐标
    :param y3: 第三个点的 y 坐标
    :return: 三角形的面积
    """
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


def calculate_area_of_three_lines(line1, line2, line3):
    """
    计算由三条直线围成的图形的面积
    :param line1: 第一条直线的系数 (a1, b1, c1)，表示 a1*x + b1*y + c1 = 0
    :param line2: 第二条直线的系数 (a2, b2, c2)，表示 a2*x + b2*y + c2 = 0
    :param line3: 第三条直线的系数 (a3, b3, c3)，表示 a3*x + b3*y + c3 = 0
    :return: 围成图形的面积，如果不能围成三角形则返回 0
    """
    # 计算三条直线两两相交的交点
    point1 = line_intersection(line1, line2)
    point2 = line_intersection(line2, line3)
    point3 = line_intersection(line3, line1)

    # 检查是否有交点不存在
    if point1 is None or point2 is None or point3 is None:
        return 0

    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    # 计算三角形的面积
    return triangle_area(x1, y1, x2, y2, x3, y3)


# 示例使用
line1 = (1, -1, 0)  # 表示直线 x - y = 0
line2 = (1, 1, -2)  # 表示直线 x + y - 2 = 0
line3 = (0, 1, 0)  # 表示直线 y = 0

area = calculate_area_of_three_lines(line1, line2, line3)
print(f"由三条直线围成的图形的面积是: {area}")
    