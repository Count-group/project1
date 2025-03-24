from collections import defaultdict

n = int(input())
p = list(map(int, input().split()))
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)

holes = [0] * n
for ball in p:
    current_vertex = 1
    while holes[current_vertex - 1] != 0:
        for son in tree[current_vertex]:
            def has_empty_subtree(node):
                stack = [node]
                while stack:
                    cur = stack.pop()
                    if holes[cur - 1] == 0:
                        return True
                    stack.extend(tree[cur])
                return False

            if has_empty_subtree(son):
                current_vertex = son
                break

    holes[current_vertex - 1] = ball

print(" ".join(map(str, holes)))