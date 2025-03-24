MOD = 10**9 + 7


def is_valid_fill(n, c, sequence, fills):
    current_sequence = []
    fill_index = 0
    for num in sequence:
        if num == 0:
            current_sequence.append(fills[fill_index])
            fill_index += 1
        else:
            current_sequence.append(num)
    for i in range(1, n + 1):
        count = 0
        for j, floor in enumerate(current_sequence):
            if floor <= i:
                count += 1
                if count >= c:
                    break
        else:
            return False
    return True


def dfs(n, c, sequence, index, fills, memo):
    if index == len(sequence):
        return 1 if is_valid_fill(n, c, sequence, fills) else 0
    if sequence[index] != 0:
        return dfs(n, c, sequence, index + 1, fills, memo)
    state = tuple(fills + [index])
    if state in memo:
        return memo[state]
    total = 0
    for floor in range(1, n + 1):
        new_fills = fills + [floor]
        total = (total + dfs(n, c, sequence, index + 1, new_fills, memo)) % MOD
    memo[state] = total
    return total


def solve():
    t = int(input())
    for _ in range(t):
        n, c, m = map(int, input().split())
        sequence = list(map(int, input().split()))
        memo = {}
        result = dfs(n, c, sequence, 0, [], memo)
        print(result)


if __name__ == "__main__":
    solve()
    