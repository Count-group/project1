def can_make_p_towering(arr, p, k):
    n = len(arr)
    for i in range(n):
        removed = 0
        valid = True
        for j in range(n):
            if arr[j] < p - abs(i - j):
                removed += 1
                if removed > k:
                    valid = False
                    break
        if valid:
            return True
    return False


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    left, right = 0, max(a) + k
    while left < right:
        mid = (left + right + 1) // 2
        if can_make_p_towering(a, mid, k):
            left = mid
        else:
            right = mid - 1
    print(left)