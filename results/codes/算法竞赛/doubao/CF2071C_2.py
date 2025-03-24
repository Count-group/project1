from collections import deque


def find_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))


def solve():
    t = int(input())
    for _ in range(t):
        n, st, en = map(int, input().split())
        graph = {i: [] for i in range(1, n + 1)}
        for _ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        path = find_path(graph, st, en)
        path_nodes = set(path)
        other_nodes = [i for i in range(1, n + 1) if i not in path_nodes]

        if path:
            result = path[:-1] + other_nodes + [en]
            print(" ".join(map(str, result)))
        else:
            print(-1)


if __name__ == "__main__":
    solve()
