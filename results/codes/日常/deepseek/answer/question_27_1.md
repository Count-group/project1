以下是一个用于计算一组数字中位数的Python程序：

```python
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle_index = n // 2
    if n % 2 == 1:
        return sorted_numbers[middle_index]
    else:
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2

# 获取用户输入
user_input = input("请输入一组数字，用空格分隔：")
try:
    numbers = list(map(float, user_input.split()))
    if not numbers:
        print("错误：未输入任何数字。")
    else:
        median = calculate_median(numbers)
        print("这组数字的中位数是：", median)
except ValueError:
    print("错误：请输入有效的数字。")
```

### 程序说明：
1. **函数 `calculate_median`**：
   - 将输入列表排序。
   - 计算列表长度，判断奇偶性。
   - 奇数长度时返回中间元素，偶数时返回中间两个数的平均值。

2. **输入处理**：
   - 用户输入以空格分隔的数字字符串。
   - 转换为浮点数列表，处理无效输入。

3. **示例输出**：
   - 输入 `3 1 4`，输出中位数 `3`。
   - 输入 `2 5 3 4`，输出中位数 `3.5`。

### 使用方法：
运行程序后，按照提示输入数字，程序会自动计算并输出中位数。程序包含基本的错误处理，确保输入有效性。