#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int HASH_SIZE = 1000007; // 选择足够大的质数作为哈希表大小
const int SEED = 131;         // BKDR哈希的种子

unsigned long long get_hash(const string &s) {
    unsigned long long h = 0;
    for (char c : s) {
        h = h * SEED + c;
    }
    return h;
}

int main() {
    int N;
    cin >> N;
    vector<vector<string>> hashtable(HASH_SIZE);
    int count = 0;

    for (int i = 0; i < N; ++i) {
        string s;
        cin >> s;
        unsigned long long h = get_hash(s);
        int index = h % HASH_SIZE;

        bool found = false;
        for (const string &t : hashtable[index]) {
            if (t == s) {
                found = true;
                break;
            }
        }
        if (!found) {
            hashtable[index].push_back(s);
            count++;
        }
    }

    cout << count << endl;

    return 0;
}