为了将中缀表达式转换为后缀表达式，我们可以使用栈来处理运算符的优先级。以下是详细的步骤和实现代码：

### 方法思路
1. **初始化结构**：使用一个栈来暂存运算符，一个列表来保存输出结果。
2. **遍历表达式**：逐个处理字符，区分数字和运算符。
3. **处理数字**：直接加入输出列表。
4. **处理括号**：
   - 左括号直接入栈。
   - 右括号则弹出栈顶元素直到遇到左括号，左括号不输出。
5. **处理运算符**：比较当前运算符与栈顶运算符的优先级，弹出优先级更高或相等的栈顶元素，再将当前运算符入栈。
6. **清理栈**：遍历结束后，将栈中剩余运算符依次弹出。

### 解决代码
```python
def infix_to_postfix(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            output.append(num)
        elif expr[i] in '+-*/()':
            if expr[i] == '(':
                stack.append(expr[i])
            elif expr[i] == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack:
                    stack.pop()  # 弹出左括号但不输出
            else:
                while stack and stack[-1] != '(' and precedence[expr[i]] <= precedence.get(stack[-1], 0):
                    output.append(stack.pop())
                stack.append(expr[i])
            i += 1
        else:
            i += 1  # 跳过非数字和操作符的字符（如空格）
    # 将栈中剩余的操作符弹出
    while stack:
        output.append(stack.pop())
    return ' '.join(output)

# 测试示例
expression = "2+3*5/(1-9)+7"
postfix = infix_to_postfix(expression)
print(postfix)  # 输出：2 3 5 * 1 9 - / + 7 +
```

### 代码解释
1. **优先级字典**：定义了加减乘除的优先级，乘除高于加减。
2. **遍历处理字符**：
   - **数字处理**：连续的数字字符合并为一个数字。
   - **左括号处理**：直接入栈。
   - **右括号处理**：弹出栈顶元素直到左括号，左括号不输出。
   - **运算符处理**：根据优先级弹出栈顶元素，当前运算符入栈。
3. **清理栈**：遍历结束后，弹出栈中所有剩余运算符。

通过这种方法，能够正确将中缀表达式转换为后缀表达式，处理运算符的优先级和括号的嵌套。