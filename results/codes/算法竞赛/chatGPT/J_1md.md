Accepted



```python
#include <iostream>
#include <algorithm>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long a, b;
    cin >> a >> b;
    // We use the fact that a square with bottom‐left (x, y) is counted
    // if its center (x+0.5, y+0.5) lies inside the triangle with vertices 
    // (a,0), (0,b), (0,0). That is, if:
    //   b*(x+0.5) + a*(y+0.5) <= a*b.
    // Multiply both sides by 2:
    //   2b*x + 2a*y + (a+b) <= 2a*b.
    // Rearranging gives:
    //   y <= (2a*b - (a+b) - 2b*x) / (2a)
    // For x from 0 to a-1 and y from 0 to b-1.
    
    long long ans = 0;
    for (long long x = 0; x < a; x++){
        long long numerator = 2*a*b - (a + b) - 2*b*x;
        if(numerator < 0) break;
        long long y_max = numerator / (2*a); // floor division
        if(y_max >= b) y_max = b - 1;
        ans += (y_max + 1);
    }
    cout << ans << "\n";
    return 0;
}

```

