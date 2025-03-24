#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    vector<int> res(n, 0);  // 结果数组，初始化为0
    vector<int> stk;        // 用vector模拟单调栈

    for (int i = 0; i < n; ++i) {
        // 当栈非空且当前元素大于栈顶元素对应的值时
        while (!stk.empty() && a[i] > a[stk.back()]) {
            res[stk.back()] = i + 1;  // 记录下标（转换为1-based）
            stk.pop_back();           // 弹出栈顶
        }
        stk.push_back(i);  // 当前元素索引入栈
    }

    // 输出结果
    for (int i = 0; i < n; ++i) {
        cout << res[i] << (i < n - 1 ? " " : "\n");
    }
    return 0;
}