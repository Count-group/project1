#include <iostream>
#include <vector>
const int MOD = 1e9 + 7;

// 快速幂取模
long long quick_pow(long long a, long long b) {
    long long res = 1;
    while (b) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

// 高斯 - 约旦消元求逆矩阵
std::vector<std::vector<long long>> inverse_matrix(std::vector<std::vector<long long>>& A) {
    int n = A.size();
    std::vector<std::vector<long long>> B(n, std::vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) B[i][i] = 1;

    for (int i = 0; i < n; ++i) {
        if (A[i][i] == 0) {
            bool found = false;
            for (int j = i + 1; j < n; ++j) {
                if (A[j][i] != 0) {
                    std::swap(A[i], A[j]);
                    std::swap(B[i], B[j]);
                    found = true;
                    break;
                }
            }
            if (!found) return {};
        }
        long long inv = quick_pow(A[i][i], MOD - 2);
        for (int j = 0; j < n; ++j) {
            A[i][j] = A[i][j] * inv % MOD;
            B[i][j] = B[i][j] * inv % MOD;
        }
        for (int k = 0; k < n; ++k) {
            if (k != i) {
                long long factor = A[k][i];
                for (int j = 0; j < n; ++j) {
                    A[k][j] = (A[k][j] - factor * A[i][j] % MOD + MOD) % MOD;
                    B[k][j] = (B[k][j] - factor * B[i][j] % MOD + MOD) % MOD;
                }
            }
        }
    }
    return B;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<std::vector<long long>> A(n, std::vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> A[i][j];
        }
    }
    std::vector<std::vector<long long>> B = inverse_matrix(A);
    if (B.empty()) {
        std::cout << "No Solution" << std::endl;
    } else {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                std::cout << B[i][j];
                if (j < n - 1) std::cout << " ";
            }
            std::cout << std::endl;
        }
    }
    return 0;
}    