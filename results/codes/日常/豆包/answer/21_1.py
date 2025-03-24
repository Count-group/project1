import re


def calculate_polynomial(poly_str, x):
    # 处理多项式字符串，将其转换为可以使用 eval 计算的形式
    poly_str = poly_str.replace('^', '**')
    # 为 x 的系数添加乘法符号
    poly_str = re.sub(r'(\d)(x)', r'\1*\2', poly_str)

    try:
        # 使用 eval 函数计算多项式的值
        result = eval(poly_str, {'x': x})
        return result
    except SyntaxError:
        print("输入的多项式格式不正确，请检查。")
        return None


if __name__ == "__main__":
    poly_str = input("请输入以 x 为唯一变量的多项式（例如：2x^2 + 3x + 1）：")
    try:
        x = float(input("请输入 x 的值："))
        result = calculate_polynomial(poly_str, x)
        if result is not None:
            print(f"多项式在 x = {x} 处的值为：{result}")
    except ValueError:
        print("输入的 x 值不是有效的数字，请输入一个有效的浮点数。")
    