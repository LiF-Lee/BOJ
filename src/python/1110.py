from sys import stdin, stdout
N = int(stdin.readline())
Q = (N % 10) * 10 + sum(map(int, str(N))) % 10
s = 1
while Q != N:
    s += 1
    Q = (Q % 10) * 10 + sum(map(int, str(Q))) % 10
print(s)