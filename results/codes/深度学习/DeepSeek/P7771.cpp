#include <bits/stdc++.h>
using namespace std;

vector<int> adj[100005];
int in_degree[100005] = {0};
int out_degree[100005] = {0};

bool is_weakly_connected(int n) {
    unordered_set<int> nodes;
    for (int i = 1; i <= n; ++i) {
        if (out_degree[i] > 0 || in_degree[i] > 0) {
            nodes.insert(i);
        }
    }
    if (nodes.empty()) return true;

    unordered_map<int, vector<int>> undir_adj;
    for (int u = 1; u <= n; ++u) {
        for (int v : adj[u]) {
            undir_adj[u].push_back(v);
            undir_adj[v].push_back(u);
        }
    }

    queue<int> q;
    int start = *nodes.begin();
    q.push(start);
    unordered_set<int> visited;
    visited.insert(start);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : undir_adj[u]) {
            if (nodes.count(v) && !visited.count(v)) {
                visited.insert(v);
                q.push(v);
            }
        }
    }

    for (int u : nodes) {
        if (!visited.count(u)) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        out_degree[u]++;
        in_degree[v]++;
    }

    int plus1 = 0, minus1 = 0;
    bool valid = true;
    for (int i = 1; i <= n; ++i) {
        int diff = out_degree[i] - in_degree[i];
        if (diff < -1 || diff > 1) {
            valid = false;
            break;
        }
        if (diff == 1) plus1++;
        else if (diff == -1) minus1++;
    }

    if (!valid || !((plus1 == 0 && minus1 == 0) || (plus1 == 1 && minus1 == 1))) {
        cout << "No\n";
        return 0;
    }

    if (!is_weakly_connected(n)) {
        cout << "No\n";
        return 0;
    }

    int start_node = -1;
    if (plus1 == 1) {
        for (int i = 1; i <= n; ++i) {
            if (out_degree[i] - in_degree[i] == 1) {
                start_node = i;
                break;
            }
        }
    } else {
        start_node = -1;
        for (int i = 1; i <= n; ++i) {
            if (out_degree[i] > 0) {
                if (start_node == -1 || i < start_node) {
                    start_node = i;
                }
            }
        }
        if (start_node == -1) start_node = 1;
    }

    for (int i = 1; i <= n; ++i) {
        sort(adj[i].begin(), adj[i].end(), greater<int>());
    }

    vector<int> path;
    function<void(int)> dfs = [&](int u) {
        while (!adj[u].empty()) {
            int v = adj[u].back();
            adj[u].pop_back();
            dfs(v);
        }
        path.push_back(u);
    };
    dfs(start_node);
    reverse(path.begin(), path.end());

    if (path.size() != m + 1) {
        cout << "No\n";
        return 0;
    }

    for (int i = 0; i < path.size(); ++i) {
        if (i > 0) cout << ' ';
        cout << path[i];
    }
    cout << '\n';

    return 0;
}