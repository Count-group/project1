from collections import defaultdict

def solve(n, q, a, queries):
    weights = defaultdict(int)
    for ai in a:
        weights[ai] += 1

    def is_possible():
        return len(weights) > 1

    print("Yes" if is_possible() else "No")

    for query in queries:
        if query[0] == '+':
            x = int(query[1])
            weights[x] += 1
        else:
            x = int(query[1])
            weights[x] -= 1
            if weights[x] == 0:
                del weights[x]
        print("Yes" if is_possible() else "No")

n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = [input().split() for _ in range(q)]
solve(n, q, a, queries)