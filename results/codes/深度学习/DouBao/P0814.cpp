#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 2e6 + 5;

// 主席树节点结构体
struct Node {
    int l, r, sum;
} tree[MAXN * 20];

// 离散化数组和根节点数组
int root[MAXN], arr[MAXN], b[MAXN];
int cnt = 0;

// 构建空树
int build(int l, int r) {
    int now = ++cnt;
    tree[now].l = tree[now].r = 0;
    tree[now].sum = 0;
    if (l < r) {
        int mid = (l + r) >> 1;
        tree[now].l = build(l, mid);
        tree[now].r = build(mid + 1, r);
    }
    return now;
}

// 更新操作
int update(int pre, int l, int r, int x) {
    int now = ++cnt;
    tree[now] = tree[pre];
    tree[now].sum++;
    if (l < r) {
        int mid = (l + r) >> 1;
        if (x <= mid) {
            tree[now].l = update(tree[pre].l, l, mid, x);
        } else {
            tree[now].r = update(tree[pre].r, mid + 1, r, x);
        }
    }
    return now;
}

// 查询操作
int query(int u, int v, int l, int r, int x) {
    if (r <= x) {
        return tree[v].sum - tree[u].sum;
    }
    int mid = (l + r) >> 1;
    int res = 0;
    res += query(tree[u].l, tree[v].l, l, mid, x);
    if (x > mid) {
        res += query(tree[u].r, tree[v].r, mid + 1, r, x);
    }
    return res;
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        cin >> arr[i];
        b[i] = arr[i];
    }
    // 离散化
    sort(b + 1, b + n + 1);
    int sz = unique(b + 1, b + n + 1) - b - 1;
    root[0] = build(1, sz);
    for (int i = 1; i <= n; ++i) {
        int pos = lower_bound(b + 1, b + sz + 1, arr[i]) - b;
        root[i] = update(root[i - 1], 1, sz, pos);
    }
    for (int i = 0; i < m; ++i) {
        int l, r, x;
        cin >> l >> r >> x;
        int pos = upper_bound(b + 1, b + sz + 1, x) - b - 1;
        if (pos < 1) {
            cout << 0 << endl;
        } else {
            cout << query(root[l - 1], root[r], 1, sz, pos) << endl;
        }
    }
    return 0;
}
    