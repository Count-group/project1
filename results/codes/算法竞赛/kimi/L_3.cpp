#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

// Function to calculate the similarity between two strings
int calculateSimilarity(const string& s1, const string& s2) {
    int similarity = 0;
    int minLen = min(s1.size(), s2.size());
    for (int i = 0; i < minLen; ++i) {
        if (s1[i] == s2[i]) {
            similarity++;
        }
    }
    return similarity;
}

int main() {
    int q;
    cin >> q;
    unordered_map<string, int> rubbishType; // Stores the type of each rubbish name
    vector<pair<string, int>> knownRubbish; // Stores all known rubbish names and their types

    while (q--) {
        int op;
        cin >> op;
        if (op == 1) {
            string s;
            int x;
            cin >> s >> x;
            // Update the type in the map
            if (rubbishType.find(s) == rubbishType.end() || x < rubbishType[s]) {
                rubbishType[s] = x;
            }
            // Add the new rubbish name and type to the list
            knownRubbish.push_back({s, x});
        } else if (op == 2) {
            string s;
            cin >> s;
            int maxSimilarity = -1;
            int minType = -1;

            // Check all known rubbish names to find the one with maximum similarity
            for (const auto& [knownName, knownType] : knownRubbish) {
                int similarity = calculateSimilarity(s, knownName);
                if (similarity > maxSimilarity || (similarity == maxSimilarity && knownType < minType)) {
                    maxSimilarity = similarity;
                    minType = knownType;
                }
            }

            // Output the type of the rubbish with maximum similarity
            cout << minType << endl;
        }
    }

    return 0;
}