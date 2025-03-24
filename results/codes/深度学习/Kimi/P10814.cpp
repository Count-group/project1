#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct SegmentTree {
    int l, r;
    vector<int> sorted;
    SegmentTree *left, *right;

    SegmentTree(int _l, int _r, const vector<int>& arr) : l(_l), r(_r), left(nullptr), right(nullptr) {
        if (l == r) {
            sorted.push_back(arr[l]);
        } else {
            int mid = (l + r) / 2;
            left = new SegmentTree(l, mid, arr);
            right = new SegmentTree(mid + 1, r, arr);
            sorted.resize(left->sorted.size() + right->sorted.size());
            merge(left->sorted.begin(), left->sorted.end(), right->sorted.begin(), right->sorted.end(), sorted.begin());
        }
    }

    int query(int L, int R, int x) {
        if (R < l || L > r) return 0;
        if (L <= l && r <= R) {
            return upper_bound(sorted.begin(), sorted.end(), x) - sorted.begin();
        }
        return left->query(L, R, x) + right->query(L, R, x);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    SegmentTree* root = new SegmentTree(0, n - 1, a);

    while (m--) {
        int l, r, x;
        cin >> l >> r >> x;
        l--; r--;
        cout << root->query(l, r, x) << '\n';
    }

    return 0;
}