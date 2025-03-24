#include <iostream>
#include <vector>

using namespace std;

// 线段树节点结构体
struct Node {
    long long sum;  // 区间和
    long long lazy; // 懒标记
    Node() : sum(0), lazy(0) {}
};

// 构建线段树
void build(vector<Node>& tree, const vector<long long>& arr, int node, int start, int end) {
    if (start == end) {
        tree[node].sum = arr[start];
        return;
    }
    int mid = (start + end) / 2;
    int leftChild = 2 * node + 1;
    int rightChild = 2 * node + 2;
    build(tree, arr, leftChild, start, mid);
    build(tree, arr, rightChild, mid + 1, end);
    tree[node].sum = tree[leftChild].sum + tree[rightChild].sum;
}

// 下推懒标记
void pushDown(vector<Node>& tree, int node, int start, int end) {
    if (tree[node].lazy != 0) {
        int mid = (start + end) / 2;
        int leftChild = 2 * node + 1;
        int rightChild = 2 * node + 2;
        tree[leftChild].sum += (mid - start + 1) * tree[node].lazy;
        tree[rightChild].sum += (end - mid) * tree[node].lazy;
        tree[leftChild].lazy += tree[node].lazy;
        tree[rightChild].lazy += tree[node].lazy;
        tree[node].lazy = 0;
    }
}

// 区间更新
void updateRange(vector<Node>& tree, int node, int start, int end, int l, int r, long long val) {
    if (start > r || end < l) return;
    if (start >= l && end <= r) {
        tree[node].sum += (end - start + 1) * val;
        tree[node].lazy += val;
        return;
    }
    pushDown(tree, node, start, end);
    int mid = (start + end) / 2;
    int leftChild = 2 * node + 1;
    int rightChild = 2 * node + 2;
    updateRange(tree, leftChild, start, mid, l, r, val);
    updateRange(tree, rightChild, mid + 1, end, l, r, val);
    tree[node].sum = tree[leftChild].sum + tree[rightChild].sum;
}

// 区间查询
long long queryRange(vector<Node>& tree, int node, int start, int end, int l, int r) {
    if (start > r || end < l) return 0;
    if (start >= l && end <= r) return tree[node].sum;
    pushDown(tree, node, start, end);
    int mid = (start + end) / 2;
    int leftChild = 2 * node + 1;
    int rightChild = 2 * node + 2;
    return queryRange(tree, leftChild, start, mid, l, r) + queryRange(tree, rightChild, mid + 1, end, l, r);
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<long long> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    vector<Node> tree(4 * n);
    build(tree, arr, 0, 0, n - 1);

    for (int i = 0; i < m; ++i) {
        int op;
        cin >> op;
        if (op == 1) {
            int x, y;
            long long k;
            cin >> x >> y >> k;
            updateRange(tree, 0, 0, n - 1, x - 1, y - 1, k);
        } else {
            int x, y;
            cin >> x >> y;
            cout << queryRange(tree, 0, 0, n - 1, x - 1, y - 1) << endl;
        }
    }
    return 0;
}    