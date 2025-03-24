#include <iostream>
using namespace std;

const int MAXN = 1e5 + 10;

struct Node {
    int l, r;
    long long sum, add;
    int lson, rson;
} tree[MAXN * 4];

int cnt = 0;
long long a[MAXN];

int build(int l, int r) {
    int idx = ++cnt;
    tree[idx].l = l;
    tree[idx].r = r;
    tree[idx].add = 0;
    if (l == r) {
        tree[idx].sum = a[l];
        tree[idx].lson = tree[idx].rson = 0;
        return idx;
    }
    int mid = (l + r) >> 1;
    tree[idx].lson = build(l, mid);
    tree[idx].rson = build(mid + 1, r);
    tree[idx].sum = tree[tree[idx].lson].sum + tree[tree[idx].rson].sum;
    return idx;
}

void push_down(int idx) {
    if (tree[idx].add != 0 && tree[idx].l != tree[idx].r) {
        int lson = tree[idx].lson;
        int rson = tree[idx].rson;
        long long add = tree[idx].add;

        tree[lson].sum += add * (tree[lson].r - tree[lson].l + 1);
        tree[lson].add += add;

        tree[rson].sum += add * (tree[rson].r - tree[rson].l + 1);
        tree[rson].add += add;

        tree[idx].add = 0;
    }
}

void update(int idx, int L, int R, long long k) {
    if (tree[idx].r < L || tree[idx].l > R) return;
    if (L <= tree[idx].l && tree[idx].r <= R) {
        tree[idx].sum += k * (tree[idx].r - tree[idx].l + 1);
        tree[idx].add += k;
        return;
    }
    push_down(idx);
    update(tree[idx].lson, L, R, k);
    update(tree[idx].rson, L, R, k);
    tree[idx].sum = tree[tree[idx].lson].sum + tree[tree[idx].rson].sum;
}

long long query(int idx, int L, int R) {
    if (tree[idx].r < L || tree[idx].l > R) return 0;
    if (L <= tree[idx].l && tree[idx].r <= R) return tree[idx].sum;
    push_down(idx);
    return query(tree[idx].lson, L, R) + query(tree[idx].rson, L, R);
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) cin >> a[i];
    int root = build(1, n);

    while (m--) {
        int op, l, r;
        long long k;
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> k;
            update(root, l, r, k);
        } else {
            cin >> l >> r;
            cout << query(root, l, r) << endl;
        }
    }
    return 0;
}