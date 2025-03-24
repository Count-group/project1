T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    press_count = 0
    for i in range(1, k + 1):
        if k % i == 0:
            divisor_count = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    divisor_count += 1
            if divisor_count % 2 == 1:
                press_count += 1

    if press_count % 2 == 1:
        print("YES")
    else:
        print("NO")