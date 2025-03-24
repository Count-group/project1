from collections import defaultdict, deque


# Function to perform breadth - first search to find connected components
def bfs(graph, start, visited):
    queue = deque([start])
    component = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            component.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return component


# Function to calculate the minimum cost to connect the tree after breaking a vertex
def calculate_min_cost(graph, weights, broken_vertex):
    # Create a new graph without the broken vertex and its edges
    new_graph = defaultdict(list)
    for u in graph:
        if u != broken_vertex:
            for v in graph[u]:
                if v != broken_vertex:
                    new_graph[u].append(v)
    # Find all connected components in the new graph
    visited = set()
    connected_components = []
    for vertex in new_graph:
        if vertex not in visited:
            component = bfs(new_graph, vertex, visited)
            connected_components.append(component)
    num_components = len(connected_components)
    if num_components <= 1:
        return 0
    # Find the minimum weight vertex in each connected component
    component_weights = []
    for component in connected_components:
        min_weight = float('inf')
        for vertex in component:
            min_weight = min(min_weight, weights[vertex - 1])
        component_weights.append(min_weight)
    # Sort the minimum weights of components
    component_weights.sort()
    total_cost = 0
    for i in range(num_components - 1):
        total_cost += component_weights[i]+component_weights[i + 1]
    return total_cost


# Read input
n = int(input())
weights = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Calculate and print the minimum cost for each broken vertex
results = []
for i in range(1, n + 1):
    result = calculate_min_cost(graph, weights, i)
    results.append(result)
print(" ".join(map(str, results)))
