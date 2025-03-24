以下是一个Python程序，它读取三篇英语文章并生成所有英文单词的倒排表：

```python
import os
import re
from collections import defaultdict

def read_article(file_path):
    """读取文章内容，返回文章中的单词列表"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 使用正则表达式提取所有英文单词，并转换为小写
        words = re.findall(r'[a-zA-Z]+', content)
        words = [word.lower() for word in words]
        return words

def build_inverted_index(article_files):
    """构建倒排表"""
    inverted_index = defaultdict(dict)
    for idx, file_path in enumerate(article_files, 1):
        words = read_article(file_path)
        word_count = defaultdict(int)
        word_positions = defaultdict(list)
        for position, word in enumerate(words):
            word_count[word] += 1
            word_positions[word].append(position + 1)  # 位置从1开始计数
        # 将单词及其出现信息添加到倒排表中
        for word in word_count:
            inverted_index[word][idx] = {
                'count': word_count[word],
                'positions': word_positions[word]
            }
    return inverted_index

def print_inverted_index(inverted_index):
    """打印倒排表"""
    for word in sorted(inverted_index):
        print(f"'{word}':", end=' ')
        articles_info = []
        for article_id in sorted(inverted_index[word]):
            count = inverted_index[word][article_id]['count']
            positions = inverted_index[word][article_id]['positions']
            articles_info.append(f"文档{article_id} (出现次数: {count}, 位置: {positions})")
        print(', '.join(articles_info))

if __name__ == "__main__":
    # 假设三篇英语文章的文件路径如下
    article_files = [
        'article1.txt',
        'article2.txt',
        'article3.txt'
    ]
    
    # 检查文件是否存在
    for file in article_files:
        if not os.path.exists(file):
            print(f"错误：文件 '{file}' 不存在")
            exit(1)
    
    # 构建倒排表
    inverted_index = build_inverted_index(article_files)
    
    # 打印倒排表
    print("倒排表如下：")
    print_inverted_index(inverted_index)
```

### 程序说明：
1. **`read_article` 函数**：
   - 读取指定路径的文章文件。
   - 使用正则表达式提取所有英文单词，并将它们转换为小写，以便不区分大小写地处理单词。

2. **`build_inverted_index` 函数**：
   - 遍历每篇文章，统计每个单词的出现次数和位置。
   - 构建一个倒排表，其中每个单词对应一个字典，记录该单词在哪些文章中出现，以及每篇文章中的出现次数和位置。

3. **`print_inverted_index` 函数**：
   - 按字母顺序打印倒排表，显示每个单词在哪些文章中出现，以及对应的出现次数和位置。

4. **主程序部分**：
   - 指定三篇英语文章的文件路径。
   - 检查文件是否存在，若不存在则提示错误并退出。
   - 调用函数构建倒排表并打印结果。

### 使用方法：
1. 将三篇英语文章分别保存为 `article1.txt`、`article2.txt` 和 `article3.txt`。
2. 确保这些文件与程序在同一目录下，或者修改程序中的文件路径为实际路径。
3. 运行程序，程序将输出所有英文单词的倒排表。

### 示例输出：
假设三篇文章内容如下：
- `article1.txt`: "Hello world. Python is fun."
- `article2.txt`: "Python is powerful. Hello AI."
- `article3.txt`: "AI is changing the world."

程序输出的倒排表可能如下：
```
倒排表如下：
'ai': 文档2 (出现次数: 1, 位置: [5]), 文档3 (出现次数: 1, 位置: [3])
'changing': 文档3 (出现次数: 1, 位置: [4])
'fun': 文档1 (出现次数: 1, 位置: [5])
'hello': 文档1 (出现次数: 1, 位置: [1]), 文档2 (出现次数: 1, 位置: [1])
'is': 文档1 (出现次数: 1, 位置: [4]), 文档2 (出现次数: 1, 位置: [3]), 文档3 (出现次数: 1, 位置: [2])
'powerful': 文档2 (出现次数: 1, 位置: [4])
'python': 文档1 (出现次数: 1, 位置: [3]), 文档2 (出现次数: 1, 位置: [2])
'the': 文档3 (出现次数: 1, 位置: [5])
'world': 文档1 (出现次数: 1, 位置: [2]), 文档3 (出现次数: 1, 位置: [6])
```