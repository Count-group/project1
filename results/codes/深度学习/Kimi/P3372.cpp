#include <iostream>
using namespace std;

const int MAXN = 1e5 + 10;
struct Node {
    int l, r;
    long long sum, add;
} tree[4 * MAXN];
long long a[MAXN];

void pushdown(int p) {
    if (tree[p].add != 0 && tree[p].l != tree[p].r) {
        int left = 2 * p, right = 2 * p + 1;
        tree[left].sum += tree[p].add * (tree[left].r - tree[left].l + 1);
        tree[left].add += tree[p].add;
        tree[right].sum += tree[p].add * (tree[right].r - tree[right].l + 1);
        tree[right].add += tree[p].add;
        tree[p].add = 0;
    }
}

void build(int p, int l, int r) {
    tree[p].l = l;
    tree[p].r = r;
    tree[p].add = 0;
    if (l == r) {
        tree[p].sum = a[l];
        return;
    }
    int mid = (l + r) / 2;
    build(2 * p, l, mid);
    build(2 * p + 1, mid + 1, r);
    tree[p].sum = tree[2 * p].sum + tree[2 * p + 1].sum;
}

void update(int p, int l, int r, long long k) {
    if (tree[p].r < l || tree[p].l > r) return;
    if (l <= tree[p].l && tree[p].r <= r) {
        tree[p].sum += k * (tree[p].r - tree[p].l + 1);
        tree[p].add += k;
        return;
    }
    pushdown(p);
    update(2 * p, l, r, k);
    update(2 * p + 1, l, r, k);
    tree[p].sum = tree[2 * p].sum + tree[2 * p + 1].sum;
}

long long query(int p, int l, int r) {
    if (tree[p].r < l || tree[p].l > r) return 0;
    if (l <= tree[p].l && tree[p].r <= r) {
        return tree[p].sum;
    }
    pushdown(p);
    return query(2 * p, l, r) + query(2 * p + 1, l, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }
    build(1, 1, n);
    while (m--) {
        int op, x, y;
        cin >> op;
        if (op == 1) {
            long long k;
            cin >> x >> y >> k;
            update(1, x, y, k);
        } else {
            cin >> x >> y;
            cout << query(1, x, y) << '\n';
        }
    }
    return 0;
}