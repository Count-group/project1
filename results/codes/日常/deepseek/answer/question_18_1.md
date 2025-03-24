以下是输出给定范围内所有质数的Python程序：

```python
def is_prime(n):
    """判断一个数是否为质数"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w  # 交替步长2和4，跳过3的倍数
    return True

# 获取用户输入
start = int(input("请输入起始数："))
end = int(input("请输入结束数："))

# 确保start <= end
if start > end:
    start, end = end, start

primes = []

# 处理2和3的情况
if start <= 2 <= end:
    primes.append(2)
if start <= 3 <= end:
    primes.append(3)

# 从5开始检查奇数
current = max(start, 5)
# 调整起始点为奇数
if current % 2 == 0:
    current += 1

# 遍历所有奇数并检查
for num in range(current, end + 1, 2):
    if is_prime(num):
        primes.append(num)

# 输出结果
print(f"在{start}和{end}之间的质数有：{primes}")
```

### 程序说明：
1. **质数判断函数 `is_prime`**：
   - 处理小于等于3的数。
   - 排除所有能被2或3整除的数。
   - 使用6k±1优化法，仅检查可能的质数候选，减少循环次数。

2. **输入处理**：
   - 用户输入起始和结束数，自动处理大小顺序。

3. **特殊质数处理**：
   - 直接处理2和3，减少后续计算量。

4. **遍历优化**：
   - 从5开始，仅遍历奇数，提高效率。

该程序能高效地找到给定范围内的所有质数，适合处理较大范围的质数查找。