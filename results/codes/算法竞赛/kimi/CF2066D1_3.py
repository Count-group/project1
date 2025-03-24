MOD = 10**9 + 7

def count_ways(n, c, m):
    # Initialize dp array
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: one way to distribute zero paper airplanes among zero floors

    # Fill dp array
    for i in range(1, n + 1):  # For each floor
        for j in range(m + 1):  # For each possible number of paper airplanes
            for k in range(max(0, j - c), j + 1):  # Ensure at least c paper airplanes are seen
                dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD

    return dp[n][m]

# Read input
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

# Output results
for result in results:
    print(result)