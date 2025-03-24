import sys

def query(u, v):
    print(f"? {u} {v}")
    sys.stdout.flush()
    return int(input())

def solve(n):
    total_nodes = 2**n - 1
    parent = [-1] * total_nodes  # Initialize parent array

    # Step 1: Identify the root node
    root = query(1, 2)
    parent[root - 1] = -1  # Root node's parent is -1

    # Step 2: Identify parents for each node
    for i in range(1, total_nodes + 1):
        if i == root:
            continue  # Skip the root node
        for j in range(1, total_nodes + 1):
            if i == j:
                continue  # Skip the same node
            lca = query(i, j)
            if lca == j:  # If LCA is j, then j is the parent of i
                parent[i - 1] = j
                break

    # Step 3: Output the result
    print("!", *parent)
    sys.stdout.flush()

# Input
n = int(input())
solve(n)