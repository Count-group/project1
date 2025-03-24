#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<long long>> Matrix;
const long long MOD = 1000000007;

// 矩阵乘法，结果取模
void multiply(const Matrix &a, const Matrix &b, Matrix &res) {
    int n = a.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            res[i][j] = 0;
            for (int k = 0; k < n; ++k) {
                res[i][j] += (a[i][k] % MOD) * (b[k][j] % MOD);
                res[i][j] %= MOD;
            }
        }
    }
}

// 矩阵快速幂
Matrix matrix_pow(Matrix a, long long k) {
    int n = a.size();
    Matrix res(n, vector<long long>(n, 0));
    Matrix temp(n, vector<long long>(n));
    
    // 初始化单位矩阵
    for (int i = 0; i < n; ++i)
        res[i][i] = 1;
    
    while (k > 0) {
        if (k % 2 == 1) {
            multiply(res, a, temp);
            swap(res, temp);
        }
        multiply(a, a, temp);
        swap(a, temp);
        k /= 2;
    }
    return res;
}

int main() {
    int n;
    long long k;
    cin >> n >> k;
    Matrix a(n, vector<long long>(n));
    
    // 读取输入并处理负数
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> a[i][j];
            a[i][j] %= MOD;
            if (a[i][j] < 0) a[i][j] += MOD;
        }
    }
    
    Matrix result = matrix_pow(a, k);
    
    // 输出结果并确保非负
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << (result[i][j] % MOD + MOD) % MOD << " ";
        }
        cout << endl;
    }
    
    return 0;
}