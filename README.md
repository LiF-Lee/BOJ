# BOJ Preset


## Python3

``` python
import sys
a = int(sys.stdin.readline())
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
```

## C++

``` cpp
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int a;
    cin >> a;
    for (int i = 0; i < a; i++) {
        int b, c;
        cin >> b >> c;
    }
}
```