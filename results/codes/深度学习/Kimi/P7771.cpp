#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n + 1);
    vector<int> outd(n + 1, 0), ind(n + 1, 0);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        outd[u]++;
        ind[v]++;
    }

    // 检查是否存在欧拉路径
    int start = -1, end = -1;
    for (int i = 1; i <= n; ++i) {
        if (abs(outd[i] - ind[i]) > 1) {
            cout << "No\n";
            return 0;
        }
        if (outd[i] - ind[i] == 1) {
            if (start != -1) {
                cout << "No\n";
                return 0;
            }
            start = i;
        }
        if (ind[i] - outd[i] == 1) {
            if (end != -1) {
                cout << "No\n";
                return 0;
            }
            end = i;
        }
    }

    // 确定起点
    int s;
    if (start != -1) {
        s = start;
    } else {
        s = -1;
        for (int i = 1; i <= n; ++i) {
            if (outd[i] > 0) {
                s = i;
                break;
            }
        }
        if (s == -1) {
            s = 1;
        }
    }

    // 对邻接表排序
    for (int i = 1; i <= n; ++i) {
        sort(adj[i].begin(), adj[i].end());
    }

    // 使用非递归Hierholzer算法
    vector<int> stack;
    vector<int> ptr(n + 1, 0);
    vector<int> result;

    stack.push_back(s);
    while (!stack.empty()) {
        int u = stack.back();
        if (ptr[u] < adj[u].size()) {
            stack.push_back(adj[u][ptr[u]]);
            ptr[u]++;
        } else {
            result.push_back(u);
            stack.pop_back();
        }
    }

    reverse(result.begin(), result.end());

    if (result.size() != m + 1) {
        cout << "No\n";
    } else {
        for (int x : result) {
            cout << x << " ";
        }
        cout << "\n";
    }

    return 0;
}