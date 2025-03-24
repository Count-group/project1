#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, weight;
};

bool compareEdges(const Edge& a, const Edge& b) {
    return a.weight < b.weight;
}

int find(int parent[], int i) {
    if (parent[i] == i)
        return i;
    return find(parent, parent[i]);
}

void unionSets(int parent[], int rank[], int x, int y) {
    x = find(parent, x);
    y = find(parent, y);
    if (rank[x] < rank[y])
        parent[x] = y;
    else if (rank[x] > rank[y])
        parent[y] = x;
    else {
        parent[y] = x;
        rank[x]++;
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    vector<Edge> edges(M);
    for (int i = 0; i < M; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].weight;
    }

    // Sort edges by weight
    sort(edges.begin(), edges.end(), compareEdges);

    int parent[N + 1];
    int rank[N + 1];
    for (int i = 1; i <= N; i++) {
        parent[i] = i;
        rank[i] = 0;
    }

    int mstWeight = 0;
    int edgesUsed = 0;

    for (const auto& edge : edges) {
        int x = find(parent, edge.u);
        int y = find(parent, edge.v);
        if (x != y) {
            mstWeight += edge.weight;
            unionSets(parent, rank, x, y);
            edgesUsed++;
        }
    }

    if (edgesUsed == N - 1) {
        cout << mstWeight << endl;
    } else {
        cout << "orz" << endl;
    }

    return 0;
}