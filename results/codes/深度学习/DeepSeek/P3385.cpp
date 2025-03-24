#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

const int MAXN = 2005; // 假设足够大
const int INF = 1e9;

struct Edge {
    int v, w;
};

vector<Edge> adj[MAXN];
int dist[MAXN];
int cnt[MAXN];
bool inq[MAXN];

bool spfa(int start, int n) {
    fill(dist, dist + n + 1, INF);
    memset(cnt, 0, sizeof(cnt));
    memset(inq, 0, sizeof(inq));
    queue<int> q;
    dist[start] = 0;
    q.push(start);
    inq[start] = true;
    cnt[start] = 1;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        inq[u] = false;

        for (Edge &e : adj[u]) {
            int v = e.v;
            int w = e.w;
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                if (!inq[v]) {
                    cnt[v]++;
                    if (cnt[v] > n) {
                        return true;
                    }
                    q.push(v);
                    inq[v] = true;
                }
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        for (int i = 1; i <= n; ++i) adj[i].clear();
        for (int i = 0; i < m; ++i) {
            int u, v, w;
            cin >> u >> v >> w;
            if (w >= 0) {
                adj[u].push_back({v, w});
                adj[v].push_back({u, w});
            } else {
                adj[u].push_back({v, w});
            }
        }

        bool has_cycle = spfa(1, n);
        cout << (has_cycle ? "YES" : "NO") << '\n';
    }
    return 0;
}