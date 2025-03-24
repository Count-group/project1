MOD = 10**9 + 7


def is_valid(sequence, n, c):
    for i in range(1, n + 1):
        count = 0
        for j in range(len(sequence)):
            if sequence[j] >= i:
                count += 1
        if count < c:
            return False
    return True


def backtrack(index, sequence, n, c, m, valid_sequences):
    if index == m:
        if is_valid(sequence, n, c):
            valid_sequences.append(sequence[:])
        return
    for i in range(1, n + 1):
        sequence[index] = i
        backtrack(index + 1, sequence, n, c, m, valid_sequences)


def solve():
    t = int(input())
    for _ in range(t):
        n, c, m = map(int, input().split())
        a = [0] * m
        valid_sequences = []
        backtrack(0, a, n, c, m, valid_sequences)
        print(len(valid_sequences) % MOD)


if __name__ == "__main__":
    solve()