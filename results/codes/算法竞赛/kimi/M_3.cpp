#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int MAX_N = 1000000; // Maximum value of n
    vector<bool> light_state(MAX_N + 1, false); // Initialize all lights as off

    // Precompute the final state of each light
    for (int i = 1; i <= MAX_N; ++i) {
        for (int j = i; j <= MAX_N; j += i) {
            light_state[j] = !light_state[j]; // Toggle the state of light j
        }
    }

    int T;
    cin >> T;
    while (T--) {
        int n, k;
        cin >> n >> k;
        if (light_state[k]) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}