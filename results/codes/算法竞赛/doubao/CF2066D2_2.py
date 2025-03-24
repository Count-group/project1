MOD = 10**9 + 7


def solve():
    t = int(input())
    for _ in range(t):
        n, c, m = map(int, input().split())
        a = list(map(int, input().split()))

        # Initialize the dynamic programming array
        dp = [0] * (1 << (n * c))
        dp[0] = 1

        for k in range(m):
            new_dp = [0] * (1 << (n * c))
            if a[k] == 0:
                for state in range(1 << (n * c)):
                    if dp[state] == 0:
                        continue
                    for i in range(n):
                        valid = True
                        new_state = state
                        for j in range(i + 1):
                            launches = (new_state >> (j * c)) & ((1 << c) - 1)
                            if launches >= c:
                                valid = False
                                break
                            new_state += (1 << (j * c))
                        if valid:
                            new_dp[new_state] = (new_dp[new_state] + dp[state]) % MOD
            else:
                for state in range(1 << (n * c)):
                    if dp[state] == 0:
                        continue
                    i = a[k] - 1
                    valid = True
                    new_state = state
                    for j in range(i + 1):
                        launches = (new_state >> (j * c)) & ((1 << c) - 1)
                        if launches >= c:
                            valid = False
                            break
                        new_state += (1 << (j * c))
                    if valid:
                        new_dp[new_state] = (new_dp[new_state] + dp[state]) % MOD
            dp = new_dp

        ans = 0
        for state in range(1 << (n * c)):
            valid = True
            for i in range(n):
                launches = (state >> (i * c)) & ((1 << c) - 1)
                if launches < c:
                    valid = False
                    break
            if valid:
                ans = (ans + dp[state]) % MOD

        print(ans)


if __name__ == "__main__":
    solve()
    