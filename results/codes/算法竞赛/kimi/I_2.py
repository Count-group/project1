def minimize_fines(N, K, M, ranges):
    # Step 1: Sort ranges by starting point and then by ending point
    ranges.sort(key=lambda x: (x[0], x[1]))
    
    # Step 2: Count coverage for each position
    coverage = [0] * N
    for l, r in ranges:
        for i in range(l-1, r):
            coverage[i] += 1
    
    # Step 3: Place fines in positions with the lowest coverage
    sequence = [0] * N
    fines = list(range(K, 0, -1))  # List of fines from K to 1
    for fine in fines:
        # Find the position with the lowest coverage that is still 0
        min_coverage_index = coverage.index(min(coverage))
        sequence[min_coverage_index] = fine
        coverage[min_coverage_index] = float('inf')  # Mark as placed
    
    # Step 4: Calculate the total fine
    total_fine = 0
    for l, r in ranges:
        total_fine += max(sequence[l-1:r])
    
    return total_fine

# Read input
N, K, M = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(M)]

# Compute and print the result
print(minimize_fines(N, K, M, ranges))