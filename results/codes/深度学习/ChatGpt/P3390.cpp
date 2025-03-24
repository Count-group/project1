#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

// 矩阵乘法：计算 (A * B) mod MOD
vector<vector<ll>> multiply(const vector<vector<ll>> &A, const vector<vector<ll>> &B) {
    int n = A.size();
    vector<vector<ll>> C(n, vector<ll>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int k = 0; k < n; k++) {
            ll tmp = A[i][k];
            for (int j = 0; j < n; j++) {
                C[i][j] = (C[i][j] + tmp * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

// 矩阵快速幂，计算 A^exp
vector<vector<ll>> matrixPower(vector<vector<ll>> A, ll exp) {
    int n = A.size();
    // 单位矩阵
    vector<vector<ll>> res(n, vector<ll>(n, 0));
    for (int i = 0; i < n; i++) {
        res[i][i] = 1;
    }
    while(exp > 0) {
        if(exp & 1)
            res = multiply(res, A);
        A = multiply(A, A);
        exp >>= 1;
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    ll k;
    cin >> n >> k;
    
    vector<vector<ll>> A(n, vector<ll>(n));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> A[i][j];
            // 处理负数情况并取模
            A[i][j] %= MOD;
            if(A[i][j] < 0)
                A[i][j] += MOD;
        }
    }
    
    vector<vector<ll>> ans = matrixPower(A, k);
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }
    
    return 0;
}
