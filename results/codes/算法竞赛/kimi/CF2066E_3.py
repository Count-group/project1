def solve(n, q, a, queries):
    # Dictionary to keep track of the counts of each weight
    weight_counts = {}
    
    # Initialize the weight counts
    for ai in a:
        weight_counts[ai] = weight_counts.get(ai, 0) + 1
    
    # Function to check if it is possible to identify the poisonous barrel
    def is_possible():
        return len(weight_counts) > 1
    
    # Initial check
    print("Yes" if is_possible() else "No")
    
    # Process each query
    for query in queries:
        op, x = query[0], int(query[1])
        
        if op == '+':
            # Adding a new barrel
            weight_counts[x] = weight_counts.get(x, 0) + 1
        else:
            # Removing a barrel
            if weight_counts[x] == 1:
                del weight_counts[x]
            else:
                weight_counts[x] -= 1
        
        # Check if it is possible to identify the poisonous barrel after the query
        print("Yes" if is_possible() else "No")

# Read input
n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = [input().split() for _ in range(q)]

# Solve the problem
solve(n, q, a, queries)