以下是一个将十六进制输入转换为二进制的Python程序：

```python
import re

hex_input = input("请输入一个十六进制数: ").strip()

# 去除开头的0x或0X前缀
hex_clean = re.sub(r'^0x', '', hex_input, flags=re.IGNORECASE)

# 验证是否为有效十六进制字符
if not re.fullmatch(r'^[0-9a-fA-F]+$', hex_clean):
    print("错误：输入无效，请确保仅包含十六进制字符（0-9, a-f, A-F）。")
else:
    # 计算二进制位数（每个十六进制字符对应4位）
    binary_length = len(hex_clean) * 4
    
    # 转换为十进制再转二进制，并补足前导零
    decimal_value = int(hex_clean, 16)
    binary_str = bin(decimal_value)[2:].zfill(binary_length)
    
    print(f"转换结果: {binary_str}")
```

### 使用说明：
1. 运行程序后输入十六进制数（可带或不带`0x`前缀）。
2. 程序会自动去除前缀并验证输入有效性。
3. 输出为补足前导零的完整二进制字符串，每个十六进制字符对应4位二进制。

### 示例：
输入：
```
1a3F
```
输出：
```
转换结果: 0001101000111111
```

输入：
```
0x00FF
```
输出：
```
转换结果: 0000000011111111
```

### 特点：
- 自动处理大小写和`0x`前缀
- 严格验证输入有效性
- 保持二进制位数与原始十六进制输入的对应关系（每个十六进制字符对应4位二进制）
- 处理前导零保留完整二进制表示