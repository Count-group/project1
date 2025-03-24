import sys


def solve():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, l, r = map(int, sys.stdin.readline().strip().split())
        a = list(map(int, sys.stdin.readline().strip().split()))

        # Function to calculate the value at a given position
        def get_value(pos):
            if pos <= n:
                return a[pos - 1]
            stack = []
            while pos > n:
                stack.append(pos)
                pos //= 2
            value = 0
            for i in range(1, pos + 1):
                value ^= a[i - 1]
            while stack:
                cur_pos = stack.pop()
                value ^= value if cur_pos % 2 == 0 else get_value(cur_pos // 2)
            return value

        result = get_value(l)
        print(result)


if __name__ == "__main__":
    solve()
