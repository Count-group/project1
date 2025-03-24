#include <iostream>
#include <string>
using namespace std;

const int MOD = 19260817;

long long mod(string s, long long p) {
    long long res = 0;
    for (int i = 0; i < s.size(); i++) {
        res = (res * 10 + (s[i] - '0')) % p;
    }
    return res;
}

int exgcd(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int g = exgcd(b, a % b, y, x);
    y -= a / b * x;
    return g;
}

int inverse(int a, int m) {
    int x, y;
    int g = exgcd(a, m, x, y);
    if (g != 1) return -1;
    return (x % m + m) % m;
}

int main() {
    string a_str, b_str;
    cin >> a_str >> b_str;
    
    long long a_mod = mod(a_str, MOD);
    long long b_mod = mod(b_str, MOD);
    
    if (b_mod == 0) {
        if (a_mod == 0) {
            cout << 0 << endl;
        } else {
            cout << -1 << endl;
        }
        return 0;
    }
    
    int x, y;
    int d = exgcd(b_mod, MOD, x, y);
    
    if (a_mod % d != 0) {
        cout << -1 << endl;
        return 0;
    }
    
    int b_prime = b_mod / d;
    int a_prime = a_mod / d;
    int p_prime = MOD / d;
    
    int inv = inverse(b_prime, p_prime);
    if (inv == -1) {
        cout << -1 << endl;
        return 0;
    }
    
    int result = (1LL * a_prime * inv) % p_prime;
    cout << result << endl;
    
    return 0;
}