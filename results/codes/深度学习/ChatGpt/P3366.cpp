#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Edge {
    int u, v;
    int w;
};

bool cmp(const Edge &a, const Edge &b) {
    return a.w < b.w;
}

int find(vector<int>& parent, int x) {
    if (parent[x] != x)
        parent[x] = find(parent, parent[x]);
    return parent[x];
}

void unionn(vector<int>& parent, vector<int>& rank, int x, int y) {
    x = find(parent, x);
    y = find(parent, y);
    if(x == y) return;
    if(rank[x] < rank[y])
        parent[x] = y;
    else {
        parent[y] = x;
        if(rank[x] == rank[y])
            rank[x]++;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M;
    cin >> N >> M;
    vector<Edge> edges(M);
    
    for (int i = 0; i < M; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }
    
    sort(edges.begin(), edges.end(), cmp);
    
    // 初始化并查集
    vector<int> parent(N + 1);
    vector<int> rank(N + 1, 0);
    for (int i = 1; i <= N; i++) {
        parent[i] = i;
    }
    
    int cnt = 0;
    long long sum = 0;
    for (int i = 0; i < M; i++) {
        int u = edges[i].u, v = edges[i].v;
        if (find(parent, u) != find(parent, v)) {
            unionn(parent, rank, u, v);
            sum += edges[i].w;
            cnt++;
        }
    }
    
    // 检查是否构成一个生成树（即连通图）
    if (cnt != N - 1)
        cout << "orz";
    else
        cout << sum;
    
    return 0;
}
