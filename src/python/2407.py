from sys import stdin, stdout
import math
a, b = map(int, stdin.readline().split())
sv = 1
for i in range(a, a - b, -1):
    sv *= i
print(int(sv // math.factorial(b)))