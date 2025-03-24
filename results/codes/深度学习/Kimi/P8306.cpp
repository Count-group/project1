#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int CHAR_SIZE = 62; // 大小写字母和数字的总数

// 字符到索引的映射函数
int charToIndex(char c) {
    if (c >= 'a' && c <= 'z') return c - 'a';
    if (c >= 'A' && c <= 'Z') return 26 + c - 'A';
    if (c >= '0' && c <= '9') return 52 + c - '0';
    return -1; // 不合法字符
}

struct TrieNode {
    vector<TrieNode*> children;
    int count;
    TrieNode() : count(0), children(CHAR_SIZE, nullptr) {}
};

void deleteTrie(TrieNode* root) {
    if (!root) return;
    for (int i = 0; i < CHAR_SIZE; ++i) {
        if (root->children[i]) {
            deleteTrie(root->children[i]);
        }
    }
    delete root;
}

void insert(TrieNode* root, const string& s) {
    TrieNode* node = root;
    for (char c : s) {
        int idx = charToIndex(c);
        if (!node->children[idx]) {
            node->children[idx] = new TrieNode();
        }
        node = node->children[idx];
        node->count++;
    }
}

int query(TrieNode* root, const string& s) {
    TrieNode* node = root;
    for (char c : s) {
        int idx = charToIndex(c);
        if (!node->children[idx]) {
            return 0;
        }
        node = node->children[idx];
    }
    return node->count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, q;
        cin >> n >> q;
        TrieNode* root = new TrieNode();
        for (int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            insert(root, s);
        }
        for (int i = 0; i < q; ++i) {
            string t;
            cin >> t;
            cout << query(root, t) << '\n';
        }
        deleteTrie(root);
    }
    return 0;
}