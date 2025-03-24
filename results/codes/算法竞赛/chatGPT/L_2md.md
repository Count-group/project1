TLE 2



```python
#include <bits/stdc++.h>
using namespace std;
 
const int INF = 0x3f3f3f3f;
 
// Maximum string length is 5. We use base‐26 encoding.
int pow26[6];
 
// dp[L][p]: For strings of length L (1≤L≤5), for each prefix length p (1≤p≤L)
// store the minimum type among strings having that exact prefix.
vector<vector<vector<int>>> dp(6);
 
// To mark if any string of length L has been inserted.
bool seen[6] = {false, false, false, false, false, false};
 
// Precomputed combinations: For each m (1≤m≤5) and each d (0≤d≤m),
// comb[m][d] is a list of all combinations (each a vector<int> of positions)
// of size d from positions 0 .. m-1.
vector<vector<vector<vector<int>>>> comb(6, vector<vector<vector<int>>>(6));
 
// Precompute all combinations for positions 0..m-1.
void precompute_combinations(){
    for (int m = 1; m <= 5; m++){
        for (int d = 0; d <= m; d++){
            vector<vector<int>> combos;
            vector<int> cur;
            function<void(int, int)> dfs = [&](int start, int left){
                if(left == 0){
                    combos.push_back(cur);
                    return;
                }
                for (int i = start; i < m; i++){
                    cur.push_back(i);
                    dfs(i+1, left-1);
                    cur.pop_back();
                }
            };
            dfs(0, d);
            comb[m][d] = move(combos);
        }
    }
}
 
// Encode the first p characters of string s into an integer (base26)
int encode(const string &s, int p){
    int code = 0;
    for (int i = 0; i < p; i++){
        code = code * 26 + (s[i] - 'a');
    }
    return code;
}
 
// For a given group of inserted strings of length L, we query the dp table for prefix length m
// (where m = min(L, |query|)) using the query code qcode.
// We want to find a candidate that minimizes the Hamming distance (i.e. maximizes similarity = m - d)
// and, in case of tie, has the smallest type.
pair<int,int> query_group(int L, int m, int qcode){
    // Try differences d from 0 to m.
    for (int d = 0; d <= m; d++){
        int bestCandidate = INF;
        // For each combination of d positions (in [0, m-1]) to change.
        for (auto &posList : comb[m][d]){
            function<void(int, int)> rec = [&](int idx, int curCode){
                if(idx == (int)posList.size()){
                    bestCandidate = min(bestCandidate, dp[L][m][curCode]);
                    return;
                }
                int pos = posList[idx];
                int orig = (qcode / pow26[m-1-pos]) % 26;
                for (int letter = 0; letter < 26; letter++){
                    if(letter == orig) continue;
                    int newCode = curCode + (letter - orig) * pow26[m-1-pos];
                    rec(idx+1, newCode);
                }
            };
            rec(0, qcode);
        }
        if(bestCandidate < INF){
            // Similarity = m - d.
            return {m - d, bestCandidate};
        }
    }
    return { -1, INF }; // Should not happen.
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    precompute_combinations();
    pow26[0] = 1;
    for (int i = 1; i <= 5; i++){
        pow26[i] = pow26[i-1] * 26;
    }
 
    int q;
    cin >> q;
 
    // Initialize dp arrays for L = 1 to 5.
    for (int L = 1; L <= 5; L++){
        dp[L].resize(L + 1);
        for (int p = 1; p <= L; p++){
            dp[L][p].assign(pow26[p], INF);
        }
    }
 
    // Store the best type for each full string.
    unordered_map<string, int> bestForString;
    bestForString.reserve(q * 2);
 
    while(q--){
        int t;
        cin >> t;
        if(t == 1){
            string s;
            int x;
            cin >> s >> x;
            if(bestForString.find(s) != bestForString.end()){
                if(x >= bestForString[s])
                    continue;
            }
            bestForString[s] = x;
            int L = s.size();
            seen[L] = true;
            int code = 0;
            for (int p = 1; p <= L; p++){
                code = code * 26 + (s[p-1] - 'a');
                dp[L][p][code] = min(dp[L][p][code], x);
            }
        } else {
            string s;
            cin >> s;
            int bestGlobalSim = -1, bestGlobalType = INF;
            int k = s.size();
            // Check each group L (strings of length L).
            for (int L = 1; L <= 5; L++){
                if(!seen[L]) continue;
                int m = min(L, k);
                int qcode = 0;
                for (int i = 0; i < m; i++){
                    qcode = qcode * 26 + (s[i] - 'a');
                }
                auto res = query_group(L, m, qcode);
                int sim = res.first, typeVal = res.second;
                if(sim > bestGlobalSim){
                    bestGlobalSim = sim;
                    bestGlobalType = typeVal;
                } else if(sim == bestGlobalSim){
                    bestGlobalType = min(bestGlobalType, typeVal);
                }
            }
            cout << bestGlobalType << "\n";
        }
    }
    return 0;
}

```

