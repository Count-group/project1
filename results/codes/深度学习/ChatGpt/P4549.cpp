#include <iostream>
#include <cstdlib> // 用于 abs 函数
using namespace std;

// 自定义实现 gcd 函数，使用欧几里得算法
int my_gcd(int a, int b) {
    a = abs(a);
    b = abs(b);
    while (b != 0) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int main(){
    int n;
    cin >> n;
    int g = 0; // 初始值设为0，保证 gcd(0, a) = |a|
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        g = my_gcd(g, a); // 累计计算 gcd
    }
    cout << g << endl;
    return 0;
}
