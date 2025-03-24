#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int longestCommonSubsequence(int n, const vector<int>& P1, const vector<int>& P2) {
    // 将P2中的值映射到它们的位置
    unordered_map<int, int> posMap;
    for (int i = 0; i < n; ++i) {
        posMap[P2[i]] = i;
    }

    // 将P1中的元素按照P2中的位置重新排列
    vector<int> posInP2;
    for (int i = 0; i < n; ++i) {
        if (posMap.find(P1[i]) != posMap.end()) {
            posInP2.push_back(posMap[P1[i]]);
        }
    }

    // 使用二分查找法求解最长递增子序列的长度
    vector<int> lis;
    for (int pos : posInP2) {
        auto it = lower_bound(lis.begin(), lis.end(), pos);
        if (it == lis.end()) {
            lis.push_back(pos);
        } else {
            *it = pos;
        }
    }

    return lis.size();
}

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

    int result = longestCommonSubsequence(n, P1, P2);
    cout << result << endl;

    return 0;
}