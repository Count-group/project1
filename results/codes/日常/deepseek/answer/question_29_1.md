以下是合并两个有序数组的Python程序：

```python
def merge_sorted_arrays(nums1, nums2):
    i = j = 0
    merged = []
    # 遍历两个数组，比较元素大小并合并
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    # 将剩余元素添加到结果中
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    return merged

# 获取用户输入
nums1 = list(map(int, input("请输入第一个有序数组（以空格分隔）：").split()))
nums2 = list(map(int, input("请输入第二个有序数组（以空格分隔）：").split()))

# 合并数组并输出结果
result = merge_sorted_arrays(nums1, nums2)
print("合并后的有序数组：", result)
```

### 使用方法：
1. 运行程序后，输入第一个有序数组（例如：`1 3 5`）
2. 输入第二个有序数组（例如：`2 4 6`）
3. 程序将输出合并后的有序数组（例如：`[1, 2, 3, 4, 5, 6]`）

### 特点：
- 时间复杂度为O(n)，n为两个数组的总长度
- 支持不同长度的数组合并
- 自动处理其中一个数组提前遍历完的情况
- 保持原有数组的升序特性（假设输入数组均为升序排列）

示例输入输出：
```
请输入第一个有序数组（以空格分隔）：1 3 5
请输入第二个有序数组（以空格分隔）：2 4 6
合并后的有序数组： [1, 2, 3, 4, 5, 6]
```