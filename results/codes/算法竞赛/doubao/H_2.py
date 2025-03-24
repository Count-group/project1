from collections import defaultdict, deque

# Read the number of vertices
n = int(input())
# Read the permutation of ball values
p = list(map(int, input().split()))

# Build the tree using an adjacency list
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)

# Initialize the array to store the ball in each hole
holes = [0] * (n + 1)

# Function to check if a subtree has an empty hole
def has_empty_hole(node):
    queue = deque([node])
    while queue:
        current = queue.popleft()
        if holes[current] == 0:
            return True
        for child in tree[current]:
            queue.append(child)
    return False

# Place the balls one by one
for ball in p:
    current = 1
    while holes[current] != 0:
        valid_children = []
        for child in tree[current]:
            if has_empty_hole(child):
                valid_children.append(child)
        if valid_children:
            current = min(valid_children)
        else:
            break
    holes[current] = ball

# Print the result, skipping the first index (since we used 1 - based indexing)
print(" ".join(map(str, holes[1:])))
