import sys
MOD = 998244353

def modinv(a):
    return pow(a, MOD-2, MOD)

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr +=1
    for _ in range(t):
        n = int(input[ptr])
        ptr +=1
        p = []
        q = []
        for __ in range(n):
            pi = int(input[ptr])
            qi = int(input[ptr+1])
            ptr +=2
            p.append(pi)
            q.append(qi)
        edges = [[] for _ in range(n)]
        for __ in range(n-1):
            u = int(input[ptr])-1
            v = int(input[ptr+1])-1
            ptr +=2
            edges[u].append(v)
            edges[v].append(u)
        
        # Precompute survival probabilities
        s = []
        for i in range(n):
            pi = p[i]
            qi = q[i]
            s.append(pi * modinv(qi) % MOD)
        
        # Precompute for each node the probability that exactly one neighbor survives
        leaf_prob = [0]*n
        for u in range(n):
            deg = len(edges[u])
            if deg == 0:
                leaf_prob[u] = 0
                continue
            total = 0
            for v in edges[u]:
                term = s[v]
                for w in edges[u]:
                    if w != v:
                        term = term * (1 - s[w]) % MOD
                total = (total + term) % MOD
            leaf_prob[u] = s[u] * total % MOD
        
        # Compute the sum over all pairs
        res = 0
        for u in range(n):
            for v in range(u+1, n):
                # Probability that both u and v are leaves
                # This is O(n^2), which is not feasible for n=1e5
                # This code is for demonstration only and will not pass large test cases
                prob = leaf_prob[u] * leaf_prob[v] % MOD
                res = (res + prob) % MOD
        print(res % MOD)

if __name__ == '__main__':
    main()