#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n; cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    sort(A.begin(), A.end());

    int done = 0;
    for (int val : A) {
        if (val <= done) {
            done++;
        } else {
            break;
        }
    }
    cout << done << endl;

    return 0;
}