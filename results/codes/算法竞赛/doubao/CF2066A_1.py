import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        x = list(map(int, sys.stdin.readline().split()))
        i, j = 1, 2  # Choosing two distinct nodes, 1-based indexing
        
        # Query (i, j)
        print(f'? {i} {j}')
        sys.stdout.flush()
        res1 = int(sys.stdin.readline())
        if res1 == -1:
            return
        
        # Query (j, i)
        print(f'? {j} {i}')
        sys.stdout.flush()
        res2 = int(sys.stdin.readline())
        if res2 == -1:
            return
        
        if res1 != res2:
            print('! A')
        else:
            print('! B')
        sys.stdout.flush()

if __name__ == "__main__":
    main()