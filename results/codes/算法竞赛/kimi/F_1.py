def final_value_of_x(k, z, b):
    x = 0
    for i in range(k):
        if b[i] % 2 == 1:
            x |= (1 << i)
    return format(x, '0' + str(k) + 'b')

# Read input
k, z = map(int, input().split())
b = list(map(int, input().split()))

# Compute and output the final value of x
print(final_value_of_x(k, z, b))