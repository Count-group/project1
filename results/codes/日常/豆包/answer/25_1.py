import datetime

def get_weekday(date_str):
    try:
        date = datetime.datetime.strptime(date_str, '%Y%m%d')
        weekday = date.strftime('%A')
        return weekday
    except ValueError:
        print("输入的日期格式不正确，请使用 YYYYMMDD 格式。")
        return None

if __name__ == "__main__":
    date_input = input("请输入日期（格式：YYYYMMDD）：")
    result = get_weekday(date_input)
    if result:
        print(f"{date_input} 是 {result}。")
    