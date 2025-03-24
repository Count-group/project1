from collections import defaultdict
import sys
input = sys.stdin.read
data = input().split()

def fix_the_tree(n, weights, edges):
    # Create adjacency list for the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # Arrays to store the sum of weights of descendants and the result
    sum_weights = [0] * (n + 1)
    result = [0] * (n + 1)
    
    # DFS function to compute the sum of weights of descendants
    def dfs(node, parent):
        sum_weights[node] = weights[node - 1]
        for neighbor in tree[node]:
            if neighbor != parent:
                sum_weights[node] += dfs(neighbor, node)
        return sum_weights[node]
    
    # DFS function to compute the result for each node
    def dfs_result(node, parent, total_weight):
        if parent == 0:
            # Root node case
            result[node] = total_weight - weights[node - 1]
        else:
            # Calculate the cost of reconnecting the subtrees of the current node
            cost = 0
            for neighbor in tree[node]:
                if neighbor != parent:
                    cost += sum_weights[neighbor]
            result[node] = cost - weights[node - 1]
        
        # Propagate the minimum cost to the parent
        for neighbor in tree[node]:
            if neighbor != parent:
                dfs_result(neighbor, node, total_weight)
    
    # Start DFS from the root node (1)
    dfs(1, 0)
    total_weight = sum(weights)
    dfs_result(1, 0, total_weight)
    
    # Print the results for each node
    return result[1:]

# Read input
n = int(data[0])
weights = list(map(int, data[1:n+1]))
edges = [tuple(map(int, data[i:i+2])) for i in range(n+1, 2*n, 2)]

# Get the results and print them
results = fix_the_tree(n, weights, edges)
print(*results)