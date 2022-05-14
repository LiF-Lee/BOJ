from sys import stdin, stdout
import math
_ = stdin.readline()
C = 0
A = 0
for i in stdin.readline().rstrip():
    if i == 'C':
        C += 1
    else:
        A += 1
print(math.ceil(C / (A + 1)))