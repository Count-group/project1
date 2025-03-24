#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>

// 定义积分精度
const double EPS = 1e-6;

// 检查在给定 q1, q2 下所有游戏的期望得分是否都非负
bool checkExpectedScores(const std::vector<std::vector<int>>& A, const std::vector<std::vector<double>>& p, double q1, double q2) {
    double q3 = 1 - q1 - q2;
    // 检查 q1, q2, q3 是否在有效范围内
    if (q1 < 0 || q2 < 0 || q3 < 0) {
        return false;
    }
    std::vector<double> q = {q1, q2, q3};
    for (const auto& prob : p) {
        double expectedScore = 0;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                expectedScore += q[i] * prob[j] * A[i][j];
            }
        }
        if (expectedScore < 0) {
            return false;
        }
    }
    return true;
}

// 进行二重积分计算概率
double doubleIntegrate(const std::vector<std::vector<int>>& A, const std::vector<std::vector<double>>& p) {
    double sum = 0;
    // 对 q1 进行积分
    for (double q1 = 0; q1 <= 1; q1 += EPS) {
        // 对 q2 进行积分
        for (double q2 = 0; q2 <= 1 - q1; q2 += EPS) {
            if (checkExpectedScores(A, p, q1, q2)) {
                sum += EPS * EPS;
            }
        }
    }
    return sum;
}

int main() {
    int n;
    std::cin >> n;

    // 读取矩阵 A
    std::vector<std::vector<int>> A(3, std::vector<int>(3));
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            std::cin >> A[i][j];
        }
    }

    // 读取每个机器人的概率分布
    std::vector<std::vector<double>> p(n, std::vector<double>(3));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 3; ++j) {
            std::cin >> p[i][j];
        }
    }

    // 计算积分结果
    double result = doubleIntegrate(A, p);
    // 输出结果，保留 6 位小数
    std::cout << std::fixed << std::setprecision(6) << result << std::endl;

    return 0;
}