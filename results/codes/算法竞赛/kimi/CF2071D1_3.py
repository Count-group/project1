def solve():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Precompute the cumulative XOR values for the first n terms
    prefix_xor = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_xor[i] = prefix_xor[i - 1] ^ a[i - 1]
    
    # Function to get the value of a_l for l > n
    def get_value(l):
        if l <= n:
            return a[l - 1]
        else:
            # Use the recursive definition
            half = l // 2
            return prefix_xor[half]
    
    # Since l = r, we only need to find a_l
    print(get_value(l))

t = int(input())
for _ in range(t):
    solve()