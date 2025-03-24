def count_squares(a, b):
    count = 0

    # Iterate over each unit square in the grid
    for x in range(a):
        for y in range(b):
            # Check the positions of the four corners of the square
            corners_inside = 0
            for dx in range(2):
                for dy in range(2):
                    if (x + dx) / a + (y + dy) / b <= 1:
                        corners_inside += 1
            
            # If at least 3 corners are inside or on the boundary, count the square
            if corners_inside >= 3:
                count += 1

    return count

# Read input
a, b = map(int, input().split())

# Calculate and print the result
print(count_squares(a, b))