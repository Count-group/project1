#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    
    unordered_set<string> uniqueStrings;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        uniqueStrings.insert(s);
    }
    
    cout << uniqueStrings.size() << "\n";
    return 0;
}
