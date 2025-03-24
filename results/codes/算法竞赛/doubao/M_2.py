T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    divisor_count = 0
    i = 1
    while i * i <= k:
        if k % (i * i) == 0:
            divisor_count += 1
        i += 1

    if divisor_count % 2 == 1:
        print("YES")
    else:
        print("NO")
