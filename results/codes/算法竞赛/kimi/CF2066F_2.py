def can_transform(a, b):
    # Check if b is a subsequence of a
    iter_a = iter(a)
    if not all(x in iter_a for x in b):
        return False
    return True

def find_operations(a, b):
    operations = []
    i, j = 0, 0
    n, m = len(a), len(b)

    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            # Find a segment in a to replace
            start = i
            while i < n and a[i] != b[j]:
                i += 1
            end = i - 1
            # Replace the segment [start, end] with b[j:j+end-start+1]
            operations.append((start + 1, end + 1, end - start + 1))
            operations.append(b[j:j + end - start + 1])
            j += end - start + 1

    # If there are remaining elements in b, replace the rest of a with them
    if j < m:
        operations.append((i + 1, n, m - j))
        operations.append(b[j:])

    return operations

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        if not can_transform(a, b):
            print(-1)
        else:
            operations = find_operations(a, b)
            print(len(operations) // 2)
            for i in range(0, len(operations), 2):
                print(*operations[i])
                print(*operations[i + 1])

if __name__ == "__main__":
    main()