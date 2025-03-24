#include <iostream>
using namespace std;

long long fast_pow_mod(long long a, long long b, long long p) {
    long long result = 1;
    a %= p; // 先对a取模，避免a本身大于p的情况
    while (b > 0) {
        if (b % 2 == 1) { // 如果b的二进制当前位是1，乘到结果中
            result = (result * a) % p;
        }
        a = (a * a) % p; // 平方基数
        b /= 2; // 右移一位
    }
    return result;
}

int main() {
    long long a, b, p;
    cin >> a >> b >> p;
    long long s = fast_pow_mod(a, b, p);
    cout << a << "^" << b << " mod " << p << "=" << s << endl;
    return 0;
}