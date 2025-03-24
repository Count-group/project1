#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m, q;
    cin >> n >> m >> q;

    // Initialize the adjacency list
    vector<vector<int>> adj(n + 1);

    // Build the graph
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    // Initialize the number of cumulonimbus clouds above each building
    vector<int> clouds(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> clouds[i];
    }

    // Pre - calculate the sum of clouds for each vertex's neighbors
    vector<int> neighbor_cloud_sums(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        for (int neighbor : adj[i]) {
            neighbor_cloud_sums[i] += clouds[neighbor];
        }
    }

    // Process the events
    for (int i = 0; i < q; ++i) {
        int type;
        cin >> type;
        if (type == 1) {
            int x, v;
            cin >> x >> v;
            clouds[x] += v;
            for (int neighbor : adj[x]) {
                neighbor_cloud_sums[neighbor] += v;
            }
        } else {
            int x;
            cin >> x;
            cout << neighbor_cloud_sums[x] << endl;
        }
    }

    return 0;
}