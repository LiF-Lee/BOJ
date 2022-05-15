from re import S
from sys import stdin, stdout
while True:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        break
    if a > b:
        print('Yes')
    else:
        print('No')