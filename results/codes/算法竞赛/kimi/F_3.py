def final_value_of_x(k, z, b):
    # Initialize the result as an empty string
    result = []
    
    # Iterate over each bit position
    for i in range(k):
        if b[i] % 2 == 1:
            result.append('1')  # If count is odd, the bit will be 1
        else:
            result.append('0')  # If count is even, the bit will be 0
    
    # Join the list into a single string and return
    return ''.join(result)

# Read input
k, z = map(int, input().split())
b = list(map(int, input().split()))

# Compute and output the final value of x
print(final_value_of_x(k, z, b))