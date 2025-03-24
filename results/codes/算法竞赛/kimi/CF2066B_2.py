def max_magical_subsequence(arr):
    n = len(arr)
    arr.sort()  # Sort the array to help with the magical condition
    mex = 0  # Initialize MEX
    count = 0  # Initialize the count of elements in the magical subsequence
    min_val = float('inf')  # Initialize the minimum value to a large number

    for i in range(n):
        if arr[i] == mex:
            mex += 1  # Update MEX if the current element is equal to the current MEX
        else:
            min_val = min(min_val, arr[i])  # Update the minimum value
            if min_val >= mex:
                count += 1  # Include the current element in the subsequence
                min_val = arr[i]  # Update the minimum value to the current element

    return count

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_magical_subsequence(arr))