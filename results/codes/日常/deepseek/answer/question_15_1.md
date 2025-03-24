要实现生成数组所有元素组成的集合的所有子集，可以采用位运算的方法。首先处理输入数组以去除重复元素并保持顺序，然后利用二进制数的每一位表示是否包含对应元素来生成子集。以下是具体的Python代码：

```python
def subsets(nums):
    # 去除重复元素并保持原顺序
    seen = set()
    unique_nums = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            unique_nums.append(num)
    n = len(unique_nums)
    result = []
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):  # 检查第j位是否为1
                subset.append(unique_nums[j])
        result.append(subset)
    return result

if __name__ == "__main__":
    # 读取输入并转换为整数列表
    nums = list(map(int, input().split()))
    # 生成所有子集
    result = subsets(nums)
    # 输出结果
    print(result)
```

### 代码解释：
1. **输入处理**：使用`input().split()`读取输入并将其转换为整数列表。
2. **去重处理**：通过集合`seen`去除重复元素，同时保持原顺序，确保生成的子集基于唯一元素。
3. **位运算生成子集**：
   - 遍历从0到2^n - 1的所有整数，每个整数表示一个子集。
   - 对于每个整数，检查其二进制表示的每一位。若某位为1，则将对应位置的元素加入子集。
4. **输出结果**：将所有生成的子集以列表形式输出。

该方法高效且简洁，时间复杂度为O(n * 2^n)，适用于处理元素数量适中的数组。