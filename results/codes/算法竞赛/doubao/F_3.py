k, z = map(int, input().split())
b = list(map(int, input().split()))

# Calculate the total number of non - zero elements
total_non_zero = sum([1 for num in b if num % 2 == 1])

# Determine the parity of the total number of turns
total_turns = total_non_zero
is_alice_last = total_turns % 2 == 1

# Initialize the result
result = 0

# Analyze each power of 2
for i in range(k):
    if b[i] % 2 == 1:
        # If Alice makes the last move, she can ensure that this bit is set in the result
        if is_alice_last:
            result |= (1 << (k - i - 1))
        else:
            # If Bob makes the last move, he can ensure that this bit is not set in the result
            pass

# Convert the result to a binary string of length k
binary_result = bin(result)[2:].zfill(k)
print(binary_result)