MOD = 10**9 + 7


def solve(n, c, m):
    # We can use a 2D dp array dp[i][j] where i represents the number of floors considered
    # and j represents the number of airplanes launched so far
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            for k in range(0, min(j + 1, c + 1)):
                # If we assume k airplanes are launched from the i - th floor
                dp[i][j] = (dp[i][j]+dp[i - 1][j - k]) % MOD

    return dp[n][m]


t = int(input())
for _ in range(t):
    n, c, m = map(int, input().split())
    result = solve(n, c, m)
    print(result)
