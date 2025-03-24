import math

def is_perfect_square(x):
    root = int(math.isqrt(x))
    return root * root == x

def perfect_permutation(n):
    if n == 1:
        return [-1]
    
    # Initialize the permutation and the list of numbers
    permutation = []
    numbers = list(range(1, n + 1))
    
    # Initialize the cumulative sum
    cumulative_sum = 0
    
    while numbers:
        # Try placing the largest number first
        for num in [numbers[-1], numbers[0]]:
            if not is_perfect_square(cumulative_sum + num):
                cumulative_sum += num
                permutation.append(num)
                numbers.remove(num)
                break
    
    return permutation

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    result = perfect_permutation(n)
    print(' '.join(map(str, result)))