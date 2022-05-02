import math
from sys import stdin, stdout
a = int(stdin.readline())
count = 0
for i in str(math.factorial(a))[::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)