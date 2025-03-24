TLE 2



```python
#include <bits/stdc++.h>
using namespace std;
 
const int INF = 0x3f3f3f3f;
 
// Precompute powers of 26 for lengths 0..5.
int pow26[6];
 
// dp[L][p]: For strings of length L (1≤L≤5) and each prefix length p (1≤p≤L),
// we store the minimum type among all strings that have that exact prefix.
vector<vector<vector<int>>> dp(6);
bool seen[6] = {false, false, false, false, false, false};
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    pow26[0] = 1;
    for (int i = 1; i <= 5; i++){
        pow26[i] = pow26[i-1] * 26;
    }
 
    // Initialize dp arrays for L = 1..5.
    for (int L = 1; L <= 5; L++){
        dp[L].resize(L + 1);
        for (int p = 1; p <= L; p++){
            dp[L][p].assign(pow26[p], INF);
        }
    }
 
    int q;
    cin >> q;
    unordered_map<string,int> bestForString;
    bestForString.reserve(q * 2);
 
    // Process each operation.
    while(q--){
        int op;
        cin >> op;
        if(op == 1){
            string s;
            int x;
            cin >> s >> x;
            // Only update if this type is better.
            if(bestForString.find(s) != bestForString.end()){
                if(x >= bestForString[s])
                    continue;
            }
            bestForString[s] = x;
            int L = s.size();
            seen[L] = true;
            int code = 0;
            for (int p = 1; p <= L; p++){
                code = code * 26 + (s[p-1]-'a');
                dp[L][p][code] = min(dp[L][p][code], x);
            }
        } else {
            string s;
            cin >> s;
            int bestGlobalSim = -1, bestGlobalType = INF;
            // Try each group L (strings of length 1..5) that has been inserted.
            for (int L = 1; L <= 5; L++){
                if(!seen[L]) continue;
                // For group L, only the first m = min(L, |s|) positions count.
                int m = min(L, (int)s.size());
                int bestMismatch = m + 1; // smaller mismatches => higher similarity
                int bestType = INF;
                // DFS that builds the m-length code and counts mismatches.
                function<void(int,int,int)> dfs = [&](int pos, int mismatches, int code) {
                    if(pos == m){
                        if(dp[L][m][code] < INF){
                            if(mismatches < bestMismatch){
                                bestMismatch = mismatches;
                                bestType = dp[L][m][code];
                            } else if(mismatches == bestMismatch){
                                bestType = min(bestType, dp[L][m][code]);
                            }
                        }
                        return;
                    }
                    if(mismatches > bestMismatch) return;
                    int curLetter = s[pos]-'a';
                    // Try matching branch first.
                    dfs(pos+1, mismatches, code * 26 + curLetter);
                    // Then try non-matching branches.
                    if(mismatches < bestMismatch){
                        for (int letter = 0; letter < 26; letter++){
                            if(letter == curLetter) continue;
                            dfs(pos+1, mismatches+1, code * 26 + letter);
                        }
                    }
                };
                dfs(0, 0, 0);
                if(bestMismatch <= m){
                    int sim = m - bestMismatch;
                    if(sim > bestGlobalSim){
                        bestGlobalSim = sim;
                        bestGlobalType = bestType;
                    } else if(sim == bestGlobalSim){
                        bestGlobalType = min(bestGlobalType, bestType);
                    }
                }
            }
            cout << bestGlobalType << "\n";
        }
    }
    return 0;
}

```

