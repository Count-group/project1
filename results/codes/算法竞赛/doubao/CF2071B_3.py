def is_perfect_square(num):
    root = int(num**0.5)
    return root * root == num


def find_perfect_permutation(n):
    if n == 1:
        return [-1]
    permutation = []
    available = set(range(1, n + 1))
    start = n
    permutation.append(start)
    available.remove(start)
    current_sum = start
    while available:
        found = False
        for num in sorted(available, reverse=True):
            new_sum = current_sum + num
            if not is_perfect_square(new_sum):
                permutation.append(num)
                available.remove(num)
                current_sum = new_sum
                found = True
                break
        if not found:
            return [-1]
    return permutation


t = int(input())
for _ in range(t):
    n = int(input())
    result = find_perfect_permutation(n)
    print(" ".join(map(str, result)))

    