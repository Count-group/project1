以下是求两个集合对称差的Python程序：

```python
# 获取用户输入的两个集合
a = input("请输入第一个集合的元素，用逗号分隔：")
set_a = set([item.strip() for item in a.split(',') if item.strip()])

b = input("请输入第二个集合的元素，用逗号分隔：")
set_b = set([item.strip() for item in b.split(',') if item.strip()])

# 计算对称差
symmetric_difference = set_a ^ set_b

# 排序结果以便更友好地显示
sorted_result = sorted(symmetric_difference, key=lambda x: x)

# 输出结果
print("对称差的结果为：", sorted_result)
```

### 程序说明：
1. **输入处理**：用户输入用逗号分隔的元素，程序会自动去除每个元素前后的空格，并过滤空元素。
2. **集合操作**：使用 `^` 运算符计算两个集合的对称差，等价于 `set_a.symmetric_difference(set_b)`。
3. **结果排序**：将结果转换为排序后的列表，便于阅读。
4. **输出**：按字母顺序或数字顺序（如果元素为数字字符串）输出对称差结果。

### 示例输入输出：
**输入**：
```
请输入第一个集合的元素，用逗号分隔：1, 2, 3, 4
请输入第二个集合的元素，用逗号分隔：3, 4, 5, 6
```

**输出**：
```
对称差的结果为： ['1', '2', '5', '6']
```

**输入**：
```
请输入第一个集合的元素，用逗号分隔：a, b, c
请输入第二个集合的元素，用逗号分隔：c, d, e
```

**输出**：
```
对称差的结果为： ['a', 'b', 'd', 'e']
```