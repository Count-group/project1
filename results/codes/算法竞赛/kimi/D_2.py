n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_cost = float('inf')

for k in range(1000001):
    cost = 0
    for i in range(n):
        if a[i] != a[0] + (i-1)*k:
            cost += b[i]
    min_cost = min(min_cost, cost)

print(min_cost)