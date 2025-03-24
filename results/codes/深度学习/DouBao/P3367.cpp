#include <iostream>
#include <vector>

using namespace std;

// 查找元素所在集合的根节点
int find(vector<int>& parent, int x) {
    if (parent[x] != x) {
        parent[x] = find(parent, parent[x]);
    }
    return parent[x];
}

// 合并两个元素所在的集合
void unite(vector<int>& parent, int x, int y) {
    int rootX = find(parent, x);
    int rootY = find(parent, y);
    if (rootX != rootY) {
        parent[rootX] = rootY;
    }
}

// 判断两个元素是否在同一集合内
bool isConnected(vector<int>& parent, int x, int y) {
    return find(parent, x) == find(parent, y);
}

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> parent(N + 1);
    // 初始化每个元素的父节点为自身
    for (int i = 1; i <= N; ++i) {
        parent[i] = i;
    }

    for (int i = 0; i < M; ++i) {
        int Z, X, Y;
        cin >> Z >> X >> Y;
        if (Z == 1) {
            unite(parent, X, Y);
        } else if (Z == 2) {
            if (isConnected(parent, X, Y)) {
                cout << "Y" << endl;
            } else {
                cout << "N" << endl;
            }
        }
    }

    return 0;
}    