#include <iostream>
#include <vector>
using namespace std;
using ll = long long;
const ll MOD = 998244353;

// 快速幂求 a^b mod mod
ll modexp(ll a, ll b, ll mod) {
    ll res = 1;
    a %= mod;
    while(b > 0) {
        if(b & 1) res = (res * a) % mod;
        a = (a * a) % mod;
        b >>= 1;
    }
    return res;
}

// 求 a 在 mod 意义下的逆元（mod 为素数）
ll modinv(ll a, ll mod) {
    return modexp(a, mod - 2, mod);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    ll k;
    cin >> n >> k;
    vector<ll> x(n), y(n);
    for(int i = 0; i < n; i++){
        cin >> x[i] >> y[i];
    }
    
    // 如果 k 恰好等于某个已知点的横坐标，则 f(k)=y_i
    for(int i = 0; i < n; i++){
        if(x[i] == k) {
            cout << ( (y[i] % MOD + MOD) % MOD ) << "\n";
            return 0;
        }
    }
    
    // 计算 G = ∏(k - x[i])
    ll G = 1;
    for (int i = 0; i < n; i++){
        ll diff = ( (k - x[i]) % MOD + MOD ) % MOD;
        G = (G * diff) % MOD;
    }
    
    ll ans = 0;
    // 对每个点使用拉格朗日插值公式求贡献
    for (int i = 0; i < n; i++){
        // 分子部分：G/(k-x[i])
        ll invDiff = modinv(( (k - x[i]) % MOD + MOD ) % MOD, MOD);
        ll numerator = (G * invDiff) % MOD;
        
        // 分母部分：∏_{j≠i}(x[i]-x[j])
        ll denom = 1;
        for (int j = 0; j < n; j++){
            if(i == j) continue;
            ll diff = ( (x[i] - x[j]) % MOD + MOD ) % MOD;
            denom = (denom * diff) % MOD;
        }
        
        // 当前点的贡献： y[i] * (G/(k-x[i])) * inv(∏_{j≠i}(x[i]-x[j]))
        ll term = y[i] % MOD;
        term = (term * numerator) % MOD;
        term = (term * modinv(denom, MOD)) % MOD;
        ans = (ans + term) % MOD;
    }
    
    cout << ( (ans % MOD + MOD) % MOD ) << "\n";
    return 0;
}
