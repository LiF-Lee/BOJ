# BOJ Preset


## Python3

``` python
# 빠른 입력 받기
from sys import stdin, stdout
a = int(stdin.readline())
```

``` python
# 빠른 입력 받기 (한 줄에 여러개, int)
from sys import stdin, stdout
a, b, c = map(int, stdin.readline().split())
```

``` python
# 빠른 출력
from sys import stdin, stdout
stdout.write(f"{a} {b}\n")
```

``` python
# for 인덱스와 값 동시 출력
from sys import stdin, stdout
list = []
for idx, val in enumerate(list):
    stdout.write(f"{idx} {val}\n")
```

``` python
# n 줄을 입력 받고 배열에 저장
from sys import stdin, stdout
n = int(stdin.readline())
data = [stdin.readline().strip() for _ in range(n)]
```

``` python
# 정렬 (람다 활용)
list = [[21, 'Junkyu'], [21, 'Dohyun'], [20, 'Sunyoung']]
list.sort(key=lambda x: x[0])
```

``` python
# 퀵 정렬
def Partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def Quick_Sort(array, low, high):
  if low < high:
    pi = Partition(array, low, high)
    Quick_Sort(array, low, pi - 1)
    Quick_Sort(array, pi + 1, high)
```

``` python
# 이분 탐색
def Binary_Search(array, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return Binary_Search(array, target, start, mid - 1)
    else:
        return Binary_Search(array, target, mid + 1, end)
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