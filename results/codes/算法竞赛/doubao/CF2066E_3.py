# Read the number of barrels (n) and the number of queries (q)
n, q = map(int, input().split())

# Read the initial water volumes of the barrels
barrels = list(map(int, input().split()))

# Function to check if we can identify the poisoned barrel
def can_identify(barrels):
    volume_count = {}
    for volume in barrels:
        if volume in volume_count:
            return True
        volume_count[volume] = 1
    return False


# Check the initial state
results = []
if can_identify(barrels):
    results.append("Yes")
else:
    results.append("No")

# Process each query
for _ in range(q):
    query = input().split()
    if query[0] == '+':
        # Add a new barrel with the given water volume
        new_volume = int(query[1])
        barrels.append(new_volume)
    elif query[0] == '-':
        # Remove a barrel with the given water volume
        remove_volume = int(query[1])
        barrels.remove(remove_volume)

    # Check the state after the query
    if can_identify(barrels):
        results.append("Yes")
    else:
        results.append("No")

# Print the results for each state
for result in results:
    print(result)