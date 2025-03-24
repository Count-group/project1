#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int n, m;
vector<ll> bit1, bit2;

// 更新树状数组：将delta加到下标i上
void update(vector<ll>& bit, int i, ll delta) {
    while (i <= n) {
        bit[i] += delta;
        i += i & (-i);
    }
}

// 查询前缀和
ll query(const vector<ll>& bit, int i) {
    ll s = 0;
    while (i > 0) {
        s += bit[i];
        i -= i & (-i);
    }
    return s;
}

// 区间更新 [l, r] 加上delta
void range_update(int l, int r, ll delta) {
    update(bit1, l, delta);
    update(bit1, r + 1, -delta);
    update(bit2, l, delta * (l - 1));
    update(bit2, r + 1, -delta * r);
}

// 计算前缀和
ll prefix_sum(int i) {
    return query(bit1, i) * i - query(bit2, i);
}

// 查询区间 [l, r] 的和
ll range_sum(int l, int r) {
    return prefix_sum(r) - prefix_sum(l - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> n >> m;
    bit1.resize(n + 1, 0);
    bit2.resize(n + 1, 0);
    
    // 输入初始序列，同时用单点更新初始化树状数组
    vector<ll> a(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        // 对于位置 i，相当于对 [i, i] 加上 a[i]
        range_update(i, i, a[i]);
    }
    
    // 处理 m 个操作
    while (m--) {
        int op;
        cin >> op;
        if (op == 1) {
            int x, y;
            ll k;
            cin >> x >> y >> k;
            range_update(x, y, k);
        } else if (op == 2) {
            int x, y;
            cin >> x >> y;
            cout << range_sum(x, y) << "\n";
        }
    }
    
    return 0;
}
