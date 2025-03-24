from collections import defaultdict, deque


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
        graph = defaultdict(list)
        for _ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        path = find_path(graph, st, en)
        if path is None:
            print(-1)
            continue

        path_set = set(path)
        remaining_nodes = [i for i in range(1, n + 1) if i not in path_set]

        permutation = []
        # 先添加路径上除了终点的节点
        for node in path[:-1]:
            permutation.append(node)
        # 添加剩余节点
        permutation.extend(remaining_nodes)
        # 最后添加终点
        permutation.append(en)

        print(" ".join(map(str, permutation)))


if __name__ == "__main__":
    solve()