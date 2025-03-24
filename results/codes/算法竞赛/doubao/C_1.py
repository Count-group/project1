from collections import defaultdict


def dfs(graph, start, visited):
    stack = [start]
    components = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            components.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return components


def calculate_min_cost(graph, weights, broken_vertex):
    new_graph = defaultdict(list)
    for u in graph:
        if u != broken_vertex:
            for v in graph[u]:
                if v != broken_vertex:
                    new_graph[u].append(v)
    visited = set()
    connected_components = []
    for vertex in new_graph:
        if vertex not in visited:
            component = dfs(new_graph, vertex, visited)
            connected_components.append(component)
    num_components = len(connected_components)
    if num_components <= 1:
        return 0
    component_weights = []
    for component in connected_components:
        min_weight = float('inf')
        for vertex in component:
            min_weight = min(min_weight, weights[vertex - 1])
        component_weights.append(min_weight)
    component_weights.sort()
    cost = 0
    for i in range(num_components - 1):
        cost += component_weights[i] + component_weights[i + 1]
    return cost


n = int(input())
weights = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
answers = []
for i in range(1, n + 1):
    answers.append(calculate_min_cost(graph, weights, i))
print(" ".join(map(str, answers)))
