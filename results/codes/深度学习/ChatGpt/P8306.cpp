#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    while(T--) {
        int n, q;
        cin >> n >> q;
        vector<string> patterns(n);
        for (int i = 0; i < n; i++){
            cin >> patterns[i];
        }
        sort(patterns.begin(), patterns.end());
        
        for (int i = 0; i < q; i++){
            string query;
            cin >> query;
            // 构造一个严格大于所有以query为前缀的字符串
            string query_next = query;
            query_next.push_back('{');  // '{' ASCII码 123，比 'z' (122) 大
            
            auto lower = lower_bound(patterns.begin(), patterns.end(), query);
            auto upper = lower_bound(patterns.begin(), patterns.end(), query_next);
            cout << (upper - lower) << "\n";
        }
    }
    return 0;
}
