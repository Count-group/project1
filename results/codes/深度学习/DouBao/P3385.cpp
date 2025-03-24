#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// 边的结构体
struct Edge {
    int u, v, w;
};

// 判断是否存在负环
bool hasNegativeCycle(int n, const vector<Edge>& edges) {
    vector<int> dist(n + 1, INT_MAX);
    dist[1] = 0;

    // 进行 n - 1 次松弛操作
    for (int i = 1; i < n; ++i) {
        for (const auto& edge : edges) {
            if (dist[edge.u] != INT_MAX && dist[edge.u] + edge.w < dist[edge.v]) {
                dist[edge.v] = dist[edge.u] + edge.w;
            }
        }
    }

    // 检查是否存在负环
    for (const auto& edge : edges) {
        if (dist[edge.u] != INT_MAX && dist[edge.u] + edge.w < dist[edge.v]) {
            return true;
        }
    }

    return false;
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n, m;
        cin >> n >> m;

        vector<Edge> edges;

        for (int i = 0; i < m; ++i) {
            int u, v, w;
            cin >> u >> v >> w;

            if (w >= 0) {
                edges.push_back({u, v, w});
                edges.push_back({v, u, w});
            } else {
                edges.push_back({u, v, w});
            }
        }

        if (hasNegativeCycle(n, edges)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}    