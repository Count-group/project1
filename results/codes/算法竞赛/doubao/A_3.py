import sys
import random

# Read the number of levels of the full binary tree
n = int(sys.stdin.readline().strip())
# Calculate the total number of nodes in the full binary tree
total_nodes = 2 ** n - 1

# Function to make a query and get the lowest common ancestor
def query(u, v):
    print(f"? {u} {v}", flush=True)
    return int(sys.stdin.readline().strip())

# Try to find the root by making multiple queries
lca_counts = {}
for _ in range(200):
    u = random.randint(1, total_nodes)
    v = random.randint(1, total_nodes)
    while u == v:
        v = random.randint(1, total_nodes)
    lca = query(u, v)
    if lca not in lca_counts:
        lca_counts[lca] = 0
    lca_counts[lca] += 1

# Determine the root node as the one with the highest LCA count
root = max(lca_counts, key=lca_counts.get)

# Initialize a list to store the parent of each node
parents = [-1] * (total_nodes + 1)

# Function to recursively find the children of a node and build the tree structure
def find_children(parent_node):
    for node in range(1, total_nodes + 1):
        if parents[node] != -1 or node == parent_node:
            continue
        lca = query(parent_node, node)
        if lca == parent_node:
            parents[node] = parent_node
            find_children(node)

# Start building the tree from the root
find_children(root)

# Generate the output string
output = "! " + " ".join(map(str, parents[1:]))
print(output, flush=True)