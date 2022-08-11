s = int(input())
n = 0
_n = 0
while _n <= s:
    n += 1
    _n += n
print(n - 1)