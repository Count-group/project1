#include <iostream>
#include <vector>
using namespace std;

const int MOD = 998244353;

// 快速幂函数，用于计算逆元
long long quick_pow(long long base, long long exp) {
    long long res = 1;
    while (exp > 0) {
        if (exp & 1) res = res * base % MOD;
        base = base * base % MOD;
        exp >>= 1;
    }
    return res;
}

// 求解 f(k) 的值
long long lagrange_interpolation(const vector<pair<long long, long long>>& points, long long k) {
    int n = points.size();
    long long result = 0;

    for (int i = 0; i < n; ++i) {
        long long numerator = 1, denominator = 1;

        for (int j = 0; j < n; ++j) {
            if (i != j) {
                numerator = numerator * (k - points[j].first + MOD) % MOD;
                denominator = denominator * (points[i].first - points[j].first + MOD) % MOD;
            }
        }

        long long term = numerator * quick_pow(denominator, MOD - 2) % MOD;
        result = (result + term * points[i].second) % MOD;
    }

    return (result + MOD) % MOD;
}

int main() {
    int n;
    long long k;
    cin >> n >> k;

    vector<pair<long long, long long>> points(n);
    for (int i = 0; i < n; ++i) {
        cin >> points[i].first >> points[i].second;
    }

    long long result = lagrange_interpolation(points, k);
    cout << result << endl;

    return 0;
}