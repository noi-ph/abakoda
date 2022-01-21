#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n; cin >> n;
    vector<int> x(n), c(n);
    for (int i = 0; i < n; i++) {
        cin >> x[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }
    sort(c.begin(), c.end());

    bool all = true;
    for (int i = 0; i < n; i++) {
        if (!(x[i] <= c[i])) {
            all = false;
            break;
        }
    }
    cout << (all ? "YES" : "NO") << endl;

    return 0;
}