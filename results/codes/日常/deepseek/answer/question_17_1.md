为了实现一个简单的邮箱格式验证程序，我们可以使用正则表达式来匹配常见的邮箱格式。以下是Python程序的实现：

```python
import re

def is_valid_email(email):
    # 定义邮箱格式的正则表达式
    pattern = r'^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email) is not None

# 获取用户输入并去除首尾空格
email = input("请输入邮箱地址：").strip()

# 验证邮箱格式并输出结果
if is_valid_email(email):
    print("邮箱格式正确")
else:
    print("邮箱格式错误")
```

### 实现说明：
1. **正则表达式解析**：
   - **用户名部分** `[a-zA-Z0-9._%+-]+`：允许字母、数字、点、下划线、百分号、加号和减号。
   - **域名部分** `([a-zA-Z0-9-]+\.)+`：允许一个或多个子域名（由字母、数字、连字符组成，后跟点）。
   - **顶级域名** `[a-zA-Z]{2,}$`：要求至少两个字母，且不包含数字或连字符。

2. **验证逻辑**：
   - 使用 `re.fullmatch()` 确保整个字符串完全匹配正则表达式。
   - 用户输入经过 `strip()` 处理，去除可能误输入的首尾空格。

### 示例测试：
- **有效邮箱**：
  - `user@example.com`
  - `user.name@domain.co.uk`
  - `user-name@sub.domain.com`
  
- **无效邮箱**：
  - `user@.com`（缺少子域名）
  - `user@domain..com`（连续点）
  - `user@domain.c`（顶级域名过短）

该程序能够覆盖大多数常见邮箱格式的验证，适用于一般应用场景。