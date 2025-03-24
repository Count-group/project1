#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<int> findNextGreater(const vector<int>& arr) {
    int n = arr.size();
    vector<int> result(n, 0);
    stack<int> st;

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && arr[st.top()] < arr[i]) {
            result[st.top()] = i + 1;
            st.pop();
        }
        st.push(i);
    }

    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    vector<int> ans = findNextGreater(arr);
    for (int i = 0; i < n; ++i) {
        if (i > 0) {
            cout << " ";
        }
        cout << ans[i];
    }
    cout << endl;

    return 0;
}    