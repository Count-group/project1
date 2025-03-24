n, k = map(int, input().split())
lights = [list(map(int, input().split())) for _ in range(n)]


def flip_row(matrix, row):
    for j in range(n):
        matrix[row][j] = 1 - matrix[row][j]
    return matrix


def flip_col(matrix, col):
    for i in range(n):
        matrix[i][col] = 1 - matrix[i][col]
    return matrix


def flip_light(matrix, x, y):
    matrix[x][y] = 1 - matrix[x][y]
    return matrix


operations = []
for i in range(n):
    if lights[i][0] == 1:
        lights = flip_row(lights, i)
        operations.append((i + 1, 0))


for j in range(1, n):
    if lights[0][j] == 1:
        lights = flip_col(lights, j)
        operations.append((0, j + 1))


single_flip_count = 0
for i in range(n):
    for j in range(n):
        if lights[i][j] == 1:
            if single_flip_count < k:
                lights = flip_light(lights, i, j)
                operations.append((i + 1, j + 1))
                single_flip_count += 1
            else:
                print(-1)
                break
    else:
        continue
    break
else:
    all_off = True
    for row in lights:
        if 1 in row:
            all_off = False
            break

    if all_off:
        print(len(operations))
        for op in operations:
            print(op[0], op[1])
    else:
        print(-1)