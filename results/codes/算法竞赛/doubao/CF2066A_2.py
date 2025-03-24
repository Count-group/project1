import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        x = list(map(int, sys.stdin.readline().split()))
        # Find two indices i and j (1-based) where x[i-1] != x[j-1]
        i = 1
        j = 2
        while j <= n and x[i-1] == x[j-1]:
            j += 1
        # If all x's are the same (theoretically impossible per problem constraints), default to 1 and 2
        if j > n:
            j = 2
        
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