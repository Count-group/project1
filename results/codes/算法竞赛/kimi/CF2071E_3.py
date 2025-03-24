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
    
    # Precompute modular inverses
    inv_q = [mod_inverse(q, MOD) for p, q in prob]
    
    # Arrays to store probabilities
    remain_prob = [0] * n
    leaf_prob = [0] * n
    
    def dfs(node, parent):
        p, q = prob[node]
        remain_prob[node] = (q - p) * inv_q[node] % MOD
        leaf_prob[node] = remain_prob[node]
        
        child_delete_prob = 1
        for child in edges[node]:
            if child == parent:
                continue
            dfs(child, node)
            child_delete_prob *= (1 - leaf_prob[child]) % MOD
            child_delete_prob %= MOD
        
        if node != 0:  # Not the root
            leaf_prob[node] *= child_delete_prob
            leaf_prob[node] %= MOD
    
    dfs(0, -1)
    
    # Calculate expected value of pairs of leaves
    expected_value = 0
    
    def dfs2(node, parent):
        nonlocal expected_value
        for child in edges[node]:
            if child == parent:
                continue
            # Contribution from pairs (node, child)
            expected_value += leaf_prob[node] * leaf_prob[child] % MOD
            expected_value %= MOD
            dfs2(child, node)
    
    dfs2(0, -1)
    
    return expected_value

t = int(input())
for _ in range(t):
    print(solve())