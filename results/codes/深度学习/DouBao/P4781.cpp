#include <iostream>
const int MOD = 998244353;

// 快速幂函数，用于计算 a^b % MOD
long long quickPow(long long a, long long b) {
    long long res = 1;
    while (b) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

// 拉格朗日插值法计算 f(k) % MOD
long long lagrange(int n, int k, int x[], int y[]) {
    long long res = 0;
    for (int i = 0; i < n; ++i) {
        long long numerator = 1, denominator = 1;
        for (int j = 0; j < n; ++j) {
            if (i != j) {
                numerator = numerator * (k - x[j] + MOD) % MOD;
                denominator = denominator * (x[i] - x[j] + MOD) % MOD;
            }
        }
        res = (res + y[i] * numerator % MOD * quickPow(denominator, MOD - 2) % MOD) % MOD;
    }
    return res;
}

int main() {
    int n, k;
    std::cin >> n >> k;
    int x[2005], y[2005];
    for (int i = 0; i < n; ++i) {
        std::cin >> x[i] >> y[i];
    }
    std::cout << lagrange(n, k, x, y) << std::endl;
    return 0;
}    