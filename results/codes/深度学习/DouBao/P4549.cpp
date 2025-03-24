#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

// 计算两个数的最大公约数
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return std::abs(a);
}

// 计算多个数的最大公约数
int multiGcd(const std::vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        if (num != 0) {
            if (result == 0) {
                result = std::abs(num);
            } else {
                result = gcd(result, num);
            }
        }
    }
    return result;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> A(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> A[i];
    }
    int minS = multiGcd(A);
    std::cout << minS << std::endl;
    return 0;
}    