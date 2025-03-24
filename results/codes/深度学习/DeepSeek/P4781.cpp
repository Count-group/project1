#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

long long pow_mod(long long a, long long b, long long mod) {
    long long res = 1;
    a %= mod;
    while (b > 0) {
        if (b % 2 == 1)
            res = (res * a) % mod;
        a = (a * a) % mod;
        b /= 2;
    }
    return res;
}

int main() {
    int n, k;
    scanf("%d%d", &n, &k);
    
    vector<int> x(n), y(n);
    unordered_map<int, int> x_to_y;
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", &x[i], &y[i]);
        x[i] %= MOD;
        y[i] %= MOD;
        x_to_y[x[i]] = y[i];
    }
    
    // 检查k是否存在于已知点中
    if (x_to_y.count(k)) {
        printf("%d\n", x_to_y[k] % MOD);
        return 0;
    }
    
    // 预处理分母和分母逆元
    vector<long long> denominator(n, 1);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (j == i) continue;
            long long diff = (x[i] - x[j]) % MOD;
            if (diff < 0) diff += MOD;
            denominator[i] = (denominator[i] * diff) % MOD;
        }
    }
    
    vector<long long> denominator_inv(n);
    for (int i = 0; i < n; ++i) {
        denominator_inv[i] = pow_mod(denominator[i], MOD - 2, MOD);
    }
    
    // 计算总乘积P
    long long P = 1;
    for (int j = 0; j < n; ++j) {
        long long term = (k - x[j]) % MOD;
        if (term < 0) term += MOD;
        P = (P * term) % MOD;
    }
    
    // 计算每个项的贡献
    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        long long diff = (k - x[i]) % MOD;
        if (diff < 0) diff += MOD;
        long long inv_diff = pow_mod(diff, MOD - 2, MOD);
        long long numer = (P * inv_diff) % MOD;
        long long term = y[i];
        term = (term * numer) % MOD;
        term = (term * denominator_inv[i]) % MOD;
        sum = (sum + term) % MOD;
    }
    
    sum = (sum % MOD + MOD) % MOD; // 确保结果非负
    printf("%lld\n", sum);
    
    return 0;
}