k, z = map(int, input().split())
b = list(map(int, input().split()))

# Determine the parity of the total number of turns
total_turns = sum(b) + z
is_alice_turn = total_turns % 2 == 1

# Initialize the result
result = 0

# Process each power of 2
for i in range(k):
    if b[i] % 2 == 1:
        if is_alice_turn:
            result |= (1 << (k - i - 1))

# Convert result to binary string of length k
binary_result = bin(result)[2:].zfill(k)
print(binary_result)