def compute_sequence(n, initial_terms):
    # Precompute the first 2n terms of the sequence
    sequence = initial_terms[:]
    for i in range(n, 2 * n):
        xor_sum = 0
        for j in range((i + 1) // 2):
            xor_sum ^= sequence[j]
        sequence.append(xor_sum)
    return sequence

def sum_of_range(l, r, sequence, period):
    # Compute the sum of elements in the range [l, r]
    sum_period = sum(sequence[:period])
    complete_periods = (r - l + 1) // period
    remaining_terms = (r - l + 1) % period
    sum_remaining = sum(sequence[l % period:l % period + remaining_terms])
    return complete_periods * sum_period + sum_remaining

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        l = int(data[index + 1])
        r = int(data[index + 2])
        index += 3
        initial_terms = list(map(int, data[index:index + n]))
        index += n
        
        # Compute the sequence up to 2n terms
        sequence = compute_sequence(n, initial_terms)
        period = 2 * n
        
        # Compute the sum of the range [l, r]
        result = sum_of_range(l - 1, r - 1, sequence, period)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()