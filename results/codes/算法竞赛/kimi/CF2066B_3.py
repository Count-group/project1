def max_magical_subsequence(arr):
    n = len(arr)
    mex = 0  # Initialize MEX
    count = 0  # Initialize the count of elements in the magical subsequence
    seen = set()  # Set to keep track of seen elements

    for num in arr:
        if num == mex:
            mex += 1  # Update MEX if the current element is equal to the current MEX
        else:
            seen.add(num)  # Add the current element to the seen set

        # Check if the current element can be included in the subsequence
        while mex in seen:
            mex += 1  # Update MEX if it is in the seen set

        if num >= mex:
            count += 1  # Include the current element in the subsequence

    return count

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_magical_subsequence(arr))