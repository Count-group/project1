MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        c = int(data[idx+1])
        m = int(data[idx+2])
        idx +=3
        a = list(map(int, data[idx:idx+m]))
        idx +=m
        
        # Check if m > 2c, which is impossible
        if m > 2 * c:
            print(0)
            continue
        
        # The number of n's must be m - c, and they must be placed in the first c positions
        k = m - c
        if k < 0 or k > c:
            print(0)
            continue
        
        # Compute combination C(c, k)
        # Precompute factorial and inverse factorial modulo MOD
        max_n = c
        fact = [1] * (max_n + 1)
        for i in range(1, max_n +1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact = [1]*(max_n +1)
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n-1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        def comb(n, k):
            if n <0 or k <0 or k >n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD
        
        res = comb(c, k)
        print(res)

if __name__ == '__main__':
    main()