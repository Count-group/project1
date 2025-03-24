#include <iostream>
#include <vector>
using namespace std;

const int MAXN = 200005;

int parent[MAXN];
int rank_[MAXN];

// 查找函数，带路径压缩
int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]);
    }
    return parent[x];
}

// 合并函数，按秩合并
void unite(int x, int y) {
    int rootX = find(x);
    int rootY = find(y);
    if (rootX != rootY) {
        if (rank_[rootX] > rank_[rootY]) {
            parent[rootY] = rootX;
        } else if (rank_[rootX] < rank_[rootY]) {
            parent[rootX] = rootY;
        } else {
            parent[rootY] = rootX;
            rank_[rootX]++;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    // 初始化并查集
    for (int i = 1; i <= N; ++i) {
        parent[i] = i;
        rank_[i] = 0;
    }

    vector<char> results;

    for (int i = 0; i < M; ++i) {
        int Z, X, Y;
        cin >> Z >> X >> Y;

        if (Z == 1) {
            // 合并操作
            unite(X, Y);
        } else {
            // 查询操作
            if (find(X) == find(Y)) {
                results.push_back('Y');
            } else {
                results.push_back('N');
            }
        }
    }

    // 输出所有查询结果
    for (char c : results) {
        cout << c << endl;
    }

    return 0;
}