def hex_to_binary(hex_str):
    try:
        decimal_num = int(hex_str, 16)
        binary_num = bin(decimal_num).replace("0b", "")
        return binary_num
    except ValueError:
        print("输入不是有效的十六进制字符串。")
        return None


hex_input = input("请输入一个十六进制字符串: ")
result = hex_to_binary(hex_input)
if result is not None:
    print(f"对应的二进制表示是: {result}")
    