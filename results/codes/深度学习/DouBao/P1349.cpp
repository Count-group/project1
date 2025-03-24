#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> p1(n), p2(n);
    std::vector<int> index(n + 1);

    // 读取第一个排列
    for (int i = 0; i < n; ++i) {
        std::cin >> p1[i];
        index[p1[i]] = i;
    }

    // 读取第二个排列
    for (int i = 0; i < n; ++i) {
        std::cin >> p2[i];
    }

    std::vector<int> lis;
    for (int i = 0; i < n; ++i) {
        int idx = index[p2[i]];
        auto it = std::lower_bound(lis.begin(), lis.end(), idx);
        if (it == lis.end()) {
            lis.push_back(idx);
        } else {
            *it = idx;
        }
    }

    std::cout << lis.size() << std::endl;

    return 0;
}    