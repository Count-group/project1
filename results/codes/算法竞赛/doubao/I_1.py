from itertools import permutations

# Read input values
N, K, M = map(int, input().split())
# Store the intervals
intervals = []
for _ in range(M):
    l, r = map(int, input().split())
    # Adjust indices to 0 - based
    intervals.append((l - 1, r - 1))

# Generate the original sequence A
A = list(range(1, K + 1)) + [0] * (N - K)
# Initialize the minimum fine to a large value
min_fine = float('inf')

# Generate all possible permutations of the sequence A
for perm in permutations(A):
    total_fine = 0
    # Calculate the total fine for each permutation
    for left, right in intervals:
        # Find the maximum value in the current interval
        total_fine += max(perm[left:right + 1])
    # Update the minimum fine if the current total fine is smaller
    min_fine = min(min_fine, total_fine)

print(min_fine)