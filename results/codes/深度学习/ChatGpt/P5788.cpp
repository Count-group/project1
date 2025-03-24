#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    
    // 存储结果 f(i)
    vector<int> f(n, 0);
    // 栈中存储下标（从右向左扫描时保持单调递减的顺序）
    stack<int> s;
    
    // 从后向前遍历
    for (int i = n - 1; i >= 0; i--) {
        // 弹出所有不大于 a[i] 的元素
        while (!s.empty() && a[s.top()] <= a[i]) {
            s.pop();
        }
        // 如果栈不为空，栈顶即为第一个大于 a[i] 的元素的下标
        if (!s.empty()) {
            // 注意：题目要求下标从 1 开始
            f[i] = s.top() + 1;
        } else {
            f[i] = 0;
        }
        // 将当前下标入栈
        s.push(i);
    }
    
    // 输出结果
    for (int i = 0; i < n; i++){
        cout << f[i] << " ";
    }
    cout << endl;
    return 0;
}
