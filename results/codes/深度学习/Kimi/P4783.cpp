#include <iostream>
#include <vector>
using namespace std;

const int mod = 1000000007;

long long pow_mod(long long a, long long b, long long mod) {
    long long res = 1;
    a %= mod;
    while (b > 0) {
        if (b % 2 == 1) {
            res = (res * a) % mod;
        }
        a = (a * a) % mod;
        b /= 2;
    }
    return res;
}

int main() {
    int n;
    cin >> n;

    vector<vector<long long>> aug(n, vector<long long>(2 * n, 0));

    // 读取原矩阵并初始化增广矩阵的左边部分
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> aug[i][j];
        }
    }

    // 初始化增广矩阵的右边部分为单位矩阵
    for (int i = 0; i < n; i++) {
        aug[i][i + n] = 1;
    }

    bool invertible = true;

    for (int col = 0; col < n; col++) {
        // 寻找当前列的主元所在的行
        int pivot_row = -1;
        for (int row = col; row < n; row++) {
            if (aug[row][col] != 0) {
                pivot_row = row;
                break;
            }
        }

        if (pivot_row == -1) {
            invertible = false;
            break;
        }

        // 交换当前行和主元所在的行
        swap(aug[col], aug[pivot_row]);

        // 计算主元的逆元
        long long pivot = aug[col][col];
        long long inv_pivot = pow_mod(pivot, mod - 2, mod);

        // 将当前行乘以逆元，使得主元变为1
        for (int j = 0; j < 2 * n; j++) {
            aug[col][j] = aug[col][j] * inv_pivot % mod;
        }

        // 消去其他行的当前列元素
        for (int row = 0; row < n; row++) {
            if (row != col) {
                long long factor = aug[row][col];
                if (factor != 0) {
                    for (int j = 0; j < 2 * n; j++) {
                        aug[row][j] = (aug[row][j] - factor * aug[col][j]) % mod;
                        if (aug[row][j] < 0) {
                            aug[row][j] += mod;
                        }
                    }
                }
            }
        }
    }

    if (!invertible) {
        cout << "No Solution" << endl;
    } else {
        // 输出逆矩阵的右边部分
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << aug[i][j + n] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}