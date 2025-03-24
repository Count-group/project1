t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    @lru_cache(maxsize=None)
    def get_term(m):
        if m <= n:
            return a[m - 1]
        half_m = m // 2
        xor_result = 0
        for i in range(1, half_m + 1):
            xor_result ^= get_term(i)
        return xor_result


    result = 0
    for i in range(l, r + 1):
        result += get_term(i)
    print(result)