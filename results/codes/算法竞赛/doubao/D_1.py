n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_cost = float('inf')
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        k = (a[j] - a[i]) // (j - i) if j - i != 0 else 0
        if 0 <= k <= 10**6:
            cost = 0
            for l in range(n):
                if a[l] != a[i] + (l - i) * k:
                    cost += b[l]
            total_cost = min(total_cost, cost)

print(total_cost)