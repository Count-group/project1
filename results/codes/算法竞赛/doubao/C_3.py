from collections import defaultdict


# Function to perform DFS to find connected components
def dfs(graph, start, visited):
    stack = [start]
    component = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return component


# Function to calculate the minimum cost to fix the tree after removing a vertex
def calculate_cost(graph, weights, removed_vertex):
    # Create a new graph without the removed vertex
    new_graph = defaultdict(list)
    for u in graph:
        if u != removed_vertex:
            for v in graph[u]:
                if v != removed_vertex:
                    new_graph[u].append(v)

    # Find all connected components
    visited = set()
    components = []
    for node in new_graph:
        if node not in visited:
            component = dfs(new_graph, node, visited)
            components.append(component)

    # If there is only one component, no cost is needed
    if len(components) <= 1:
        return 0

    # Find the minimum weight vertex in each component
    min_weights = []
    for component in components:
        min_weight = float('inf')
        for node in component:
            min_weight = min(min_weight, weights[node - 1])
        min_weights.append(min_weight)

    # Sort the minimum weights
    min_weights.sort()

    total_cost = 0
    for i in range(len(min_weights) - 1):
        total_cost += min_weights[i] + min_weights[i + 1]
        # Update the weights according to the rule (although it doesn't affect the final result of minimum cost calculation here)
        min_weights[i] += 1
        min_weights[i + 1] += 1

    return total_cost


# Read input
n = int(input())
weights = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Calculate and print the result for each vertex
results = []
for i in range(1, n + 1):
    result = calculate_cost(graph, weights, i)
    results.append(result)

print(" ".join(map(str, results)))