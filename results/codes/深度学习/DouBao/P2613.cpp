#include <iostream>
#include <string>
using namespace std;

const long long MOD = 19260817;

// 快速幂函数
long long quick_pow(long long a, long long b) {
    long long res = 1;
    while (b) {
        if (b & 1) {
            res = res * a % MOD;
        }
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

// 将字符串转换为模 MOD 意义下的整数
long long str_to_num(const string& s) {
    long long res = 0;
    for (char c : s) {
        res = (res * 10 + (c - '0')) % MOD;
    }
    return res;
}

// 扩展欧几里得算法求逆元
long long exgcd(long long a, long long b, long long& x, long long& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long d = exgcd(b, a % b, y, x);
    y -= a / b * x;
    return d;
}

// 求 b 在模 MOD 意义下的逆元
long long mod_inverse(long long b) {
    long long x, y;
    long long d = exgcd(b, MOD, x, y);
    if (d != 1) {
        return -1;
    }
    return (x % MOD + MOD) % MOD;
}

int main() {
    string a_str, b_str;
    cin >> a_str >> b_str;

    long long a = str_to_num(a_str);
    long long b = str_to_num(b_str);

    long long inv_b = mod_inverse(b);
    if (inv_b == -1) {
        cout << "Angry!" << endl;
    } else {
        long long result = a * inv_b % MOD;
        cout << result << endl;
    }

    return 0;
}    