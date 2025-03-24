#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

const int MAXN = 1e5 + 5;
vector<int> adj[MAXN];
int in[MAXN], out[MAXN];
stack<int> path;

void dfs(int u) {
    while (!adj[u].empty()) {
        int v = adj[u].back();
        adj[u].pop_back();
        dfs(v);
    }
    path.push(u);
}

int main() {
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        in[v]++;
        out[u]++;
    }

    for (int i = 1; i <= n; i++) {
        sort(adj[i].begin(), adj[i].end(), greater<int>());
    }

    int start = 1, cnt1 = 0, cnt2 = 0;
    for (int i = 1; i <= n; i++) {
        if (out[i] - in[i] == 1) {
            cnt1++;
            start = i;
        } else if (in[i] - out[i] == 1) {
            cnt2++;
        } else if (in[i] != out[i]) {
            cout << "No" << endl;
            return 0;
        }
    }

    if (!(cnt1 == 0 && cnt2 == 0) && !(cnt1 == 1 && cnt2 == 1)) {
        cout << "No" << endl;
        return 0;
    }

    dfs(start);

    if (path.size() != m + 1) {
        cout << "No" << endl;
        return 0;
    }

    while (!path.empty()) {
        cout << path.top();
        path.pop();
        if (!path.empty()) cout << " ";
    }
    cout << endl;

    return 0;
}    