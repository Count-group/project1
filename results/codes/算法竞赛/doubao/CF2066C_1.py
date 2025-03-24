MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        dp_all = [0] * (n + 1)
        dp_two = [0] * (n + 1)
        dp_all[0] = 1
        
        for i in range(1, n + 1):
            # Transition from all equal
            dp_two[i] = (dp_two[i] + 3 * dp_all[i-1]) % MOD
            
            # Transition from two equal
            dp_all[i] = (dp_all[i] + dp_two[i-1]) % MOD
            dp_two[i] = (dp_two[i] + 2 * dp_two[i-1]) % MOD
        
        print((dp_all[n] + dp_two[n]) % MOD)

if __name__ == "__main__":
    solve()