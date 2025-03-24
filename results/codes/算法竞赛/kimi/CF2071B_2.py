import math

def is_perfect_square(x):
    return int(math.isqrt(x)) ** 2 == x

def perfect_permutation(n):
    if n == 1:
        return [-1]
    
    # Initialize the permutation list
    permutation = []
    
    # For even n, use the pattern [2, 4, 1, 3, 6, 5, 8, 7, ...]
    if n % 2 == 0:
        for i in range(1, n // 2 + 1):
            permutation.append(2 * i)
            permutation.append(2 * i - 1)
    # For odd n, use the pattern [n, 1, n-1, 2, n-2, 3, ...]
    else:
        permutation.append(n)
        permutation.append(1)
        for i in range(2, (n - 1) // 2 + 1):
            permutation.append(n - i + 1)
            permutation.append(i)
    
    return permutation

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    result = perfect_permutation(n)
    print(' '.join(map(str, result)))