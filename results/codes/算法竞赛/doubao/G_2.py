# Read the number of buildings, streets and days
n, m, q = map(int, input().split())

# Initialize the adjacency list to represent the graph
adj = [[] for _ in range(n + 1)]

# Build the graph
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# Initialize the number of cumulonimbus clouds above each building
clouds = [0] + [int(input()) for _ in range(n)]

# Pre - calculate the sum of clouds for each vertex's neighbors
neighbor_cloud_sums = [0] * (n + 1)
for i in range(1, n + 1):
    for neighbor in adj[i]:
        neighbor_cloud_sums[i] += clouds[neighbor]

# Process the events
for _ in range(q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        x, v = event[1], event[2]
        # Update the cloud count of the current building
        clouds[x] += v
        # Update the neighbor cloud sums for all neighbors of x
        for neighbor in adj[x]:
            neighbor_cloud_sums[neighbor] += v
    else:
        x = event[1]
        print(neighbor_cloud_sums[x])