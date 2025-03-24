a, b = map(int, input().split())
count = 0
# Iterate over all possible unit squares
for x in range(a):
    for y in range(b):
        # Calculate the number of vertices of the square that are inside the triangle
        vertices_inside = 0
        # Check each vertex of the square
        if y <= (-b / a) * x + b:
            vertices_inside += 1
        if y <= (-b / a) * (x + 1)+ b:
            vertices_inside += 1
        if y + 1 <= (-b / a) * x + b:
            vertices_inside += 1
        if y + 1 <= (-b / a) * (x + 1)+ b:
            vertices_inside += 1
        # If at least half of the vertices are inside the triangle
        if vertices_inside >= 2:
            count += 1
print(count)