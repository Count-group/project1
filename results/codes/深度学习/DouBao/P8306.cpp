#include <iostream>
#include <vector>
#include <string>

const int ALPHABET_SIZE = 62; // 大小写字母和数字

// 字典树节点结构体
struct TrieNode {
    TrieNode* children[ALPHABET_SIZE];
    int count;
    bool isEndOfWord;

    TrieNode() : count(0), isEndOfWord(false) {
        for (int i = 0; i < ALPHABET_SIZE; ++i) {
            children[i] = nullptr;
        }
    }
};

// 获取字符对应的索引
int getIndex(char ch) {
    if (ch >= '0' && ch <= '9') return ch - '0';
    if (ch >= 'A' && ch <= 'Z') return ch - 'A' + 10;
    return ch - 'a' + 36;
}

// 插入字符串到字典树
void insert(TrieNode* root, const std::string& key) {
    TrieNode* node = root;
    for (char ch : key) {
        int index = getIndex(ch);
        if (!node->children[index]) {
            node->children[index] = new TrieNode();
        }
        node = node->children[index];
        ++node->count;
    }
    node->isEndOfWord = true;
}

// 查找以给定字符串为前缀的字符串数量
int search(TrieNode* root, const std::string& key) {
    TrieNode* node = root;
    for (char ch : key) {
        int index = getIndex(ch);
        if (!node->children[index]) {
            return 0;
        }
        node = node->children[index];
    }
    return node->count;
}

// 释放字典树的内存
void freeTrie(TrieNode* node) {
    if (!node) return;
    for (int i = 0; i < ALPHABET_SIZE; ++i) {
        if (node->children[i]) {
            freeTrie(node->children[i]);
        }
    }
    delete node;
}

int main() {
    int T;
    std::cin >> T;

    while (T--) {
        int n, q;
        std::cin >> n >> q;

        TrieNode* root = new TrieNode();

        // 插入模式串到字典树
        for (int i = 0; i < n; ++i) {
            std::string pattern;
            std::cin >> pattern;
            insert(root, pattern);
        }

        // 处理询问
        for (int i = 0; i < q; ++i) {
            std::string query;
            std::cin >> query;
            int count = search(root, query);
            std::cout << count << std::endl;
        }

        // 释放字典树内存
        freeTrie(root);
    }

    return 0;
}    