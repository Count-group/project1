MOD = 998244353


def solve(n, m):
    total = 0
    # Generate all non - empty subsets of rows and columns
    for row_mask in range(1, 1 << n):
        for col_mask in range(1, 1 << m):
            # Calculate the number of points in the current subset
            num_points = bin(row_mask).count('1') * bin(col_mask).count('1')
            # The maximum matching of a bipartite graph with num_points points
            max_matching = min(bin(row_mask).count('1'), bin(col_mask).count('1'))
            # Calculate the number of non - empty subsets that contain this set of rows and columns
            num_subsets = (2**(num_points) - 1) * (2**((n - bin(row_mask).count('1')) * (m - bin(col_mask).count('1'))))
            total = (total + max_matching * num_subsets) % MOD

    return total


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(solve(n, m))
