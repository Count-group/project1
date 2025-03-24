#include <bits/stdc++.h>
using namespace std;

struct Element {
    int value, pos;
    bool operator<(const Element& other) const {
        return value < other.value;
    }
};

struct Query {
    int l, r, x, idx;
    bool operator<(const Query& other) const {
        return x < other.x;
    }
};

class FenwickTree {
private:
    vector<int> tree;
public:
    FenwickTree(int size) : tree(size + 2) {}
    
    void update(int pos, int delta) {
        for (; pos < tree.size(); pos += pos & -pos)
            tree[pos] += delta;
    }
    
    int prefix_sum(int pos) {
        int sum = 0;
        for (; pos > 0; pos -= pos & -pos)
            sum += tree[pos];
        return sum;
    }
    
    int range_sum(int l, int r) {
        return prefix_sum(r) - prefix_sum(l - 1);
    }
};

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    
    vector<Element> elements(n);
    for (int i = 0; i < n; ++i) {
        int val;
        scanf("%d", &val);
        elements[i] = {val, i + 1}; // 转换为1-based位置
    }
    sort(elements.begin(), elements.end());

    vector<Query> queries(m);
    for (int i = 0; i < m; ++i) {
        int l, r, x;
        scanf("%d%d%d", &l, &r, &x);
        queries[i] = {l, r, x, i};
    }
    sort(queries.begin(), queries.end());

    FenwickTree ft(n);
    vector<int> ans(m);
    int elem_ptr = 0;
    
    for (auto& q : queries) {
        // 插入所有值小于等于当前查询x的元素
        while (elem_ptr < n && elements[elem_ptr].value <= q.x) {
            ft.update(elements[elem_ptr].pos, 1);
            ++elem_ptr;
        }
        // 计算区间和
        ans[q.idx] = ft.range_sum(q.l, q.r);
    }

    for (auto& cnt : ans)
        printf("%d\n", cnt);

    return 0;
}