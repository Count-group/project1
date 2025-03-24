import sys
from collections import defaultdict
import random

def main():
    n = int(sys.stdin.readline())
    total_nodes = 2 ** n - 1
    nodes = list(range(1, total_nodes + 1))
    
    # Step 1: Determine the root by querying random pairs
    count = defaultdict(int)
    for _ in range(200):
        u = random.randint(1, total_nodes)
        v = random.randint(1, total_nodes)
        while u == v:
            v = random.randint(1, total_nodes)
        print(f"? {u} {v}")
        sys.stdout.flush()
        t = int(sys.stdin.readline())
        count[t] += 1
    
    root = max(count, key=lambda k: count[k])
    
    # Step 2: Initialize parent array
    parent = [-1] * (total_nodes + 1)  # 1-based indexing
    
    # Step 3: Recursively determine the tree structure
    def process(current_root):
        children = []
        for u in nodes:
            if u == current_root or parent[u] != -1:
                continue
            print(f"? {u} {current_root}")
            sys.stdout.flush()
            lca = int(sys.stdin.readline())
            if lca == current_root:
                parent[u] = current_root
                children.append(u)
        for child in children:
            process(child)
    
    process(root)
    
    # Prepare the output
    output = []
    for i in range(1, total_nodes + 1):
        output.append(str(parent[i]))
    print("! " + ' '.join(output))
    sys.stdout.flush()

if __name__ == "__main__":
    main()