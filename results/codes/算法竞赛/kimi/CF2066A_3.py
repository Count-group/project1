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
    
    # Query 2: Check distance between vertices 1 and 3
    res2 = query(1, 3)
    
    if res2 == 0:
        print("! A")
        return
    
    # If both queries return positive values, analyze them
    if res1 > 0 and res2 > 0:
        # In Object B (points), the Manhattan distance is typically small (1 or 2)
        # In Object A (graph), the shortest path can be larger (e.g., 3 or more)
        if res1 > 2 or res2 > 2:
            print("! A")
        else:
            # Check if the distances are consistent with Manhattan distance
            # For points, the maximum possible distance is 2n (since x_i, y_i <= n)
            # For a graph with n vertices, a path length of 3 or more is possible
            if res1 == 1 and res2 == 1:
                # If both distances are 1, it could be either Object A or Object B
                # We need an additional check to be sure
                # Query 3: Check distance between vertices 2 and 3
                res3 = query(2, 3)
                if res3 == 0:
                    print("! A")
                elif res3 == 2:
                    print("! B")
                else:
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