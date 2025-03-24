from collections import defaultdict

def dfs(graph, start, end, path, visited):
    visited[start] = True
    path.append(start)
    if start == end:
        return True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, end, path, visited):
                return True
    path.pop()
    return False

def solve(n, st, en, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    path = []
    if not dfs(graph, st, en, path, visited):
        return -1  # This should not happen since the graph is a tree and st and en are connected
    
    # Create the permutation
    permutation = path + [v for v in range(1, n + 1) if v not in path]
    return permutation

t = int(input())
for _ in range(t):
    n, st, en = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    result = solve(n, st, en, edges)
    if result == -1:
        print(-1)
    else:
        print(' '.join(map(str, result)))