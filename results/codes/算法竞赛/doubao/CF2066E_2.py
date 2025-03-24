n, q = map(int, input().split())
barrels = list(map(int, input().split()))

# Function to check if we can identify the poisoned barrel
def can_identify(barrels):
    volume_count = {}
    for volume in barrels:
        if volume in volume_count:
            return True
        volume_count[volume] = 1
    return False


# Initial check
results = []
results.append("Yes" if can_identify(barrels) else "No")

# Process queries
for _ in range(q):
    query = input().split()
    if query[0] == '+':
        barrels.append(int(query[1]))
    else:
        barrels.remove(int(query[1]))
    results.append("Yes" if can_identify(barrels) else "No")

# Print the results
for result in results:
    print(result)