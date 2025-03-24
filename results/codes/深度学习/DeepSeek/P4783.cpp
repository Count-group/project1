#include <iostream>
#include <vector>
using namespace std;

const long long MOD = 1e9 + 7;

long long pow_mod(long long a, long long b) {
    long long res = 1;
    a %= MOD;
    while (b > 0) {
        if (b % 2 == 1) {
            res = res * a % MOD;
        }
        a = a * a % MOD;
        b /= 2;
    }
    return res;
}

long long mod_inverse(long long a) {
    return pow_mod(a, MOD - 2);
}

int main() {
    int n;
    cin >> n;
    vector<vector<long long>> mat(n, vector<long long>(2 * n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> mat[i][j];
            mat[i][j] %= MOD;
            if (mat[i][j] < 0) mat[i][j] += MOD;
        }
        mat[i][i + n] = 1;
    }

    for (int i = 0; i < n; ++i) {
        int r = -1;
        for (int j = i; j < n; ++j) {
            if (mat[j][i] != 0) {
                r = j;
                break;
            }
        }
        if (r == -1) {
            cout << "No Solution" << endl;
            return 0;
        }
        swap(mat[i], mat[r]);

        long long inv = mod_inverse(mat[i][i]);
        for (int k = 0; k < 2 * n; ++k) {
            mat[i][k] = mat[i][k] * inv % MOD;
        }

        for (int j = 0; j < n; ++j) {
            if (j == i) continue;
            long long coeff = mat[j][i];
            for (int k = 0; k < 2 * n; ++k) {
                long long sub = (coeff * mat[i][k]) % MOD;
                mat[j][k] = (mat[j][k] - sub + MOD) % MOD;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << mat[i][j + n] << " ";
        }
        cout << endl;
    }

    return 0;
}