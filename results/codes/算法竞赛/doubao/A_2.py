import sys
from collections import defaultdict
import random


n = int(sys.stdin.readline().strip())
total_nodes = 2**n - 1

# Use a dictionary to count the frequency of LCA results
lca_count = defaultdict(int)
# Make some random queries to find the root
for _ in range(200):
    u = random.randint(1, total_nodes)
    v = random.randint(1, total_nodes)
    while u == v:
        v = random.randint(1, total_nodes)
    print(f"? {u} {v}", flush=True)
    t = int(sys.stdin.readline().strip())
    lca_count[t] += 1

# Find the root node
root = max(lca_count, key=lca_count.get)

# Initialize the parent list
parent = [-1] * (total_nodes + 1)

# Function to find children of a node
def find_children(node):
    children = []
    for other in range(1, total_nodes + 1):
        if other == node or parent[other] != -1:
            continue
        print(f"? {node} {other}", flush=True)
        lca = int(sys.stdin.readline().strip())
        if lca == node:
            parent[other] = node
            children.append(other)
    for child in children:
        find_children(child)


find_children(root)

# Print the result
result_str = " ".join(map(str, parent[1:]))
print(f"! {result_str}", flush=True)