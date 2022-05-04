from sys import stdin, stdout
a, b = map(int, stdin.readline().split())
if a < b:
    print((a + b) * (b - a + 1) // 2)
else:
    print((b + a) * (a - b + 1) // 2)
