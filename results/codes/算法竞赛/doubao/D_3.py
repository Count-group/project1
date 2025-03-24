n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_cost = float('inf')

# Try all possible first elements
for start_index in range(n):
    # Try all possible common differences k in the valid range
    for k in range(10**6 + 1):
        current_cost = 0
        valid = True
        for i in range(n):
            expected_value = a[start_index] + (i - start_index) * k
            if expected_value < 0:
                valid = False
                break
            if a[i] != expected_value:
                current_cost += b[i]
        if valid:
            min_cost = min(min_cost, current_cost)

print(min_cost)