T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    toggle_count = 0
    for i in range(1, int(k**0.5)+1):
        if k % (i * i) == 0:
            toggle_count += 1
    if toggle_count % 2 == 1:
        print("YES")
    else:
        print("NO")