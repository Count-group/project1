t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 0
    length = 0
    for num in a:
        if num >= mex:
            length += 1
            mex += 1

    print(length)