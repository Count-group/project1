#include <iostream>
#include <vector>
#include <limits>
using namespace std;

struct Edge {
    int u, v;
    int w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<Edge> edges;
        // 输入边信息，若 w>=0 则添加双向边，否则添加单向边
        for (int i = 0; i < m; i++) {
            int u, v, w;
            cin >> u >> v >> w;
            if (w >= 0) {
                edges.push_back({u, v, w});
                edges.push_back({v, u, w});
            } else {
                edges.push_back({u, v, w});
            }
        }
        
        // 使用 Bellman-Ford 算法检测从 1 可达的负环
        const long long INF = numeric_limits<long long>::max() / 2;
        vector<long long> dist(n + 1, INF);
        dist[1] = 0;
        bool negative_cycle = false;
        
        // 松弛 n-1 次
        for (int i = 1; i < n; i++) {
            bool updated = false;
            for (auto &e : edges) {
                if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
                    dist[e.v] = dist[e.u] + e.w;
                    updated = true;
                }
            }
            if (!updated) break;
        }
        
        // 检测第 n 次松弛是否还可以更新
        for (auto &e : edges) {
            if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
                negative_cycle = true;
                break;
            }
        }
        
        cout << (negative_cycle ? "YES" : "NO") << "\n";
    }
    
    return 0;
}
