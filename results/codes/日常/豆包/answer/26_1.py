def swap_arrays(arr1, arr2):
    return arr2, arr1


# 示例数组
array1 = [1, 2, 3]
array2 = [4, 5, 6]

print("交换前:")
print("数组 1:", array1)
print("数组 2:", array2)

array1, array2 = swap_arrays(array1, array2)

print("交换后:")
print("数组 1:", array1)
print("数组 2:", array2)
    