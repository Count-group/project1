MOD = 10**9 + 7


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Initialize dp array
        dp = [[[[0 for _ in range(1 << 30)] for _ in range(1 << 30)] for _ in range(1 << 30)] for _ in range(n + 1)]
        dp[0][0][0][0] = 1

        for i in range(n):
            for p in range(1 << 30):
                for q in range(1 << 30):
                    for r in range(1 << 30):
                        if dp[i][p][q][r] == 0:
                            continue
                        # Case 1: P := P ^ a[i]
                        new_p = p ^ a[i]
                        if not (new_p != q and new_p != r and q != r):
                            dp[i + 1][new_p][q][r] = (dp[i + 1][new_p][q][r] + dp[i][p][q][r]) % MOD
                        # Case 2: Q := Q ^ a[i]
                        new_q = q ^ a[i]
                        if not (p != new_q and p != r and new_q != r):
                            dp[i + 1][p][new_q][r] = (dp[i + 1][p][new_q][r] + dp[i][p][q][r]) % MOD
                        # Case 3: R := R ^ a[i]
                        new_r = r ^ a[i]
                        if not (p != q and p != new_r and q != new_r):
                            dp[i + 1][p][q][new_r] = (dp[i + 1][p][q][new_r] + dp[i][p][q][r]) % MOD

        ans = 0
        for p in range(1 << 30):
            for q in range(1 << 30):
                for r in range(1 << 30):
                    ans = (ans + dp[n][p][q][r]) % MOD
        print(ans)


if __name__ == "__main__":
    solve()
