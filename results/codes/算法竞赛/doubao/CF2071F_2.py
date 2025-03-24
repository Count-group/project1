# 检查数组是否可以通过移除最多 k 个元素成为 p -towering 数组
def can_make_p_towering(arr, p, k):
    n = len(arr)
    for center in range(n):
        removed = 0
        for i in range(n):
            if arr[i] < p - abs(center - i):
                removed += 1
                if removed > k:
                    break
        else:
            return True
    return False


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 二分查找最大的 p 值
    left, right = 0, 10**9 + k
    while left < right:
        mid = (left + right + 1) // 2
        if can_make_p_towering(a, mid, k):
            left = mid
        else:
            right = mid - 1
    print(left)
    