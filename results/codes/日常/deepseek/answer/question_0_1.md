可以使用Python的`ast`模块中的`literal_eval`方法安全地将字符串转换为列表。以下是实现代码：

```python
import ast

# 原始字符串
s = "[[498,248,125,36,-76],[332,484,123,28,-81],[338,580,202,48,-79]]"

# 转换为列表
result = ast.literal_eval(s)

# 验证结果
print("转换后的类型:", type(result))
print("转换后的内容:", result)
```

**代码说明**：
1. `import ast`：导入安全处理字面量表达的库。
2. `ast.literal_eval(s)`：将字符串安全地转换为对应的Python对象（这里是嵌套列表）。
3. 该方法会检查字符串是否为合法的Python字面量，避免直接使用`eval()`的安全风险。