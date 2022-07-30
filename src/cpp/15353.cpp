#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    string a, b, r;
    cin >> a >> b;
    int al = a.length(), bl = b.length(), an, bn, u = 0;
    while (al | bl) {
        if (al) an = a[(al--) - 1] - '0';
        else an = 0;
        if (bl) bn = b[(bl--) - 1] - '0';
        else bn = 0;
        if (an + bn + u >= 10) {
            if (!al && !bl) r = to_string(an + bn + u) + r;
            else r = to_string((an + bn + u) % 10) + r;
            u = 1;
        } else {
            r = to_string(an + bn + u) + r;
            u = 0;
        }
    }
    cout << r;
    return 0;
}