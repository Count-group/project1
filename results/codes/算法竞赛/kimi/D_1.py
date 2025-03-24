from math import gcd
from functools import reduce

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

differences = [a[i] - a[0] for i in range(1, n)]
gcd_diff = reduce(gcd, differences)

divisors = [i for i in range(1, gcd_diff + 1) if gcd_diff % i == 0]

min_cost = float('inf')

for k in divisors:
    cost = 0
    for i in range(n):
        if a[i] != a[0] + (i-1)*k:
            cost += b[i]
    min_cost = min(min_cost, cost)

print(min_cost)