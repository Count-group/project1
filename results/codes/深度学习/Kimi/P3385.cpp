#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9;

struct Edge {
    int u, v, w;
    Edge(int u, int v, int w) : u(u), v(v), w(w) {}
};

bool hasNegativeCycle(int n, const vector<Edge>& edges) {
    vector<int> dist(n + 1, INF);
    vector<int> pre(n + 1, -1);
    vector<int> cnt(n + 1, 0);

    dist[1] = 0;

    // 进行n次松弛操作
    for (int i = 1; i <= n; ++i) {
        bool updated = false;
        for (const Edge& e : edges) {
            if (dist[e.u] != INF && dist[e.v] > dist[e.u] + e.w) {
                dist[e.v] = dist[e.u] + e.w;
                pre[e.v] = e.u;
                cnt[e.v] = cnt[e.u] + 1;
                if (cnt[e.v] >= n) { // 发现负环
                    // 检查负环是否在从1出发的路径上
                    int node = e.v;
                    for (int j = 0; j < n; ++j) {
                        if (node == 1) return true;
                        node = pre[node];
                    }
                    return true;
                }
                updated = true;
            }
        }
        if (!updated) break;
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
                // 添加双向边
                edges.emplace_back(u, v, w);
                edges.emplace_back(v, u, w);
            } else {
                // 只添加单向边
                edges.emplace_back(u, v, w);
            }
        }

        bool result = hasNegativeCycle(n, edges);
        cout << (result ? "YES" : "NO") << endl;
    }

    return 0;
}