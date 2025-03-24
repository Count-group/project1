from math import gcd
from functools import reduce

def get_divisors(x):
    divisors = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            divisors.append(i)
            if i != x // i:
                divisors.append(x // i)
    return sorted(divisors)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate differences
differences = [a[i+1] - a[i] for i in range(n-1)]

# Calculate GCD of differences
if differences:
    gcd_diff = reduce(gcd, differences)
else:
    gcd_diff = 0

# Get all divisors of the GCD
divisors = get_divisors(gcd_diff)

# Initialize minimum cost to a large number
min_cost = float('inf')

# Check each divisor as a potential k
for k in divisors:
    cost = 0
    for i in range(n):
        if a[i] != a[0] + (i - 1) * k:
            cost += b[i]
    min_cost = min(min_cost, cost)

# Special case when k = 0
cost = sum(b)
min_cost = min(min_cost, cost)

print(min_cost)