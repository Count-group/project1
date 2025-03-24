def turn_off_the_lights(n, k, matrix):
    operations = []
    
    # Step 1: Reverse rows to make the number of '1's in each row even
    for i in range(n):
        if sum(matrix[i]) % 2 == 1:
            operations.append((i + 1, 0))  # Reverse row i
            for j in range(n):
                matrix[i][j] = 1 - matrix[i][j]
    
    # Step 2: Reverse columns to make the number of '1's in each column even
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) % 2 == 1:
            operations.append((0, j + 1))  # Reverse column j
            for i in range(n):
                matrix[i][j] = 1 - matrix[i][j]
    
    # Step 3: Count remaining '1's
    remaining_ones = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                remaining_ones.append((i, j))
    
    # If there are more than k remaining '1's, it's impossible
    if len(remaining_ones) > k:
        return -1
    
    # Step 4: Perform single light flips for remaining '1's
    for i, j in remaining_ones:
        operations.append((i + 1, j + 1))
    
    # Check the total number of operations
    if len(operations) > 3 * n:
        return -1
    
    return operations

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
matrix = []
index = 2
for i in range(n):
    row = list(map(int, data[index:index + n]))
    matrix.append(row)
    index += n

# Solve the problem
result = turn_off_the_lights(n, k, matrix)

# Output the result
if result == -1:
    print(-1)
else:
    print(len(result))
    for op in result:
        print(op[0], op[1])