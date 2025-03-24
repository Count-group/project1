def minimize_fines(N, K, M, ranges):
    # Sort ranges by length in ascending order
    ranges.sort(key=lambda x: x[1] - x[0] + 1)
    
    # Initialize the sequence with zeros
    sequence = [0] * N
    
    # Place the fines from K down to 1
    for fine in range(K, 0, -1):
        placed = False
        for l, r in ranges:
            if not placed and sequence[l-1:r] == [0] * (r - l + 1):
                sequence[l-1] = fine
                placed = True
        if not placed:
            # If no suitable range is found, place the fine in the first available position
            for i in range(N):
                if sequence[i] == 0:
                    sequence[i] = fine
                    break
    
    # Calculate the total fine
    total_fine = 0
    for l, r in ranges:
        total_fine += max(sequence[l-1:r])
    
    return total_fine

# Read input
N, K, M = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(M)]

# Compute and print the result
print(minimize_fines(N, K, M, ranges))