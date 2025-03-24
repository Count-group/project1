def is_feasible(a, p, k):
    n = len(a)
    # Create an array to store the minimum required value for each position
    required = [p - abs(i - j) for j in range(n) for i in range(n)]
    required.sort()
    
    # Use a sliding window to count the number of elements that need to be removed
    count = 0
    for i in range(n):
        if a[i] < required[i]:
            count += 1
        if count > k:
            return False
    return True

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