import sys
from collections import defaultdict

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n, q = int(input[ptr]), int(input[ptr+1])
    ptr +=2
    a = list(map(int, input[ptr:ptr+n]))
    ptr +=n
    
    freq = defaultdict(int)
    for num in a:
        freq[num] +=1
    
    def solve():
        for val in freq.values():
            if val >=2:
                return True
        return False
    
    res = []
    res.append("Yes" if solve() else "No")
    
    for _ in range(q):
        query = input[ptr]
        x = int(input[ptr+1])
        ptr +=2
        if query == '+':
            freq[x] +=1
        else:
            freq[x] -=1
            if freq[x] ==0:
                del freq[x]
        res.append("Yes" if solve() else "No")
    
    print('\n'.join(res))

if __name__ == "__main__":
    main()