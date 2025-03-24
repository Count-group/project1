def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


num1 = 12
num2 = 18
result = lcm(num1, num2)
print(f"{num1} 和 {num2} 的最小公倍数是 {result}")
    