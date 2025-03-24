#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<int> P1(n), P2(n);
    for (int i = 0; i < n; i++) {
        cin >> P1[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> P2[i];
    }
    
    // 记录第二个排列中每个数字的位置（下标从0开始）
    vector<int> pos(n + 1);
    for (int i = 0; i < n; i++) {
        pos[P2[i]] = i;
    }
    
    // 将第一个排列中的数字转换为它在第二个排列中的下标
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        arr[i] = pos[P1[i]];
    }
    
    // 求 arr 的最长递增子序列（LIS）长度
    vector<int> lis;
    for (int x : arr) {
        auto it = lower_bound(lis.begin(), lis.end(), x);
        if (it == lis.end()) {
            lis.push_back(x);
        } else {
            *it = x;
        }
    }
    
    cout << lis.size() << "\n";
    return 0;
}
