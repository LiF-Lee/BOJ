#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int l[26] = {0};
    string s; cin >> s;
    for (int i = 0; i < s.size(); i++) {
        l[s[i] - 97]++;
    }
    for (int i = 0; i < 26; i++) {
        cout << l[i] << " ";
    }
}