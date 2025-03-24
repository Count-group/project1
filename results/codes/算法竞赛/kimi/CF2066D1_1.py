MOD = 10**9 + 7

def count_ways(n, c, m):
    # 初始化 dp 数组
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1  # 初始状态

    for i in range(1, m + 1):  # 遍历每架纸飞机
        for j in range(1, n + 1):  # 遍历每层楼
            for k in range(1, j + 1):  # 遍历前 i-1 架纸飞机的可能状态
                if i - k < c:  # 确保从第 j 层楼的人的视角来看，已经扔出的纸飞机数量不超过 c
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD

    # 计算最终结果
    result = 0
    for j in range(1, n + 1):
        result = (result + dp[m][j]) % MOD

    return result

# 读取输入
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    c = int(data[index + 1])
    m = int(data[index + 2])
    index += 3
    results.append(count_ways(n, c, m))

# 输出结果
for result in results:
    print(result)