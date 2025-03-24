def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []

    for char in expression:
        if char.isdigit():
            output.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # 弹出 '('
        else:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence.get(char, 0)):
                output.append(operator_stack.pop())
            operator_stack.append(char)

    while operator_stack:
        output.append(operator_stack.pop())

    return ''.join(output)


expression = "2+3*5/(1-9)+7"
postfix_expression = infix_to_postfix(expression)
print("后缀表达式:", postfix_expression)
    