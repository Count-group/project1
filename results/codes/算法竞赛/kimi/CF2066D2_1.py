def compute_sequence(n, a):
    for i in range(n + 1, 2 * n + 1):
        a.append(a[0] ^ a[1] ^ a[2] ^ ... ^ a[(i - 1) // 2])
    return a

def sum_of_range(l, r, a, period):
    sum_period = sum(a[:period])
    complete_periods = (r - l + 1) // period
    remaining_terms = (r - l + 1) % period
    sum_remaining = sum(a[l % period:l % period + remaining_terms])
    return complete_periods * sum_period + sum_remaining

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a = compute_sequence(n, a)
    period = 2 * n
    print(sum_of_range(l - 1, r - 1, a, period))