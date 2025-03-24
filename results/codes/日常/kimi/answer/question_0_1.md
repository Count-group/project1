在 Python 中，可以使用 `ast.literal_eval` 方法将这样的字符串安全地转换为列表类型。以下是一个示例程序：

```python
import ast

# 原始字符串
s = "[[498,248,125,36,-76],[332,484,123,28,-81],[338,580,202,48,-79]]"

# 使用 ast.literal_eval 转换为列表
result = ast.literal_eval(s)

# 输出结果
print(result)
print(type(result))
```

### 程序说明：
1. **`ast.literal_eval`** 是一个安全的方法，用于将字符串转换为 Python 的字面量（如列表、字典、元组等）。
2. 输入字符串 `s` 是一个合法的 Python 列表的字符串表示形式。
3. 转换后，`result` 将是一个嵌套的列表。

### 输出结果：
```
[[498, 248, 125, 36, -76], [332, 484, 123, 28, -81], [338, 580, 202, 48, -79]]
<class 'list'>
```

如果你的字符串格式可能不合法，建议添加异常处理：

```python
import ast

s = "[[498,248,125,36,-76],[332,484,123,28,-81],[338,580,202,48,-79]]"

try:
    result = ast.literal_eval(s)
    if isinstance(result, list):
        print("转换成功:", result)
    else:
        print("转换结果不是列表")
except (ValueError, SyntaxError):
    print("字符串格式不合法，无法转换为列表")
```

这样可以避免因非法输入导致程序崩溃。

