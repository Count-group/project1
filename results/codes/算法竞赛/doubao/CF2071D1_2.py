import sys

# Increase the recursion limit
sys.setrecursionlimit(1 << 25)


def get_element(n, a, m):
    if m <= n:
        return a[m - 1]
    # Calculate the XOR of the first floor(m/2) elements
    xor_val = 0
    current = m // 2
    while True:
        if current <= n:
            for i in range(1, current + 1):
                xor_val ^= a[i - 1]
            break
        xor_val ^= get_element(n, a, current)
        current //= 2
    return xor_val


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, l, r = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    result = get_element(n, a, l)
    print(result)
