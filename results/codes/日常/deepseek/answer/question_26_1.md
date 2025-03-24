以下是交换两个数组内容的Python程序：

```python
# 定义两个数组
array1 = [1, 2, 3]
array2 = [4, 5, 6]

print("交换前:")
print("array1 =", array1)
print("array2 =", array2)

# 交换数组内容
array1[:], array2[:] = array2[:], array1[:]

print("\n交换后:")
print("array1 =", array1)
print("array2 =", array2)
```

### 实现说明：
1. **切片赋值**：通过 `array1[:]` 和 `array2[:]` 直接修改原数组的内容，而非改变变量指向的引用。这种方式适用于不同长度的数组，且会保留原始数组的引用不变。
2. **无需临时变量**：利用Python的元组解包特性，直接交换两个数组的全部元素。
3. **通用性**：无论数组长度是否一致，都能正确交换内容。

### 输出结果：
```
交换前:
array1 = [1, 2, 3]
array2 = [4, 5, 6]

交换后:
array1 = [4, 5, 6]
array2 = [1, 2, 3]
```