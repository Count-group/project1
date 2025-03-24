def dfs(v, p, tree, p_values, a, filled):
    if not filled[v-1]:
        a[v-1] = p_values[0]
        filled[v-1] = True
        p_values.pop(0)
    for u in tree[v]:
        if u != p:
            dfs(u, v, tree, p_values, a, filled)

def solve(n, p_values, edges):
    tree = [[] for _ in range(n+1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    a = [0] * n
    filled = [False] * n
    dfs(1, -1, tree, p_values, a, filled)
    return a

n = int(input())
p_values = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
print(*solve(n, p_values, edges))