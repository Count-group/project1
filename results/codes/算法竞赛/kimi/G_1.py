def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    q = int(data[index])
    index += 1
    
    # Build the graph using adjacency list
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x = int(data[index])
        index += 1
        y = int(data[index])
        index += 1
        graph[x].append(y)
        graph[y].append(x)
    
    # Initialize clouds array
    clouds = [0] * (n + 1)
    for i in range(1, n + 1):
        clouds[i] = int(data[index])
        index += 1
    
    # Initialize connected_clouds array
    connected_clouds = [0] * (n + 1)
    for i in range(1, n + 1):
        for neighbor in graph[i]:
            connected_clouds[i] += clouds[neighbor]
    
    # Process queries
    results = []
    for _ in range(q):
        op = int(data[index])
        index += 1
        x = int(data[index])
        index += 1
        
        if op == 1:
            v = int(data[index])
            index += 1
            clouds[x] += v
            for neighbor in graph[x]:
                connected_clouds[neighbor] += v
        elif op == 2:
            results.append(connected_clouds[x])
    
    # Output results
    for result in results:
        print(result)

# Call the solve function
solve()