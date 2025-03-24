#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int gcd(int a, int b) {
    a = abs(a);
    b = abs(b);
    while (b != 0) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }
    
    vector<int> nonZeroElements;
    for (int num : A) {
        if (num != 0) {
            nonZeroElements.push_back(num);
        }
    }
    
    if (nonZeroElements.empty()) {
        cout << 0 << endl;
        return 0;
    }
    
    int currentGCD = abs(nonZeroElements[0]);
    for (size_t i = 1; i < nonZeroElements.size(); ++i) {
        currentGCD = gcd(currentGCD, nonZeroElements[i]);
    }
    
    cout << currentGCD << endl;
    return 0;
}