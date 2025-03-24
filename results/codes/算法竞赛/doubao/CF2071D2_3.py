t = int(input())

# Function to calculate the prefix XOR of the sequence
def prefix_xor(n, a):
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] ^ a[i - 1]
    return prefix

# Function to calculate the value of a_m
def get_a(m, n, prefix, memo):
    if m <= n:
        return a[m - 1]
    if m in memo:
        return memo[m]
    k = m // 2
    val = prefix[k] if k <= n else get_a(k, n, prefix, memo)
    for i in range(n + 1, k + 1):
        val ^= get_a(i, n, prefix, memo)
    memo[m] = val
    return val

# Function to calculate the sum of elements in the range [l, r]
def sum_in_range(l, r, n, a):
    prefix = prefix_xor(n, a)
    memo = {}
    total = 0
    for i in range(l, r + 1):
        total += get_a(i, n, prefix, memo)
    return total


for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum_in_range(l, r, n, a))
