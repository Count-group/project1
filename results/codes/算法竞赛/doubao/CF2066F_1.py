import sys
from sys import stdin
import math

def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = int(input[ptr]), int(input[ptr+1])
        ptr +=2
        a = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        b = list(map(int, input[ptr:ptr+m]))
        ptr +=m
        
        sum_b = sum(b)
        if n ==0 or m ==0:
            print(-1)
            continue
        max_a = max_subarray_sum(a)
        if sum_b < max_a:
            print(-1)
            continue
        
        operations = []
        # First, replace the entire array a with sum_b
        operations.append((1, n, 1))
        operations.append([sum_b])
        # Then replace the single element with b
        operations.append((1, 1, m))
        operations.append(b)
        
        print(len(operations)//2)
        for i in range(0, len(operations), 2):
            l, r, k = operations[i]
            print(l, r, k)
            print(' '.join(map(str, operations[i+1])) + ' ')
            
solve()