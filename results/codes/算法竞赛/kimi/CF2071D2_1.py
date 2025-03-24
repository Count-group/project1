def compute_sequence_sum(n, l, r, a):
    # Step 1: Identify the repeating pattern
    pattern = a[:]
    while len(pattern) < 2 * n:
        next_term = sum(pattern[:len(pattern) // 2]) % 2
        pattern.append(next_term)
    
    # Step 2: Calculate the sum of the repeating pattern
    pattern_sum = sum(pattern)
    pattern_length = len(pattern)
    
    # Step 3: Determine the number of complete cycles in the range [l, r]
    l -= 1
    r -= 1
    complete_cycles = (r - l + 1) // pattern_length
    remaining_terms = (r - l + 1) % pattern_length
    
    # Step 4: Calculate the sum of the remaining terms
    remaining_sum = sum(pattern[:remaining_terms])
    
    # Step 5: Combine the results
    total_sum = complete_cycles * pattern_sum + remaining_sum
    return total_sum

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(compute_sequence_sum(n, l, r, a))