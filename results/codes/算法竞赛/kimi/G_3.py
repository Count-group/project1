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
    
    # Define a fixed size for adjacency list (each building can have at most 10 connections)
    MAX_DEGREE = 10
    
    # Initialize adjacency list with fixed size
    graph = [[0] * MAX_DEGREE for _ in range(n + 1)]
    degree = [0] * (n + 1)  # Track the number of connections for each building
    
    # Build the graph
    for _ in range(m):
        x = int(data[index])
        index += 1
        y = int(data[index])
        index += 1
        
        # Add connection for x
        graph[x][degree[x]] = y
        degree[x] += 1
        
        # Add connection for y
        graph[y][degree[y]] = x
        degree[y] += 1
    
    # Initialize clouds array
    clouds = [0] * (n + 1)
    for i in range(1, n + 1):
        clouds[i] = int(data[index])
        index += 1
    
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
        elif op == 2:
            # Dynamically calculate the total clouds for connected buildings
            total_clouds = 0
            for i in range(degree[x]):
                neighbor = graph[x][i]
                total_clouds += clouds[neighbor]
            results.append(total_clouds)
    
    # Output results
    for result in results:
        print(result)

# Call the solve function
solve()