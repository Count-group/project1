q = int(input())
rubbish_dict = {}

for _ in range(q):
    parts = input().split()
    if parts[0] == '1':
        name, r_type = parts[1], int(parts[2])
        if name not in rubbish_dict:
            rubbish_dict[name] = r_type
    else:
        query_name = parts[1]
        max_similarity = -1
        result_type = float('inf')
        for stored_name, stored_type in rubbish_dict.items():
            sim = 0
            for i in range(min(len(query_name), len(stored_name))):
                if query_name[i] == stored_name[i]:
                    sim += 1
                else:
                    break
            if sim > max_similarity:
                max_similarity = sim
                result_type = stored_type
            elif sim == max_similarity:
                result_type = min(result_type, stored_type)

        print(result_type)
