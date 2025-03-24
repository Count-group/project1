from collections import deque

def find_path(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        vertex, path = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return None

def solve(n, st, en, edges):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    path = find_path(graph, st, en)
    if path is None:
        return -1
    
    permutation = path + [v for v in range(1, n+1) if v not in path]
    return permutation

t = int(input())
for _ in range(t):
    n, st, en = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n-1)]
    result = solve(n, st, en, edges)
    if result == -1:
        print(-1)
    else:
        print(' '.join(map(str, result)))