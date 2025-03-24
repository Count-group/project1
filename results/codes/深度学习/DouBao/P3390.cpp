#include <iostream>
#include <vector>
const int MOD = 1e9 + 7;

// 矩阵乘法函数
std::vector<std::vector<long long>> matrixMultiply(const std::vector<std::vector<long long>>& A, const std::vector<std::vector<long long>>& B) {
    int n = A.size();
    std::vector<std::vector<long long>> result(n, std::vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return result;
}

// 矩阵快速幂函数
std::vector<std::vector<long long>> matrixPower(const std::vector<std::vector<long long>>& A, long long k) {
    int n = A.size();
    std::vector<std::vector<long long>> result(n, std::vector<long long>(n, 0));
    // 初始化结果矩阵为单位矩阵
    for (int i = 0; i < n; ++i) {
        result[i][i] = 1;
    }
    std::vector<std::vector<long long>> base = A;
    while (k > 0) {
        if (k & 1) {
            result = matrixMultiply(result, base);
        }
        base = matrixMultiply(base, base);
        k >>= 1;
    }
    return result;
}

int main() {
    int n;
    long long k;
    std::cin >> n >> k;
    std::vector<std::vector<long long>> A(n, std::vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> A[i][j];
        }
    }
    std::vector<std::vector<long long>> result = matrixPower(A, k);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cout << result[i][j] << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}    