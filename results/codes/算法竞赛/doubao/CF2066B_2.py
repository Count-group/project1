def find_max_magical_subsequence_length(arr):
    n = len(arr)
    max_length = 0
    from itertools import combinations
    for r in range(n, 0, -1):
        for subseq in combinations(arr, r):
            is_magical = True
            for i in range(len(subseq) - 1):
                left_min = min(subseq[:i + 1])
                right_nums = subseq[i + 1:]
                mex = 0
                while mex in right_nums:
                    mex += 1
                if left_min < mex:
                    is_magical = False
                    break
            if is_magical:
                return r
    return 1


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_max_magical_subsequence_length(arr))