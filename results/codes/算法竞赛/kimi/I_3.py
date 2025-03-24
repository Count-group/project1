from itertools import permutations

def minimize_fines(N, K, M, ranges):
    # Generate the initial sequence with fines and zeros
    sequence = list(range(1, K + 1)) + [0] * (N - K)
    
    # Function to calculate the total fine for a given sequence
    def calculate_fine(seq):
        total_fine = 0
        for l, r in ranges:
            total_fine += max(seq[l-1:r])
        return total_fine
    
    # Generate all permutations of the sequence
    min_fine = float('inf')
    for perm in permutations(sequence):
        current_fine = calculate_fine(perm)
        if current_fine < min_fine:
            min_fine = current_fine
    
    return min_fine

# Read input
N, K, M = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(M)]

# Compute and print the result
print(minimize_fines(N, K, M, ranges))