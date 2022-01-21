#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
const int INF = 1e9;
int main() {
    int n; cin >> n;
    string s; cin >> s;

    vector<char> flags = {'A', 'C'};
    map<char, vector<int>> ans;
    for (char flag : flags) {
        ans[flag] = vector<int>(n, INF);
    }

    for (int i = 0; i < n; i++) {
        if (find(flags.begin(), flags.end(), s[i]) != flags.end()) {
            ans[s[i]][i] = 0;

            for (int j = i+1; j < n; j++) {
                if (s[j] == '.') {
                    ans[s[i]][j] = min(ans[s[i]][j], j - i);
                } else {
                    break;
                }
            }
            for (int j = i-1; j >= 0; j--) {
                if (s[j] == '.') {
                    ans[s[i]][j] = min(ans[s[i]][j], i - j);
                } else {
                    break;
                }
            }
        }
    }

    for (char flag : flags) {
        for (int i = 0; i < n; i++) {
            if (i != 0) {
                cout << " ";
            }
            cout << (ans[flag][i] == INF ? -1 : ans[flag][i]);
        }
        cout << endl;
    }
    return 0;
}