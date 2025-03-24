#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

// 字典树节点结构
struct TrieNode {
    TrieNode* children[26]; // 存储子节点
    int type = -1; // 存储当前节点对应的垃圾类型
    TrieNode() {
        for (int i = 0; i < 26; ++i) {
            children[i] = nullptr;
        }
    }
};

// 字典树类
class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // 插入垃圾名称和类型
    void insert(const string& s, int type) {
        TrieNode* node = root;
        for (char c : s) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        // 如果当前节点没有类型，或者新类型更小，更新类型
        if (node->type == -1 || type < node->type) {
            node->type = type;
        }
    }

    // 查询垃圾名称的类型
    int query(const string& s) {
        TrieNode* node = root;
        int maxType = -1;
        for (char c : s) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                break;
            }
            node = node->children[index];
            if (node->type != -1) {
                if (maxType == -1 || node->type < maxType) {
                    maxType = node->type;
                }
            }
        }
        return maxType;
    }

private:
    TrieNode* root; // 字典树根节点
};

int main() {
    int q;
    cin >> q;
    Trie trie;
    unordered_map<string, int> rubbishType;

    while (q--) {
        int op;
        cin >> op;
        if (op == 1) {
            string s;
            int x;
            cin >> s >> x;
            // 更新哈希表中的垃圾名称和类型
            if (rubbishType.find(s) == rubbishType.end() || x < rubbishType[s]) {
                rubbishType[s] = x;
            }
            // 插入到字典树中
            trie.insert(s, x);
        } else if (op == 2) {
            string s;
            cin >> s;
            // 如果哈希表中有该垃圾名称，直接返回类型
            if (rubbishType.find(s) != rubbishType.end()) {
                cout << rubbishType[s] << endl;
            } else {
                // 否则通过字典树查询类型
                cout << trie.query(s) << endl;
            }
        }
    }

    return 0;
}