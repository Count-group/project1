def compute_sequence_sum(n, l, r, a):
    # Step 1: Generate the initial sequence
    sequence = a[:]
    
    # Step 2: Extend the sequence to identify the repeating pattern
    while len(sequence) < 2 * n:
        next_term = sum(sequence[:len(sequence) // 2]) % 2
        sequence.append(next_term)
    
    # Step 3: Identify the repeating pattern
    pattern = sequence[:]
    while len(pattern) < 2 * len(pattern):
        next_term = sum(pattern[:len(pattern) // 2]) % 2
        pattern.append(next_term)
    
    # Find the length of the repeating pattern
    for i in range(1, len(pattern)):
        if pattern[:i] == pattern[i:i * 2]:
            pattern_length = i
            break
    
    # Step 4: Calculate the sum of the repeating pattern
    pattern_sum = sum(pattern[:pattern_length])
    
    # Step 5: Calculate the sum of elements in the range [l, r]
    l -= 1
    r -= 1
    complete_cycles = (r - l + 1) // pattern_length
    remaining_terms = (r - l + 1) % pattern_length
    
    # Calculate the sum of the remaining terms
    remaining_sum = sum(pattern[l % pattern_length:(l % pattern_length) + remaining_terms])
    
    # Combine the results
    total_sum = complete_cycles * pattern_sum + remaining_sum
    return total_sum

# Read input
t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(compute_sequence_sum(n, l, r, a))