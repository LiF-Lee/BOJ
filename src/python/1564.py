from sys import stdin, stdout
from math import factorial
a = int(stdin.readline())
sv = 1
for i in range(2, a + 1):
    sv *= i
    while sv % 10 == 0:
        sv //= 10
    sv %= 1_000_000_000_000
print(str(sv)[-5:])