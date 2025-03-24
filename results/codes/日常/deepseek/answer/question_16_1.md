可以使用Python将字符串中的数字移动到开头，同时保持非数字字符的顺序。以下是实现这一功能的代码：

```python
def move_digits_to_front(s):
    digits = [c for c in s if c.isdigit()]
    non_digits = [c for c in s if not c.isdigit()]
    return ''.join(digits + non_digits)

# 示例测试
print(move_digits_to_front("a1b2c3"))       # 输出: "123abc"
print(move_digits_to_front("test4here5"))   # 输出: "45testhere"
print(move_digits_to_front("abc"))          # 输出: "abc"
print(move_digits_to_front("12345"))        # 输出: "12345"
```

### 方法解析：
1. **分离数字与非数字字符**：
   - 使用列表推导式 `digits = [c for c in s if c.isdigit()]` 提取所有数字字符。
   - 使用 `non_digits = [c for c in s if not c.isdigit()]` 提取所有非数字字符。

2. **合并结果**：
   - 将数字字符列表 `digits` 和非数字字符列表 `non_digits` 合并，并通过 `''.join()` 转换为字符串。

### 特点：
- **时间复杂度**：O(n)，仅需遍历字符串一次。
- **空间复杂度**：O(n)，存储两个列表。
- **稳定性**：保留数字和非数字字符在原字符串中的相对顺序。