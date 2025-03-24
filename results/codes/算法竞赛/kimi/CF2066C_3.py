MOD = 10**9 + 7

def count_valid_sequences(n, a):
    # Initialize dp array
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][0] = 1  # Initial state: P = Q = R = 0

    for i in range(1, n + 1):
        # Transition from P = Q = R to P = Q = R
        dp[i][0] = (dp[i-1][0] * 3) % MOD
        # Transition from P = Q = R to P = Q != R
        dp[i][1] = (dp[i-1][0] + dp[i-1][1] * 2) % MOD

    # The result is the sum of all valid states
    return (dp[n][0] + dp[n][1]) % MOD

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count_valid_sequences(n, a))