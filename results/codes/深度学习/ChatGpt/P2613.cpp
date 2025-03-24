#include <iostream>
#include <string>
using namespace std;

// 自己写的 gcd 函数（欧几里得算法）
long long gcd(long long a, long long b) {
    return b == 0 ? a : gcd(b, a % b);
}

// 计算一个大整数（以字符串表示）对 m 的余数
long long modString(const string &s, long long m) {
    long long rem = 0;
    for (char c : s) {
        rem = (rem * 10 + (c - '0')) % m;
    }
    return rem;
}

// 扩展欧几里得算法
// 求出 x, y，使得 a*x + b*y = gcd(a, b)
long long extended_gcd(long long a, long long b, long long &x, long long &y) {
    if(b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long d = extended_gcd(b, a % b, y, x);
    y -= (a / b) * x;
    return d;
}
 
// 求 a 在模 m 下的逆元（保证 gcd(a, m)==1）
long long modInverse(long long a, long long m) {
    long long x, y;
    long long g = extended_gcd(a, m, x, y);
    if(g != 1) return -1; // 不存在逆元
    x %= m;
    if(x < 0) x += m;
    return x;
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    string a_str, b_str;
    cin >> a_str >> b_str;
    const long long M = 19260817;
    
    // 计算 a 和 b 对 M 的余数
    long long A = modString(a_str, M);
    long long B = modString(b_str, M);
    
    // 求 d = gcd(B, M)（使用自己写的 gcd 函数）
    long long d = gcd(B, M);
    // 如果 d 不能整除 A，则方程无解
    if(A % d != 0){
        cout << "Angry!" << "\n";
        return 0;
    }
    
    // 化简方程： B' * x ≡ A' (mod M')
    long long A_ = A / d;
    long long B_ = B / d;
    long long M_ = M / d;
    
    // 求 B_' 的逆元（此时 gcd(B_, M_) = 1）
    long long invB = modInverse(B_, M_);
    if(invB == -1) {
        cout << "Angry!" << "\n";
        return 0;
    }
    
    // 得到特解
    long long x0 = (A_ % M_ * invB) % M_;
    cout << x0 << "\n";
    
    return 0;
}
