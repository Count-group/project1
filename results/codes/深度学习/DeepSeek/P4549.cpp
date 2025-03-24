#include <iostream>
#include <vector>
#include <cmath>  // 用于 abs 函数

using namespace std;

// 自定义实现 GCD 函数（欧几里得算法）
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return abs(a); // 保证返回值为非负
}

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }
    
    // 计算所有元素的绝对值与初始值的 GCD
    int g = 0;
    for (int num : A) {
        g = gcd(g, abs(num)); // 每次计算当前 GCD 和元素的绝对值
    }
    
    cout << g << endl;
    return 0;
}