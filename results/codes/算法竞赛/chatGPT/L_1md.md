TLE 2



```python
#include <bits/stdc++.h>
using namespace std;
 
const int INF = 0x3f3f3f3f;
 
// Precompute powers of 26 for lengths 0..5.
int pow26[6];
 
// For each length L (1<=L<=5) and each prefix length p (1<=p<=L),
// dp[L][p] is an array (of size 26^p) that stores the minimum type among all strings of length L 
// that have that prefix.
vector<vector<vector<int>>> dp(6);
 
// For each length L, mark if any update has occurred.
bool seen[6] = {false, false, false, false, false, false};
 
// Encode a string (of given length 'len') into an integer (base26).
int encodeStr(const string &s, int len) {
    int code = 0;
    for (int i = 0; i < len; i++) {
        code = code * 26 + (s[i] - 'a');
    }
    return code;
}
 
// Main
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    pow26[0] = 1;
    for (int i = 1; i < 6; i++){
        pow26[i] = pow26[i-1] * 26;
    }
 
    int q;
    cin >> q;
 
    // Initialize dp arrays for L = 1..5.
    dp[0].resize(0);
    for (int L = 1; L <= 5; L++){
        dp[L].resize(L + 1);
        for (int p = 1; p <= L; p++){
            dp[L][p].assign(pow26[p], INF);
        }
    }
 
    // Maintain a map for each full string to record its current (minimum) type.
    unordered_map<string, int> bestForString;
    bestForString.reserve(q * 2);
 
    // Process each operation.
    for (int op_i = 0; op_i < q; op_i++){
        int t;
        cin >> t;
        if(t == 1){
            string s;
            int x;
            cin >> s >> x;
            // If s already exists, update only if new type is smaller.
            if(bestForString.find(s) != bestForString.end()){
                if(x >= bestForString[s]) continue;
            }
            bestForString[s] = x;
            int L = s.size();
            seen[L] = true;
            // Update all prefixes of s.
            for (int p = 1; p <= L; p++){
                int code = encodeStr(s, p);
                dp[L][p][code] = min(dp[L][p][code], x);
            }
        } else if(t == 2){
            string s;
            cin >> s;
            // Global answer: choose the candidate with maximum similarity,
            // and if tie, the one with the smallest type.
            int global_bestScore = -1;
            int global_bestType = INF;
 
            // Check each group L = 1..5.
            for (int L = 1; L <= 5; L++){
                if(!seen[L]) continue;
                // Compare only up to min(|s|, L) characters.
                int m = min((int)s.size(), L);
                string qPrefix = s.substr(0, m);
 
                int bestScoreForGroup = -1;
                int bestTypeForGroup = INF;
                bool foundGroup = false;
 
                // For a given group, try all possible modifications of qPrefix.
                // d = number of positions in [0, m-1] where the candidate differs from qPrefix.
                // Similarity will be m - d.
                for (int d = 0; d <= m; d++){
                    int localBest = INF;
                    // Recursive lambda to enumerate all candidates that differ in exactly d positions.
                    function<void(int, int, int)> rec = [&](int pos, int diffCount, int curCode) {
                        if(pos == m){
                            if(diffCount == d){
                                localBest = min(localBest, dp[L][m][curCode]);
                            }
                            return;
                        }
                        if((m - pos) < (d - diffCount)) return;
                        // Option 1: no change at this position.
                        int letter = qPrefix[pos] - 'a';
                        rec(pos + 1, diffCount, curCode * 26 + letter);
                        // Option 2: if we still need to differ, try all other letters.
                        if(diffCount < d){
                            for (int alt = 0; alt < 26; alt++){
                                if(alt == letter) continue;
                                rec(pos + 1, diffCount + 1, curCode * 26 + alt);
                            }
                        }
                    };
                    rec(0, 0, 0);
 
                    if(localBest < INF){
                        int score = m - d; // similarity score for group L.
                        bestScoreForGroup = score;
                        bestTypeForGroup = localBest;
                        foundGroup = true;
                        break; // Found best candidate (with smallest d) in this group.
                    }
                }
 
                if(foundGroup){
                    if(bestScoreForGroup > global_bestScore){
                        global_bestScore = bestScoreForGroup;
                        global_bestType = bestTypeForGroup;
                    } else if(bestScoreForGroup == global_bestScore){
                        global_bestType = min(global_bestType, bestTypeForGroup);
                    }
                }
            }
            cout << global_bestType << "\n";
        }
    }
    return 0;
}

```

