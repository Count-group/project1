MOD = 10**9 + 7

# Function to compute binomial coefficient modulo MOD
def binomial_coefficient(n, k, MOD):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    numerator = 1
    for i in range(k):
        numerator = numerator * (n - i) % MOD
    denominator = 1
    for i in range(1, k + 1):
        denominator = denominator * i % MOD
    return numerator * pow(denominator, MOD - 2, MOD) % MOD

# Function to solve the problem
def count_ways(n, c, m):
    # Calculate the remaining airplanes after ensuring each floor sees at least c airplanes
    remaining_airplanes = m - c * n
    if remaining_airplanes < 0:
        return 0  # Not possible to distribute
    # Calculate the number of ways to distribute the remaining airplanes
    return binomial_coefficient(remaining_airplanes + n - 1, n - 1, MOD)

# Read input
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    c = int(data[index + 1])
    m = int(data[index + 2])
    index += 3
    results.append(count_ways(n, c, m))

# Output results
for result in results:
    print(result)