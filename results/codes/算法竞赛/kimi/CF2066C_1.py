MOD = 10**9 + 7

def count_ways(n, a):
    # 初始化 dp 数组
    dp = [[0] * 4 for _ in range(n + 1)]
    dp[0][0] = 1  # 初始状态 P = Q = R = 0

    for i in range(1, n + 1):
        # 当前状态为 P = Q = R
        dp[i][0] = dp[i - 1][0] * 3 % MOD
        # 当前状态为 P = Q != R
        dp[i][1] = (dp[i - 1][1] * 2 + dp[i - 1][0]) % MOD
        # 当前状态为 P = R != Q
        dp[i][2] = (dp[i - 1][2] * 2 + dp[i - 1][0]) % MOD
        # 当前状态为 Q = R != P
        dp[i][3] = (dp[i - 1][3] * 2 + dp[i - 1][0]) % MOD

    # 最终结果为所有合法状态的方案数之和
    return (dp[n][0] + dp[n][1] + dp[n][2] + dp[n][3]) % MOD

# 读取输入
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count_ways(n, a))