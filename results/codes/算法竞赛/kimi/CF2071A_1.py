def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        k = int(input())  # Input for each test case
        if k % 3 == 1:
            print("YES")
        else:
            print("NO")

# Example usage:
solve()