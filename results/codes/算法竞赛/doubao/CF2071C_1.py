import sys
from collections import deque

def find_path(tree, st, en):
    visited = {}
    q = deque()
    q.append(st)
    visited[st] = None
    while q:
        u = q.popleft()
        if u == en:
            break
        for v in tree[u]:
            if v not in visited:
                visited[v] = u
                q.append(v)
    # Reconstruct path
    path = []
    current = en
    while current is not None:
        path.append(current)
        current = visited.get(current, None)
    path.reverse()
    return path

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, st, en = map(int, input[ptr:ptr+3])
        ptr +=3
        tree = [[] for _ in range(n+1)]
        for __ in range(n-1):
            u, v = map(int, input[ptr:ptr+2])
            ptr +=2
            tree[u].append(v)
            tree[v].append(u)
        if st == en:
            if n == 1:
                print(1)
            else:
                perm = list(range(1, n+1))
                perm.remove(en)
                perm.append(en)
                print(' '.join(map(str, perm)))
        else:
            path = find_path(tree, st, en)
            path_nodes = path[:-1]  # exclude en
            path_set = set(path)
            other_nodes = []
            for node in range(1, n+1):
                if node not in path_set:
                    other_nodes.append(node)
            perm = path_nodes + other_nodes + [en]
            print(' '.join(map(str, perm)))

if __name__ == "__main__":
    main()