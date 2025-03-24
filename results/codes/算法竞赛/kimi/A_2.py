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

    # Step 2: Build the tree structure
    def build_tree(node, level):
        if level == n - 1:  # If we are at the last level, no children
            return
        left_child = 2 * node
        right_child = 2 * node + 1
        if left_child <= total_nodes:
            lca = query(node, left_child)
            if lca == node:
                parent[left_child - 1] = node
                build_tree(left_child, level + 1)
        if right_child <= total_nodes:
            lca = query(node, right_child)
            if lca == node:
                parent[right_child - 1] = node
                build_tree(right_child, level + 1)

    build_tree(root, 0)

    # Step 3: Output the result
    print("!", *parent)
    sys.stdout.flush()

# Input
n = int(input())
solve(n)