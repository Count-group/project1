#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Edge {
    int u, v, w;
    Edge(int a, int b, int c) : u(a), v(b), w(c) {}
    bool operator<(const Edge& e) const { return w < e.w; }
};

const int MAXN = 100005;
int parent[MAXN];

int find(int x) {
    if (parent[x] != x)
        parent[x] = find(parent[x]);
    return parent[x];
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<Edge> edges;
    for (int i = 0; i < M; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        edges.emplace_back(x, y, z);
    }
    sort(edges.begin(), edges.end());
    for (int i = 1; i <= N; ++i) parent[i] = i;
    int sum = 0, cnt = 0;
    for (const auto& e : edges) {
        int uRoot = find(e.u), vRoot = find(e.v);
        if (uRoot != vRoot) {
            parent[uRoot] = vRoot;
            sum += e.w;
            if (++cnt == N - 1) break;
        }
    }
    cout << (cnt == N - 1 ? to_string(sum) : "orz") << endl;
    return 0;
}