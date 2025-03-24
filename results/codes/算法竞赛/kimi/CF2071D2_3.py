def compute_sequence_sum(n, l, r, a):
    # Step 1: Compute the prefix XOR array for the first n terms
    prefix_xor = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_xor[i] = prefix_xor[i - 1] ^ a[i - 1]
    
    # Step 2: Function to compute the sum of elements in the range [1, m]
    def sum_up_to(m):
        if m <= n:
            return prefix_xor[m]
        else:
            return sum_up_to((m + 1) // 2)
    
    # Step 3: Compute the sum of elements in the range [l, r]
    return sum_up_to(r) - sum_up_to(l - 1)

# Read input
t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(compute_sequence_sum(n, l, r, a))