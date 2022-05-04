#include <iostream>
using namespace std;

long long int a, b, c;
int result = 0;
long long int pow(long long int x, long long int m) {
 
    if (m == 0)
        return 1;
    else if (m == 1)
        return x;
    if (m % 2 > 0)
        return pow(x, m - 1)*x;
    long long int half = pow(x, m / 2);
    half %= c;
    return (half * half) % c;
}

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	long long int a, b, c;
	cin >> a >> b >> c;
    cout << pow(a, b) % c;
}