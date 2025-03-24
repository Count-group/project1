def dfs(v, tree, p_values, a, filled, index):
    if filled[v]:
        return index
    a[v] = p_values[index]
    filled[v] = True
    index += 1
    for u in tree[v]:
        index = dfs(u, tree, p_values, a, filled, index)
    return index

def solve(n, p_values, edges):
    tree = [[] for _ in range(n + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    a = [0] * n
    filled = [False] * (n + 1)
    index = 0
    dfs(1, tree, p_values, a, filled, index)
    return a

# Input
n = int(input())
p_values = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Solve and print the result
result = solve(n, p_values, edges)
print(*result)