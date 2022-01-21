#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;
typedef long long LL;
int main() {
    int n; cin >> n;
    LL h, k; cin >> h >> k;
    
    LL farthest = 0;
    for (int i = 0; i < n; i++) {
        LL x, y; cin >> x >> y;
        farthest = max(farthest, (x - h)*(x - h) + (y - k)*(y - k));
    }

    cout << fixed << setprecision(20) << 2 * sqrt(farthest) << endl; 
    return 0;
}