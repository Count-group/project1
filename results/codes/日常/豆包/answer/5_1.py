from datetime import datetime

date_string = "2025-1-1 8:00:00 AM"
# 定义日期时间格式
format_string = "%Y-%m-%d %I:%M:%S %p"

try:
    # 将字符串转换为 datetime 对象
    date_object = datetime.strptime(date_string, format_string)
    print("转换后的时间对象:", date_object)
except ValueError:
    print("输入的字符串格式与指定的格式不匹配。")
    