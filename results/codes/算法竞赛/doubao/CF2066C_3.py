MOD = 10**9 + 7

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # dp[i][0] represents the number of ways when P = Q = R
    # dp[i][1] represents the number of ways when exactly two of P, Q, R are equal
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        num = a[i - 1]
        # Transition from all - equal state
        dp[i][1] = (dp[i][1] + 3 * dp[i - 1][0]) % MOD
        # Transition from two - equal state
        dp[i][0] = (dp[i][0] + dp[i - 1][1]) % MOD
        dp[i][1] = (dp[i][1] + 2 * dp[i - 1][1]) % MOD

    result = (dp[n][0] + dp[n][1]) % MOD
    print(result)
