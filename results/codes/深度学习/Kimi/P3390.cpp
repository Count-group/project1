#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

vector<vector<int>> multiply(const vector<vector<int>>& a, const vector<vector<int>>& b) {
    int n = a.size();
    vector<vector<int>> res(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            long long sum = 0;
            for (int k = 0; k < n; ++k) {
                sum = (sum + (long long)a[i][k] * b[k][j]) % MOD;
            }
            res[i][j] = sum;
        }
    }
    return res;
}

vector<vector<int>> identity_matrix(int n) {
    vector<vector<int>> mat(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i) {
        mat[i][i] = 1 % MOD;
    }
    return mat;
}

vector<vector<int>> matrix_pow(vector<vector<int>> base, long long power) {
    int n = base.size();
    vector<vector<int>> result = identity_matrix(n);
    while (power > 0) {
        if (power % 2 == 1) {
            result = multiply(result, base);
        }
        base = multiply(base, base);
        power /= 2;
    }
    return result;
}

int main() {
    int n;
    long long k;
    cin >> n >> k;
    vector<vector<int>> mat(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> mat[i][j];
            mat[i][j] = (mat[i][j] % MOD + MOD) % MOD;
        }
    }
    if (k == 0) {
        auto res = identity_matrix(n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cout << res[i][j];
                if (j < n - 1) cout << " ";
            }
            cout << endl;
        }
    } else {
        auto res = matrix_pow(mat, k);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cout << res[i][j];
                if (j < n - 1) cout << " ";
            }
            cout << endl;
        }
    }
    return 0;
}