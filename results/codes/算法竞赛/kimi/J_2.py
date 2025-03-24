def count_squares(a, b):
    count = 0

    # Iterate over each unit square in the grid
    for x in range(a):
        for y in range(b):
            # Check the position of the top-right corner of the square
            if (x + 1) / a + (y + 1) / b <= 1:
                count += 1
            # Check the position of the bottom-left corner of the square
            elif x / a + y / b < 1:
                count += 1

    return count

# Read input
a, b = map(int, input().split())

# Calculate and print the result
print(count_squares(a, b))