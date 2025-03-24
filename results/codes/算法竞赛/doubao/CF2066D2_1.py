MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n, c, m = map(int, data[idx:idx+3])
        idx +=3
        a = list(map(int, data[idx:idx+m]))
        idx +=m
        
        from collections import defaultdict

        dp = defaultdict(int)
        initial = tuple([0]*(n+1))  # cnt[0] unused, cnt[1..n]
        dp[initial] = 1

        for pos in range(m):
            current = a[pos]
            new_dp = defaultdict(int)
            for state in dp:
                cnt = list(state)
                if current != 0:
                    j = current
                    if j < 1 or j > n:
                        continue
                    if cnt[j] >= c:
                        continue
                    new_cnt = cnt.copy()
                    for k in range(j, n+1):
                        new_cnt[k] += 1
                    new_state = tuple(new_cnt)
                    new_dp[new_state] = (new_dp[new_state] + dp[state]) % MOD
                else:
                    for j in range(1, n+1):
                        if cnt[j] >= c:
                            continue
                        new_cnt = cnt.copy()
                        for k in range(j, n+1):
                            new_cnt[k] += 1
                        new_state = tuple(new_cnt)
                        new_dp[new_state] = (new_dp[new_state] + dp[state]) % MOD
            dp = new_dp

        total = 0
        for state in dp:
            valid = True
            for i in range(1, n+1):
                if state[i] < c:
                    valid = False
                    break
            if valid:
                total = (total + dp[state]) % MOD
        print(total % MOD)

if __name__ == '__main__':
    main()