#include <iostream>
using namespace std;

int main() {
    unsigned int a, b, p;
    cin >> a >> b >> p;
    
    // 保存原始输入，用于最后的输出格式
    unsigned int origA = a, origB = b, origP = p;
    
    unsigned long long result = 1;  // 使用 64 位保存中间计算结果
    a %= p;
    
    // 快速幂算法计算 a^b mod p
    while(b > 0) {
        if(b & 1) {
            result = (result * a) % p;
        }
        // 注意：这里强制将 a 转换为 unsigned long long，防止 a*a 溢出
        a = (unsigned long long)a * a % p;
        b >>= 1;
    }
    
    cout << origA << "^" << origB << " mod " << origP << "=" << result;
    return 0;
}
