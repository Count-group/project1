def find_mex(arr):
    mex = 0
    while mex in arr:
        mex += 1
    return mex

def max_magical_subsequence(arr):
    n = len(arr)
    used = set()
    subseq = []
    mex = find_mex(arr)
    
    for i in range(n):
        if arr[i] >= mex and arr[i] not in used:
            subseq.append(arr[i])
            used.add(arr[i])
            mex = find_mex([x for x in arr if x not in used])
    
    return len(subseq)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_magical_subsequence(arr))