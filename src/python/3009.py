from sys import stdin, stdout
x1, y1 = map(int, stdin.readline().split())
x2, y2 = map(int, stdin.readline().split())
x3, y3 = map(int, stdin.readline().split())

print(x1 ^ x2 ^ x3, y1 ^ y2 ^ y3)