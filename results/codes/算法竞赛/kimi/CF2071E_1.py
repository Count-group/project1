MOD = 998244353

def mod_inverse(a, m):
    return pow(a, m - 2, m)

def solve():
    n = int(input())
    prob = []
    for _ in range(n):
        p, q = map(int, input().split())
        prob.append((p, q))
    
    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    
    # DFS to calculate the probability of each node becoming a leaf
    def dfs(node, parent):
        p, q = prob[node]
        retain_prob = (q - p) * mod_inverse(q, MOD) % MOD
        delete_prob = p * mod_inverse(q, MOD) % MOD
        
        if len(edges[node]) == 1 and node != 0:
            # It's a leaf if it's not the root and has only one neighbor
            return retain_prob
        
        child_delete_prob = 1
        for child in edges[node]:
            if child == parent:
                continue
            child_delete_prob *= dfs(child, node)
            child_delete_prob %= MOD
        
        return retain_prob * child_delete_prob % MOD
    
    leaf_prob = [0] * n
    leaf_prob[0] = dfs(0, -1)
    
    # Calculate the expected value of pairs of leaves
    expected_value = 0
    for i in range(n):
        for j in range(i + 1, n):
            if leaf_prob[i] and leaf_prob[j]:
                expected_value += leaf_prob[i] * leaf_prob[j] % MOD
                expected_value %= MOD
    
    return expected_value

t = int(input())
for _ in range(t):
    print(solve())