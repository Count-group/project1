#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 定义边的结构体
struct Edge {
    int u, v, w;
    Edge(int u, int v, int w) : u(u), v(v), w(w) {}
    // 重载小于运算符，用于边的排序
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

// 并查集的查找操作
int find(vector<int>& parent, int x) {
    if (parent[x] != x) {
        parent[x] = find(parent, parent[x]);
    }
    return parent[x];
}

// 并查集的合并操作
void unite(vector<int>& parent, int x, int y) {
    int rootX = find(parent, x);
    int rootY = find(parent, y);
    if (rootX != rootY) {
        parent[rootX] = rootY;
    }
}

int kruskal(int n, vector<Edge>& edges) {
    // 对边按权重从小到大排序
    sort(edges.begin(), edges.end());

    vector<int> parent(n + 1);
    for (int i = 1; i <= n; ++i) {
        parent[i] = i;
    }

    int mstWeight = 0;
    int edgeCount = 0;

    // 遍历每条边
    for (const Edge& edge : edges) {
        int u = edge.u;
        int v = edge.v;
        int w = edge.w;

        int rootU = find(parent, u);
        int rootV = find(parent, v);

        // 如果u和v不在同一个连通分量中，则加入这条边
        if (rootU != rootV) {
            unite(parent, u, v);
            mstWeight += w;
            edgeCount++;
        }

        // 如果已经加入了n-1条边，说明最小生成树已经形成
        if (edgeCount == n - 1) {
            break;
        }
    }

    // 如果边的数量小于n-1，说明图不连通
    if (edgeCount < n - 1) {
        return -1;
    }

    return mstWeight;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<Edge> edges;
    for (int i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        edges.emplace_back(x, y, z);
    }

    int result = kruskal(n, edges);
    if (result == -1) {
        cout << "orz" << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}    