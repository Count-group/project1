#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

// 快速幂求 a^b mod mod
ll modExp(ll a, ll b, ll mod) {
    ll result = 1;
    a %= mod;
    while(b > 0) {
        if(b & 1) result = (result * a) % mod;
        a = (a * a) % mod;
        b >>= 1;
    }
    return result;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    // 构造增广矩阵：左边是输入矩阵，右边是单位阵
    vector<vector<ll>> mat(n, vector<ll>(2*n, 0));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> mat[i][j];
            mat[i][j] %= MOD;
        }
    }
    for (int i = 0; i < n; i++){
        mat[i][n+i] = 1;
    }

    // 高斯消元
    for (int i = 0; i < n; i++){
        // 寻找主元
        int pivot = i;
        while(pivot < n && mat[pivot][i] == 0)
            pivot++;
        if(pivot == n){
            cout << "No Solution" << "\n";
            return 0;
        }
        // 若 pivot 行不等于当前行，则交换
        if(pivot != i)
            swap(mat[i], mat[pivot]);
        
        // 将主元化为 1：乘以逆元
        ll inv = modExp(mat[i][i], MOD - 2, MOD);
        for (int j = 0; j < 2*n; j++){
            mat[i][j] = (mat[i][j] * inv) % MOD;
        }
        // 消去其他行中第 i 列的元素
        for (int j = 0; j < n; j++){
            if(j == i) continue;
            ll factor = mat[j][i];
            if(factor != 0){
                for (int k = 0; k < 2*n; k++){
                    mat[j][k] = (mat[j][k] - factor * mat[i][k]) % MOD;
                    if(mat[j][k] < 0) mat[j][k] += MOD;
                }
            }
        }
    }
    
    // 输出逆矩阵：增广矩阵的右半部分
    for (int i = 0; i < n; i++){
        for (int j = n; j < 2*n; j++){
            cout << mat[i][j] << (j == 2*n-1 ? "\n" : " ");
        }
    }
    return 0;
}
