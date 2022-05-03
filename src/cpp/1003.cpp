#include <iostream>
#include <map>

using namespace std;

typedef std::map<char, char> BasePairMap;

// int fibonacci(int n) {
//     if (n == 0) {
//         printf("0");
//         return 0;
//     } else if (n == 1) {
//         printf("1");
//         return 1;
//     } else {
//         return fibonacci(n‐1) + fibonacci(n‐2);
//     }
// }

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int T;
    cin >> T;
    BasePairMap l;
    for (int i = 0; i < T; i++) {
        l[char(i)] = '0';
        l[char(i)] = '0';
    }
    cout << l['0'] << endl;
    cout << l['1'] << endl;
}