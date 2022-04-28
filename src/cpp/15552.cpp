#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int a, b, c;
	cin >> a;
	for (int i = 0; i < a; i++) {
        cin >> b >> c;
        cout << b + c << "\n";
    }
}