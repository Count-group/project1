def compute_xor(prefix_xor, m):
    if m <= n:
        return a[m-1]
    else:
        return prefix_xor[(m-1) // 2]

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    prefix_xor = [0] * n
    prefix_xor[0] = a[0]
    for i in range(1, n):
        prefix_xor[i] = prefix_xor[i-1] ^ a[i]
    print(compute_xor(prefix_xor, l))