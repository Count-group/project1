# Read input values for n and k
n, k = map(int, input().split())
# Initialize the matrix of lights
lights = [list(map(int, input().split())) for _ in range(n)]

# Function to reverse the state of a row
def flip_row(matrix, row):
    for j in range(n):
        matrix[row][j] = 1 - matrix[row][j]
    return matrix

# Function to reverse the state of a column
def flip_col(matrix, col):
    for i in range(n):
        matrix[i][col] = 1 - matrix[i][col]
    return matrix

# Function to reverse the state of a single light
def flip_light(matrix, x, y):
    matrix[x][y] = 1 - matrix[x][y]
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
                lights = flip_light(lights, i, j)
                operations.append((i + 1, j + 1))
                single_flip_count += 1
            else:
                # If we exceed the limit of single - light flips, it's impossible
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
        # Print each operation
        for op in operations:
            print(op[0], op[1])
    else:
        print(-1)
