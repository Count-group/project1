import math
a, b = map(int, input().split())
gcd_val = math.gcd(a, b)
result = ((a - 1) * (b - 1)+ gcd_val) // 2
print(result)