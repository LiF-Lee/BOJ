from sys import stdin, stdout
a, b = map(str, stdin.readline().split())
print(int(str(int(a[::-1]) + int(b[::-1]))[::-1]))