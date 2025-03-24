def perfect_permutation(n):
    if n == 1:
        return [-1]
    
    permutation = []
    remaining = list(range(1, n + 1))
    
    while remaining:
        permutation.append(remaining.pop())
        if remaining:
            permutation.append(remaining.pop(0))
    
    return permutation

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    result = perfect_permutation(n)
    print(' '.join(map(str, result)))