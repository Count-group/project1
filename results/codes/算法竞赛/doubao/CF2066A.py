#!/usr/bin/env python3
import sys

# 定义一个函数来处理每个测试用例

def solve():
    # 读取数组长度n
    n = int(input())
    # 读取数组x
    x = list(map(int, input().split()))

    # 第一次查询
    print("? 1 2")
    sys.stdout.flush()
    response1 = int(input())

    # 第二次查询
    print("? 2 3")
    sys.stdout.flush()
    response2 = int(input())

    # 假设一个简单的判断逻辑，实际中需要根据具体的图和点的特性进行判断
    # 这里简单假设如果两次查询结果都小于等于2，认为是对象A，否则是对象B
    if response1 <= 2 and response2 <= 2:
        result = "A"
    else:
        result = "B"

    # 输出结果
    print(f"! {result}")
    sys.stdout.flush()

# 读取测试用例的数量t

t = int(input())
# 循环处理每个测试用例
for _ in range(t):
    solve()