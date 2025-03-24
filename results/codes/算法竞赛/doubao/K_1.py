MOD = 998244353

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    total = 0
    max_subsets = 2**(n * m) - 1
    for subset in range(1, max_subsets + 1):
        points = []
        for i in range(n * m):
            if (subset >> i) & 1:
                x = i % n + 1
                y = i // n + 1
                points.append((x, y))

        graph = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                    if i not in graph:
                        graph[i] = []
                    if j not in graph:
                        graph[j] = []
                    graph[i].append(j)
                    graph[j].append(i)

        match = [-1] * len(points)
        def find_path(u, visited):
            for v in graph.get(u, []):
                if not visited[v]:
                    visited[v] = True
                    if match[v] == -1 or find_path(match[v], visited):
                        match[v] = u
                        return True
            return False

        max_match = 0
        for i in range(len(points)):
            visited = [False] * len(points)
            if find_path(i, visited):
                max_match += 1
        total = (total + max_match // 2) % MOD

    print(total)