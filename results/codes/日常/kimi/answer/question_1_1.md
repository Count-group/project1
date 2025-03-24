以下是一个将中缀表达式转换为后缀表达式的 Python 程序。该程序使用栈来处理运算符和括号，并根据运算符的优先级进行转换。

```python
def infix_to_postfix(expression):
    # 定义运算符优先级
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    # 用于存储操作数或结果的栈
    stack = []
    # 用于存储后缀表达式的输出
    output = []
    # 遍历中缀表达式中的每个字符
    for char in expression:
        # 如果是数字或字母，直接添加到输出
        if char.isdigit() or (char.isalpha() and char not in precedence):
            output.append(char)
        # 如果是左括号，压入栈中
        elif char == '(':
            stack.append(char)
        # 如果是右括号，弹出栈中的元素直到遇到左括号
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # 弹出左括号，不加入输出
        # 如果是运算符
        else:
            # 弹出优先级更高或相等的运算符到输出
            while stack and stack[-1] != '(' and precedence[char] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
    # 弹出栈中剩余的运算符到输出
    while stack:
        output.append(stack.pop())
    # 返回后缀表达式
    return ' '.join(output)

# 测试
infix_expression = "2+3*5/(1-9)+7"
postfix_expression = infix_to_postfix(infix_expression)
print("中缀表达式:", infix_expression)
print("后缀表达式:", postfix_expression)
```

### 程序说明：
1. **运算符优先级**：定义了一个字典 `precedence` 来存储运算符的优先级。
2. **栈的使用**：栈用于暂存运算符和括号。
3. **遍历中缀表达式**：
   - 如果是数字或字母，直接加入输出。
   - 如果是左括号，压入栈中。
   - 如果是右括号，弹出栈中的元素直到遇到左括号。
   - 如果是运算符，弹出优先级更高或相等的运算符到输出，然后将当前运算符压入栈中。
4. **剩余运算符**：最后将栈中剩余的运算符弹出到输出。

### 输出结果：
对于输入 `"2+3*5/(1-9)+7"`，程序将输出：
```
中缀表达式: 2+3*5/(1-9)+7
后缀表达式: 2 3 5 * 1 9 - / + 7 +
```

你可以根据需要扩展此程序，例如支持多位数字、负数或更复杂的表达式。