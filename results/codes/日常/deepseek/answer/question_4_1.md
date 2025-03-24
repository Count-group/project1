要实现将字符串中的大写字母转为小写，小写字母转为大写的功能，可以使用以下两种方法：

### 方法一：使用内置的 `swapcase()` 方法
Python 字符串自带的 `swapcase()` 方法可以直接实现该功能，代码简洁高效：
```python
s = input()
print(s.swapcase())
```

### 方法二：手动转换每个字符
通过遍历字符串中的每个字符，分别处理大小写转换：
```python
s = input()
result = ''.join([c.upper() if c.islower() else c.lower() for c in s])
print(result)
```
**解释：**
- 使用列表推导式遍历每个字符 `c`。
- 若 `c` 是小写字母，转换为大写（`c.upper()`）。
- 否则转换为小写（`c.lower()`），这包括大写字母和非字母字符（非字母字符转换后不变）。

这两种方法均可实现需求，推荐使用内置方法 `swapcase()` 以获得最佳性能。若需了解底层逻辑，可参考手动实现的方式。