#include <iostream>
using namespace std;

int Factorial(int n)
{
    if (n <= 1)
        return 1;
    return n * Factorial(n - 1);
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int a;
    cin >> a;
    cout << Factorial(a);
}