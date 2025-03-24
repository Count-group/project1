# Read the values of n and k from the input
n, k = map(int, input().split())
# Initialize a 2D list to represent the state of the lights
lights = [list(map(int, input().split())) for _ in range(n)]

# Function to reverse the state of a row
def flip_row(matrix, row_index):
    for col in range(n):
        matrix[row_index][col] = 1 - matrix[row_index][col]
    return matrix

# Function to reverse the state of a column
def flip_col(matrix, col_index):
    for row in range(n):
        matrix[row][col_index] = 1 - matrix[row][col_index]
    return matrix

# Function to reverse the state of a single light
def flip_single_light(matrix, row, col):
    matrix[row][col] = 1 - matrix[row][col]
    return matrix

# List to store the operations
operations = []

# First, make the first column all 0 by flipping rows
for i in range(n):
    if lights[i][0] == 1:
        lights = flip_row(lights, i)
        operations.append((i + 1, 0))

# Then, make the first row (except the first element) all 0 by flipping columns
for j in range(1, n):
    if lights[0][j] == 1:
        lights = flip_col(lights, j)
        operations.append((0, j + 1))

# Count the number of single - light flips
single_flip_count = 0
for i in range(n):
    for j in range(n):
        if lights[i][j] == 1:
            if single_flip_count < k:
                lights = flip_single_light(lights, i, j)
                operations.append((i + 1, j + 1))
                single_flip_count += 1
            else:
                print(-1)
                break
    else:
        continue
    break
else:
    # Check if all lights are off
    all_off = True
    for row in lights:
        if 1 in row:
            all_off = False
            break

    if all_off:
        # Print the number of operations
        print(len(operations))
        # Print each operation according to the format
        for op in operations:
            print(f"{op[0]} {op[1]}")
    else:
        print(-1)