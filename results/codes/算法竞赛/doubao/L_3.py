q = int(input())
# Dictionary to store the mapping of rubbish names to their types
rubbish_info = {}

for _ in range(q):
    op = input().split()
    if op[0] == '1':
        # For operation 1, store the rubbish name and its type
        name = op[1]
        type_num = int(op[2])
        if name not in rubbish_info:
            rubbish_info[name] = type_num
    else:
        # For operation 2, find the type based on similarity
        query_name = op[1]
        max_similarity = -1
        min_type = float('inf')
        for stored_name, stored_type in rubbish_info.items():
            similarity = 0
            # Calculate the similarity between the query name and the stored name
            for i in range(min(len(query_name), len(stored_name))):
                if query_name[i] == stored_name[i]:
                    similarity += 1
                else:
                    break
            if similarity > max_similarity:
                max_similarity = similarity
                min_type = stored_type
            elif similarity == max_similarity:
                min_type = min(min_type, stored_type)

        print(min_type)