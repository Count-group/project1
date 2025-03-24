import sys

def query(i, j):
    print(f"? {i} {j}")
    sys.stdout.flush()
    return int(input())

def solve():
    n = int(input())
    x = list(map(int, input().split()))
    
    # Query 1: Check distance between vertices 1 and 2
    res1 = query(1, 2)
    
    if res1 == 0:
        print("! A")
        return
    
    # Query 2: Check distance between vertices 2 and 3
    res2 = query(2, 3)
    
    if res2 == 0:
        print("! A")
        return
    
    # If both queries return positive values, check if they fit Manhattan distance
    if res1 > 0 and res2 > 0:
        # In a graph, the shortest path length can be 1, 2, or more
        # In points, the Manhattan distance is always positive and can be any integer
        # If the values are small (1 or 2), it could be either, but if they are large,
        # it is more likely to be a graph (since points' distances are usually small)
        if res1 > 2 or res2 > 2:
            print("! A")
        else:
            print("! B")
    else:
        print("! A")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()