from collections import defaultdict, deque

def find_path(graph, start, end):
    parent = [-1] * (len(graph) + 1)
    queue = deque([start])
    visited = [False] * (len(graph) + 1)
    visited[start] = True

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)

    if parent[end] == -1:
        return None  # Path not found

    path = []
    while end != -1:
        path.append(end)
        end = parent[end]
    path.reverse()
    return path

def solve(n, st, en, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    path = find_path(graph, st, en)
    if path is None:
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