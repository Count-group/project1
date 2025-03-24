def count_squares(a, b):
    # The triangle ABC is a right triangle with vertices at (a, 0), (0, b), and (0, 0).
    # The area of the triangle can be calculated as (1/2) * base * height.
    area = (a * b) // 2
    
    # The number of squares that belong to the triangle is equal to the area of the triangle.
    # This is because each unit square is 1x1, and the area of the triangle gives the count of such squares.
    return area

# Read input
a, b = map(int, input().split())

# Calculate and print the result
print(count_squares(a, b))