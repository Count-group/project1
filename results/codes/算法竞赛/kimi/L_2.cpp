#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct TrieNode {
    TrieNode* children[26];
    int type = -1; // Store the type of the rubbish associated with this node
    TrieNode() {
        for (int i = 0; i < 26; ++i) {
            children[i] = nullptr;
        }
    }
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Insert a new rubbish name with its type
    void insert(const string& s, int type) {
        TrieNode* node = root;
        for (char c : s) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
        }
        // Update the type if it's the first time or a smaller type is found
        if (node->type == -1 || type < node->type) {
            node->type = type;
        }
    }

    // Query the type of a rubbish name
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
    TrieNode* root;
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
            // Update the type in the map and the Trie
            if (rubbishType.find(s) == rubbishType.end() || x < rubbishType[s]) {
                rubbishType[s] = x;
                trie.insert(s, x);
            }
        } else if (op == 2) {
            string s;
            cin >> s;
            // Check if the exact name exists in the map
            if (rubbishType.find(s) != rubbishType.end()) {
                cout << rubbishType[s] << endl;
            } else {
                // Otherwise, find the closest match in the Trie
                int type = trie.query(s);
                cout << type << endl;
            }
        }
    }

    return 0;
}