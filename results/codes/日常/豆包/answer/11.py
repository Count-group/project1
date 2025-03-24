def get_adjacent_pairs(arr):
    return [(arr[i], arr[i + 1]) for i in range(len(arr) - 1)]


# 示例使用
arr = [1, 2, 3, 4, 5]
result = get_adjacent_pairs(arr)
print(result)
    