def solve(n, m):
    mod = 998244353
    total_sum = n * m * (2 ** (n * m - 2)) % mod
    return total_sum

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    n, m = map(int, input().split())
    result = solve(n, m)
    print(result)