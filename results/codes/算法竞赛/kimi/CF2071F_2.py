def is_feasible(a, p, k):
    n = len(a)
    # For each possible center i, calculate the number of elements to remove
    for i in range(n):
        remove_count = 0
        for j in range(n):
            if a[j] < p - abs(i - j):
                remove_count += 1
        if remove_count <= k:
            return True
    return False

def max_p_towering(a, k):
    low, high = 1, max(a)
    result = 1
    while low <= high:
        mid = (low + high) // 2
        if is_feasible(a, mid, k):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

# Read input
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_p_towering(a, k))