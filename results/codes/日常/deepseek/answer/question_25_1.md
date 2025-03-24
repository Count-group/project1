以下是Python程序，用于输入日期并输出对应的星期几：

```python
from datetime import datetime

date_str = input("请输入日期（格式：YYYY-MM-DD）：")
try:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekday_num = date_obj.weekday()  # 0表示星期一，6表示星期日
    print(f"{date_str} 是{weekdays[weekday_num]}")
except ValueError:
    print("错误：日期格式不正确，请按照YYYY-MM-DD格式输入。")
```

**程序说明：**
1. 使用`datetime.strptime`将输入的字符串转换为日期对象，支持格式为`YYYY-MM-DD`（例如：2023-10-09）。
2. `weekday()`方法返回0（星期一）到6（星期日）的整数。
3. 通过预设的中文星期列表将数字转换为对应的星期名称。
4. 包含异常处理，确保用户输入格式错误时能友好提示。

**示例输出：**
```
请输入日期（格式：YYYY-MM-DD）：2023-10-09
2023-10-09 是星期一
```