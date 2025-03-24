from collections import deque

def solve(n, p_values, edges):
    # Build the tree using an adjacency list
    tree = [[] for _ in range(n + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # Initialize the result array and a queue for BFS
    result = [0] * n
    queue = deque([(1, 0)])  # (current vertex, parent)
    visited = [False] * (n + 1)
    visited[1] = True
    
    # Sort the edges to ensure we process vertices in depth order
    for i in range(1, n + 1):
        tree[i].sort()
    
    # Perform BFS to fill the tree
    for ball in p_values:
        while queue:
            current, parent = queue.popleft()
            if result[current - 1] == 0:  # If the current vertex is not filled
                result[current - 1] = ball
                break
            else:  # If the current vertex is filled, add its children to the queue
                for child in tree[current]:
                    if not visited[child]:
                        visited[child] = True
                        queue.append((child, current))
    
    return result

# Input
n = int(input())
p_values = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Solve and print the result
result = solve(n, p_values, edges)
print(*result)