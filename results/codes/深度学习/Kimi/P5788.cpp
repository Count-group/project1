#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> a(n + 1); // 1-based indexing
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<int> f(n + 1, 0); // Initialize all f values to 0
    stack<int> s;

    for (int i = 1; i <= n; ++i) {
        while (!s.empty() && a[i] > a[s.top()]) {
            int top = s.top();
            s.pop();
            f[top] = i;
        }
        s.push(i);
    }

    for (int i = 1; i <= n; ++i) {
        cout << f[i] << " ";
    }
    cout << endl;

    return 0;
}