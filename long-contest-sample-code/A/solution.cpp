#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<string> names = {"Alice", "Bob", "Cindy", "Dani"};
    vector<string> roster(3);
    for (int i = 0; i < 3; i++) {
        cin >> roster[i];
    }

    for(string& name: names) {
        if (find(roster.begin(), roster.end(), name) == roster.end()) {
            cout << name << endl;
            break;
        }
    }

    return 0;
}