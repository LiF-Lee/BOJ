# [1/1] [1/2, 2/1] [3/1, 2/2, 1/3] [1/4, 2/3, 3/2, 4/1] [5/1, 4/2, 3/3, 2/4, 1/5]
from sys import stdin, stdout
import math
a = int(stdin.readline())
c = 0
for i in range(1, a + 1):
    c += i
    if a <= c:
        x1 = i - (c - a)
        x2 = i - x1 + 1
        if i % 2 == 0:
            stdout.write(f"{x1}/{x2}")
        else:
            stdout.write(f"{x2}/{x1}")
        break