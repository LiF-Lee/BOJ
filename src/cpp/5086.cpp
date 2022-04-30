#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    while (true)
    {
        int a, b;
        cin >> a >> b;
        if (a == 0 && b == 0)
            break;
        if (b % a == 0)
            cout << "factor\n";
        else if (a % b == 0)
            cout << "multiple\n";
        else
            cout << "neither\n";
    }
}