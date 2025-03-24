import re


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 未找到!")
        return None
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")
        return None


def build_inverted_index(file_paths):
    inverted_index = {}
    for doc_id, file_path in enumerate(file_paths, start=1):
        content = read_file(file_path)
        if content:
            words = re.findall(r'\b\w+\b', content.lower())
            for word in words:
                if word not in inverted_index:
                    inverted_index[word] = set()
                inverted_index[word].add(doc_id)

    # 将集合转换为列表以方便输出
    for word in inverted_index:
        inverted_index[word] = sorted(inverted_index[word])

    return inverted_index


if __name__ == "__main__":
    file_paths = ['article1.txt', 'article2.txt', 'article3.txt']
    inverted_index = build_inverted_index(file_paths)

    for word, doc_ids in sorted(inverted_index.items()):
        print(f"{word}: {doc_ids}")

    