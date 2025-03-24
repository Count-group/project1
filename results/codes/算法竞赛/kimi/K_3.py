MOD = 998244353

# Precompute factorials and their modular inverses
max_n = 500
factorial = [1] * (max_n + 1)
inverse_factorial = [1] * (max_n + 1)

for i in range(2, max_n + 1):
    factorial[i] = factorial[i - 1] * i % MOD

inverse_factorial[max_n] = pow(factorial[max_n], MOD - 2, MOD)
for i in range(max_n - 1, 0, -1):
    inverse_factorial[i] = inverse_factorial[i + 1] * (i + 1) % MOD

def binomial(n, k):
    if k > n or k < 0:
        return 0
    return factorial[n] * inverse_factorial[k] * inverse_factorial[n - k] % MOD

def solve(n, m):
    if n > m:
        n, m = m, n  # Ensure n <= m

    result = 0
    for k in range(1, n + 1):
        # Number of ways to choose k rows and k columns
        ways_to_choose_rows = binomial(n, k)
        ways_to_choose_columns = binomial(m, k)
        # Contribution to the sum of maximum matchings
        contribution = ways_to_choose_rows * ways_to_choose_columns * factorial[k] % MOD
        result = (result + contribution) % MOD

    return result

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    n, m = map(int, input().split())
    result = solve(n, m)
    print(result)