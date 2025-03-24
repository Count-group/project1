import math

def calculate_probability(n, A, p):
    # 计算三角形面积
    def triangle_area():
        return 0.5 * abs(1 * 1 - 0 * 0)

    # 计算满足条件的区域面积比例
    def valid_area_ratio(S1, S2, S3):
        # 将不等式转换为关于 q1 和 q2 的形式
        # S1 * q1 + S2 * q2 + S3 * (1 - q1 - q2) >= 0
        # (S1 - S3) * q1 + (S2 - S3) * q2 + S3 >= 0
        a = S1 - S3
        b = S2 - S3
        c = S3

        # 计算直线与三角形的交点
        if a == 0 and b == 0:
            if c >= 0:
                return 1.0
            else:
                return 0.0

        if a == 0:
            if b > 0:
                q2 = -c / b
                if 0 <= q2 <= 1:
                    return 1.0 - q2
                else:
                    return 0.0
            else:
                q2 = -c / b
                if 0 <= q2 <= 1:
                    return q2
                else:
                    return 0.0

        if b == 0:
            if a > 0:
                q1 = -c / a
                if 0 <= q1 <= 1:
                    return 1.0 - q1
                else:
                    return 0.0
            else:
                q1 = -c / a
                if 0 <= q1 <= 1:
                    return q1
                else:
                    return 0.0

        # 计算交点
        q1_intersect = -c / a if a != 0 else float('inf')
        q2_intersect = -c / b if b != 0 else float('inf')

        if 0 <= q1_intersect <= 1 and 0 <= q2_intersect <= 1:
            return 0.5 * abs(q1_intersect * q2_intersect)
        elif 0 <= q1_intersect <= 1:
            return 0.5 * abs(q1_intersect)
        elif 0 <= q2_intersect <= 1:
            return 0.5 * abs(q2_intersect)
        else:
            return 0.0

    total_probability = 1.0
    for i in range(n):
        S1 = p[i][0] * A[0][0] + p[i][1] * A[0][1] + p[i][2] * A[0][2]
        S2 = p[i][0] * A[1][0] + p[i][1] * A[1][1] + p[i][2] * A[1][2]
        S3 = p[i][0] * A[2][0] + p[i][1] * A[2][1] + p[i][2] * A[2][2]

        ratio = valid_area_ratio(S1, S2, S3)
        total_probability *= ratio

    return total_probability

# 输入部分
n = int(input())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

p = []
for _ in range(n):
    p.append(list(map(float, input().split())))

# 计算结果
result = calculate_probability(n, A, p)
print(f"{result:.6f}")