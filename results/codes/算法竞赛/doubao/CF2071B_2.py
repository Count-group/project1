def is_perfect_square(num):
    root = int(num**0.5)
    return root * root == num


def find_perfect_permutation(n):
    used = [False] * (n + 1)
    result = []

    def backtrack(current_sum):
        if len(result) == n:
            return True
        for i in range(1, n + 1):
            if not used[i]:
                new_sum = current_sum + i
                if not is_perfect_square(new_sum):
                    used[i] = True
                    result.append(i)
                    if backtrack(new_sum):
                        return True
                    used[i] = False
                    result.pop()
        return False

    if backtrack(0):
        return result
    return [-1]


t = int(input())
for _ in range(t):
    n = int(input())
    permutation = find_perfect_permutation(n)
    print(" ".join(map(str, permutation)))
