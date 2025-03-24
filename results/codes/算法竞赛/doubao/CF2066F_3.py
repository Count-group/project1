MOD = 10**9 + 7


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result


def mod_inverse(a):
    return pow(a, MOD - 2, MOD)


def combination(n, k):
    if k > n:
        return 0
    numerator = factorial(n)
    denominator = (factorial(k) * factorial(n - k)) % MOD
    return (numerator * mod_inverse(denominator)) % MOD


t = int(input())
for _ in range(t):
    n, c, m = map(int, input().split())
    # The number of airplanes launched from floor n must be m - c
    # We need to place these m - c airplanes among the first c positions
    num_ways = combination(c, m - c)
    print(num_ways)