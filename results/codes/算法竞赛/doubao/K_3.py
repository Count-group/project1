MOD = 998244353

# Function to calculate binomial coefficients
def binomial_coefficient(n, k):
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
    return C

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())

    # Calculate binomial coefficients
    binom_n = binomial_coefficient(n, n)
    binom_m = binomial_coefficient(m, m)

    total = 0
    # Iterate over possible number of rows and columns selected
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            # Number of ways to choose r rows out of n and c columns out of m
            choose_rows = binom_n[n][r]
            choose_cols = binom_m[m][c]

            # The maximum matching size for a bipartite graph formed by r rows and c columns
            max_match = min(r, c)

            # The number of non - empty subsets of points formed by r rows and c columns
            num_points = r * c
            non_empty_subsets = (pow(2, num_points, MOD) - 1)

            # Calculate the contribution of this combination of rows and columns
            contribution = (choose_rows * choose_cols * non_empty_subsets * max_match) % MOD
            total = (total + contribution) % MOD

    print(total)