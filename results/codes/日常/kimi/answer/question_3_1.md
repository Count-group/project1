以下是一个使用Python编写的计算两个数字最小公倍数的程序：

```python
import math

def lcm(a, b):
    # 计算两个数的最小公倍数
    return a * b // math.gcd(a, b)

# 获取用户输入的两个数字
num1 = int(input("请输入第一个数字: "))
num2 = int(input("请输入第二个数字: "))

# 计算并输出结果
result = lcm(num1, num2)
print(f"{num1} 和 {num2} 的最小公倍数是 {result}")
```

### 程序说明：
1. 使用了Python内置的`math.gcd()`函数来计算两个数的最大公约数（Greatest Common Divisor，GCD）。
2. 根据数学公式，两个数的最小公倍数（LCM）可以通过以下公式计算：
   \[
   \text{LCM}(a, b) = \frac{|a \times b|}{\text{GCD}(a, b)}
   \]
   因此，程序中通过`a * b // math.gcd(a, b)`来计算最小公倍数。
3. 用户输入两个数字后，程序会调用`lcm`函数计算并输出结果。

### 示例运行：
```
请输入第一个数字: 12
请输入第二个数字: 18
12 和 18 的最小公倍数是 36
```

你可以将此代码复制到Python环境中直接运行。

