import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, email))


if __name__ == "__main__":
    user_email = input("请输入邮箱地址: ")
    if is_valid_email(user_email):
        print(f"{user_email} 是有效的邮箱地址。")
    else:
        print(f"{user_email} 不是有效的邮箱地址。")
    