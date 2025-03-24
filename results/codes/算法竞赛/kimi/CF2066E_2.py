def solve(n, q, a, queries):
    # Dictionary to keep track of the counts of each weight
    weight_counts = {}
    
    # Initialize the weight counts
    for ai in a:
        if ai in weight_counts:
            weight_counts[ai] += 1
        else:
            weight_counts[ai] = 1
    
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
            if x in weight_counts:
                weight_counts[x] += 1
            else:
                weight_counts[x] = 1
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