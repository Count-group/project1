#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Query {
    int l, r, x, idx;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++){
        cin >> a[i];
    }
    
    vector<Query> queries(m);
    for (int i = 0; i < m; i++){
        cin >> queries[i].l >> queries[i].r >> queries[i].x;
        queries[i].idx = i;
    }
    
    // 将查询按 x 从小到大排序
    sort(queries.begin(), queries.end(), [](const Query &q1, const Query &q2){
        return q1.x < q2.x;
    });
    
    // 将数组元素与下标 pair 化并按数值排序
    vector<pair<int, int>> arr;
    arr.reserve(n);
    for (int i = 1; i <= n; i++){
        arr.push_back({a[i], i});
    }
    sort(arr.begin(), arr.end());
    
    // 树状数组 BIT
    vector<int> BIT(n + 1, 0);
    auto update = [&](int pos, int delta) {
        for (; pos <= n; pos += pos & -pos)
            BIT[pos] += delta;
    };
    auto queryBIT = [&](int pos) -> int {
        int res = 0;
        for (; pos > 0; pos -= pos & -pos)
            res += BIT[pos];
        return res;
    };

    vector<int> ans(m, 0);
    int j = 0;  // arr 的指针
    // 遍历每个查询
    for (const auto &q : queries) {
        // 将数组中所有小于等于 q.x 的元素更新到 BIT 中
        while (j < n && arr[j].first <= q.x) {
            update(arr[j].second, 1);
            j++;
        }
        // 查询区间 [l, r] 中的元素个数
        ans[q.idx] = queryBIT(q.r) - queryBIT(q.l - 1);
    }
    
    for (int x : ans)
        cout << x << "\n";
    
    return 0;
}
