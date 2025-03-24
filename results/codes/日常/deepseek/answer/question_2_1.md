以下是一个Python程序，用于读取三篇英语文章并生成所有英文单词的倒排表：

```python
import re
from collections import defaultdict

def build_inverted_index(filenames):
    inverted_index = defaultdict(set)
    
    for doc_id, filename in enumerate(filenames, 1):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                words = re.findall(r'\b[a-z]+\b', text)
                unique_words = set(words)
                
                for word in unique_words:
                    inverted_index[word].add(doc_id)
        except FileNotFoundError:
            print(f"警告：文件 {filename} 未找到，已跳过")
            continue
    
    # 将集合转换为排序列表
    for word in inverted_index:
        inverted_index[word] = sorted(inverted_index[word])
    
    return inverted_index

def print_inverted_index(inverted_index):
    for word in sorted(inverted_index.keys()):
        docs = ', '.join(map(str, inverted_index[word]))
        print(f"{word:<15} -> 出现在文章 {docs}")

if __name__ == "__main__":
    files = ['article1.txt', 'article2.txt', 'article3.txt']  # 替换为实际文件名
    index = build_inverted_index(files)
    print_inverted_index(index)
```

### 功能说明：
1. **读取文件**：程序会依次读取指定的三个文本文件（默认名为article1.txt, article2.txt, article3.txt）
2. **文本处理**：
   - 将文本转换为小写
   - 使用正则表达式提取纯字母单词（过滤数字和特殊符号）
   - 对每个文档中的单词进行去重
3. **构建倒排表**：
   - 使用`defaultdict`存储倒排索引
   - 键为单词，值为包含该单词的文档ID集合
4. **输出结果**：按字母顺序排列单词，并显示每个单词出现的文档列表

### 使用说明：
1. 将三篇英文文章保存为article1.txt、article2.txt和article3.txt
2. 将上述代码保存为`inverted_index.py`
3. 运行程序：`python inverted_index.py`

### 示例输出：
```
about           -> 出现在文章 1, 3
analysis       -> 出现在文章 2
computer       -> 出现在文章 1, 2
data           -> 出现在文章 1, 2, 3
...
```

### 注意事项：
1. 程序会自动跳过不存在的文件并给出警告
2. 单词匹配规则为纯字母字符（a-z），忽略带数字或特殊符号的"单词"
3. 文档ID按输入顺序从1开始编号
4. 支持UTF-8编码文件，确保文本文件保存为UTF-8格式

如果需要处理更复杂的单词形式（如包含连字符的单词），可以修改正则表达式为`r'\b[a-z]+(?:-[a-z]+)*\b'`。