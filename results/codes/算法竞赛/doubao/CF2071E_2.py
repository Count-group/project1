MOD = 998244353


def mod_inverse(x):
    return pow(x, MOD - 2, MOD)


t = int(input())
for _ in range(t):
    n = int(input())
    p = []
    q = []
    for i in range(n):
        pi, qi = map(int, input().split())
        p.append(pi)
        q.append(qi)

    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            prob = 1
            for k in range(n):
                deg = len(adj[k])
                if k == i or k == j:
                    # Calculate the probability that k is a leaf
                    if deg == 0:
                        prob *= 0
                    else:
                        leaf_prob = 0
                        for neighbor in adj[k]:
                            term = 1
                            for other_neighbor in adj[k]:
                                if other_neighbor == neighbor:
                                    term *= p[neighbor] * mod_inverse(q[neighbor]) % MOD
                                else:
                                    term *= (q[other_neighbor] - p[other_neighbor]) * mod_inverse(q[other_neighbor]) % MOD
                            leaf_prob = (leaf_prob + term) % MOD
                        prob *= leaf_prob
                else:
                    # Calculate the probability that k is in a valid state (not affecting i and j to be leaves)
                    valid_prob = 1
                    if k in adj[i] or k in adj[j]:
                        for neighbor in adj[k]:
                            if neighbor != i and neighbor != j:
                                valid_prob *= (q[neighbor] - p[neighbor]) * mod_inverse(q[neighbor]) % MOD
                    prob *= valid_prob
            ans = (ans + prob) % MOD

    print(ans)