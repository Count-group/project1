def is_feasible(a, p, k):
    n = len(a)
    # Calculate the minimum number of elements to remove for each possible center i
    removals = [0] * n
    for i in range(n):
        for j in range(n):
            if a[j] < p - abs(i - j):
                removals[i] += 1
    # Check if there exists a center i such that the number of removals is at most k
    return min(removals) <= k

def max_p_towering(a, k):
    low, high = 1, max(a)
    while low < high:
        mid = (low + high + 1) // 2
        if is_feasible(a, mid, k):
            low = mid
        else:
            high = mid - 1
    return low

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_p_towering(a, k))