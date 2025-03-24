t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        res = [2]
        used = {2}
        low = 1
        high = n
        while len(res) < n:
            if high not in used and high != 2:
                res.append(high)
                used.add(high)
                high -= 1
            if len(res) < n and low not in used and low != 2:
                res.append(low)
                used.add(low)
                low += 1
        print(' '.join(map(str, res)))