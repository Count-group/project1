#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> P1(n), P2(n);
    for (int i = 0; i < n; ++i) {
        cin >> P1[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> P2[i];
    }
    
    vector<int> pos(n + 1);
    for (int i = 0; i < n; ++i) {
        pos[P1[i]] = i;
    }
    
    vector<int> B;
    for (int x : P2) {
        B.push_back(pos[x]);
    }
    
    vector<int> d;
    for (int x : B) {
        auto it = lower_bound(d.begin(), d.end(), x);
        if (it == d.end()) {
            d.push_back(x);
        } else {
            *it = x;
        }
    }
    
    cout << d.size() << endl;
    
    return 0;
}