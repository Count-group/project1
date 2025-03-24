import sys
from sys import stdin
from functools import lru_cache

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n, l, r = map(int, data[idx:idx+3])
        idx +=3
        a = list(map(int, data[idx:idx+n]))
        idx +=n
        
        prefix_xor = [0]*(n+1)
        for i in range(1, n+1):
            prefix_xor[i] = prefix_xor[i-1] ^ a[i-1]
        
        memo_a = {}
        memo_f = {}
        
        def compute_f(m):
            if m <= n:
                return prefix_xor[m]
            if m in memo_f:
                return memo_f[m]
            prev_f = compute_f(m-1)
            am = compute_a(m)
            current_f = prev_f ^ am
            memo_f[m] = current_f
            return current_f
        
        def compute_a(m):
            if m <= n:
                return a[m-1]
            if m in memo_a:
                return memo_a[m]
            k = m // 2
            res = compute_f(k)
            memo_a[m] = res
            return res
        
        total = 0
        for m in range(l, r+1):
            if m <= n:
                total += a[m-1]
            else:
                total += compute_a(m)
        print(total)

if __name__ == '__main__':
    main()