def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        mex = 0
        count = 0
        for num in reversed(a):
            if num >= mex:
                count += 1
                mex += 1
        print(count)

if __name__ == "__main__":
    main()