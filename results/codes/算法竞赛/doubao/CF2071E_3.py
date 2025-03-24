MOD = 998244353


def mod_inverse(x):
    return pow(x, MOD - 2, MOD)


t = int(input())
for _ in range(t):
    n = int(input())
    p = []
    q = []
    for _ in range(n):
        pi, qi = map(int, input().split())
        p.append(pi)
        q.append(qi)

    edges = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Probability that vertex i is a leaf
            prob_i_leaf = 0
            if len(edges[i]) > 0:
                for neighbor_i in edges[i]:
                    term = 1
                    for other_neighbor_i in edges[i]:
                        if other_neighbor_i == neighbor_i:
                            term = term * p[neighbor_i] * mod_inverse(q[neighbor_i]) % MOD
                        else:
                            term = term * (q[other_neighbor_i] - p[other_neighbor_i]) * mod_inverse(q[other_neighbor_i]) % MOD
                    term = term * p[i] * mod_inverse(q[i]) % MOD
                    prob_i_leaf = (prob_i_leaf + term) % MOD

            # Probability that vertex j is a leaf
            prob_j_leaf = 0
            if len(edges[j]) > 0:
                for neighbor_j in edges[j]:
                    term = 1
                    for other_neighbor_j in edges[j]:
                        if other_neighbor_j == neighbor_j:
                            term = term * p[neighbor_j] * mod_inverse(q[neighbor_j]) % MOD
                        else:
                            term = term * (q[other_neighbor_j] - p[other_neighbor_j]) * mod_inverse(q[other_neighbor_j]) % MOD
                    term = term * p[j] * mod_inverse(q[j]) % MOD
                    prob_j_leaf = (prob_j_leaf + term) % MOD

            # Probability that both i and j are independent in terms of leaf - becoming
            prob_both_leaf = prob_i_leaf * prob_j_leaf % MOD

            # Exclude the case where the connection between i and j affects the leaf - status
            if j in edges[i]:
                # Adjust the probability
                # If i and j are adjacent, we need to subtract the double - counted cases
                prob_i_leaf_only = 0
                for neighbor_i in edges[i]:
                    if neighbor_i != j:
                        term = 1
                        for other_neighbor_i in edges[i]:
                            if other_neighbor_i == neighbor_i:
                                term = term * p[neighbor_i] * mod_inverse(q[neighbor_i]) % MOD
                            else:
                                term = term * (q[other_neighbor_i] - p[other_neighbor_i]) * mod_inverse(q[other_neighbor_i]) % MOD
                        term = term * p[i] * mod_inverse(q[i]) % MOD
                        prob_i_leaf_only = (prob_i_leaf_only + term) % MOD

                prob_j_leaf_only = 0
                for neighbor_j in edges[j]:
                    if neighbor_j != i:
                        term = 1
                        for other_neighbor_j in edges[j]:
                            if other_neighbor_j == neighbor_j:
                                term = term * p[neighbor_j] * mod_inverse(q[neighbor_j]) % MOD
                            else:
                                term = term * (q[other_neighbor_j] - p[other_neighbor_j]) * mod_inverse(q[other_neighbor_j]) % MOD
                        term = term * p[j] * mod_inverse(q[j]) % MOD
                        prob_j_leaf_only = (prob_j_leaf_only + term) % MOD

                prob_both_leaf = (prob_both_leaf - prob_i_leaf_only * prob_j_leaf_only % MOD + MOD) % MOD

            result = (result + prob_both_leaf) % MOD

    print(result)
