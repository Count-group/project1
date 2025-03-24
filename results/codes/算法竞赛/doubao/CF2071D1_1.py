import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, l, r = map(int, data[idx:idx+3])
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Precompute S for 1..n
        S = [0] * (n + 1)
        S[1] = a[0]
        for i in range(2, n + 1):
            S[i] = S[i-1] ^ a[i-1]
        
        memo = {}
        
        def compute_S(k):
            if k in memo:
                return memo[k]
            if k <= n:
                return S[k]
            res = compute_S(k-1) ^ compute_S(k // 2)
            memo[k] = res
            return res
        
        if l <= n:
            results.append(str(a[l-1]))
        else:
            k = l // 2
            results.append(str(compute_S(k)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()