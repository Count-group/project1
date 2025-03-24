q = int(input())
rubbish_dict = {}

for _ in range(q):
    op = input().split()
    if op[0] == '1':
        s, x = op[1], int(op[2])
        if s not in rubbish_dict:
            rubbish_dict[s] = x
    else:
        s = op[1]
        max_similarity = -1
        min_type = float('inf')
        for key, value in rubbish_dict.items():
            similarity = 0
            for i in range(min(len(s), len(key))):
                if s[i] == key[i]:
                    similarity += 1
            if similarity > max_similarity:
                max_similarity = similarity
                min_type = value
            elif similarity == max_similarity:
                min_type = min(min_type, value)
        print(min_type)