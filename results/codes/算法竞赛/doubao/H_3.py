from collections import defaultdict, deque


# Function to check if there is an empty hole in the subtree of a given node
def has_empty_hole(node, filled):
    stack = [node]
    while stack:
        current = stack.pop()
        if not filled[current]:
            return True
        stack.extend(tree[current])
    return False


# Function to find the next available position for a ball
def find_next_position(current, filled):
    valid_children = []
    for child in tree[current]:
        if has_empty_hole(child, filled):
            valid_children.append(child)
    if valid_children:
        return min(valid_children)
    return None


# Read the number of vertices
n = int(input())
# Read the permutation of ball values
p = list(map(int, input().split()))

# Build the tree
tree = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)

# Initialize the array to track filled holes
filled = [False] * (n + 1)
# Initialize the array to store the ball in each hole
result = [0] * (n + 1)

# Place the balls one by one
for ball in p:
    current = 1
    while filled[current]:
        next_pos = find_next_position(current, filled)
        if next_pos is not None:
            current = next_pos
        else:
            break
    filled[current] = True
    result[current] = ball

# Print the result
print(" ".join(map(str, result[1:])))