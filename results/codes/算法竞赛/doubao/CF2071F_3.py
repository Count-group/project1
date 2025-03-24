# 检查数组是否可以通过移除最多 k 个元素成为 p -towering 数组
def can_make_p_towering(arr, p, k):
    n = len(arr)
    for center in range(n):
        remove_count = 0
        for i in range(n):
            # 计算当前位置所需的最小元素值
            required = p - abs(center - i)
            if arr[i] < required:
                remove_count += 1
                if remove_count > k:
                    break
        else:
            return True
    return False


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 初始化二分查找的左右边界
    left, right = 0, max(a) + k
    while left < right:
        mid = (left + right + 1) // 2
        if can_make_p_towering(a, mid, k):
            left = mid
        else:
            right = mid - 1
    print(left)
    