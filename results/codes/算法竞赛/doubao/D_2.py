n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Initialize the minimum cost to a large value
min_cost = float('inf')

# Iterate through all possible pairs (i, j)
for i in range(n):
    for j in range(i + 1, n):
        # Calculate the common difference k
        if (j - i) != 0:
            k = (a[j] - a[i]) // (j - i)
            # Check if the calculated k is within the valid range
            if 0 <= k <= 10**6 and (a[j] - a[i]) % (j - i) == 0:
                current_cost = 0
                for l in range(n):
                    # Calculate the expected value in the arithmetic sequence
                    expected = a[i]+(l - i)*k
                    if a[l] != expected:
                        current_cost += b[l]
                min_cost = min(min_cost, current_cost)

# If the sequence is already good (e.g., when we consider all elements equal), the cost is 0
# We can also try to keep all elements the same (k = 0)
cost_all_same = 0
for l in range(n):
    if a[l] != a[0]:
        cost_all_same += b[l]
min_cost = min(min_cost, cost_all_same)

print(min_cost)
