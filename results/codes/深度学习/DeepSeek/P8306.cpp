#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    int cnt;
    TrieNode() : cnt(0) {}
};

void insert(TrieNode* root, const string &s) {
    TrieNode* node = root;
    for (char c : s) {
        if (node->children.find(c) == node->children.end()) {
            node->children[c] = new TrieNode();
        }
        node = node->children[c];
        node->cnt++;
    }
}

int query(TrieNode* root, const string &s, int total) {
    if (s.empty()) {
        return total;
    }
    TrieNode* node = root;
    for (char c : s) {
        auto it = node->children.find(c);
        if (it == node->children.end()) {
            return 0;
        }
        node = it->second;
    }
    return node->cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin>>T;
    while(T>0){
        T--;
        int n, q;
        cin >> n >> q;
        cin.ignore(); // 忽略换行符
        
        TrieNode* root = new TrieNode();
        for (int i = 0; i < n; ++i) {
            string s;
            getline(cin, s);
            insert(root, s);
        }
        
        while (q--) {
            string t;
            getline(cin, t);
            cout << query(root, t, n) << '\n';
        }
    }
    
    return 0;
}