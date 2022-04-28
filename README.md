# BOJ Preset


## Python3

``` python
# 빠른 입력 받기
import sys
a = int(sys.stdin.readline())
```

``` python
# 빠른 입력 받기 (한 줄에 여러개, int)
import sys
a, b, c = map(int, sys.stdin.readline().split())
```

``` python
# 빠른 출력
import sys
sys.stdout.write("%s %s\n" % ("a", "b")) # a b
```

``` python
# n 줄을 입력 받고 배열에 저장
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(n)]
```

``` python
# 정렬 (람다 활용)
list = [[21, 'Junkyu'], [21, 'Dohyun'], [20, 'Sunyoung']]
list.sort(key=lambda x: x[0])
```

## C++

``` cpp
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int a;
    cin >> a;
}
```