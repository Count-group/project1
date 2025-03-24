#include <iostream>
#include <vector>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    
    UnionFind(int n) : parent(n + 1), rank(n + 1, 0) {
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }
    }
    
    // 查找根节点，并进行路径压缩
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    // 合并两个集合，按秩合并
    void unionSets(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        if (rootA == rootB) return;
        
        if (rank[rootA] < rank[rootB]) {
            parent[rootA] = rootB;
        } else {
            parent[rootB] = rootA;
            if (rank[rootA] == rank[rootB]) {
                rank[rootA]++;
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    UnionFind uf(n);
    for (int i = 0; i < m; i++) {
        int z, x, y;
        cin >> z >> x >> y;
        if (z == 1) {
            // 合并操作
            uf.unionSets(x, y);
        } else if (z == 2) {
            // 查询操作，判断是否属于同一集合
            cout << (uf.find(x) == uf.find(y) ? "Y" : "N") << "\n";
        }
    }
    
    return 0;
}
