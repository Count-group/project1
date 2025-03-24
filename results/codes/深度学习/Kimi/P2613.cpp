#include <iostream>
#include <string>
using namespace std;

const int MOD = 19260817;

long long compute_mod(const string &s, long long m) {
    long long result = 0;
    for (char c : s) {
        result = (result * 10 + (c - '0')) % m;
    }
    return result;
}

int extended_gcd(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int gcd = extended_gcd(b, a % b, y, x);
    y -= (a / b) * x;
    return gcd;
}

int main() {
    string a_str, b_str;
    cin >> a_str >> b_str;

    long long a_mod = compute_mod(a_str, MOD);
    long long b_mod = compute_mod(b_str, MOD);

    int gcd, x, y;
    gcd = extended_gcd(static_cast<int>(b_mod), MOD, x, y);

    if (gcd != 1) {
        cout << "Angry!" << endl;
    } else {
        x = (x % MOD + MOD) % MOD; // Ensure x is positive
        long long result = (a_mod * x) % MOD;
        cout << result << endl;
    }

    return 0;
}