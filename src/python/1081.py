from sys import stdin, stdout
L, U = map(int, stdin.readline().split())
for i in range(L, U + 1):
    if i % 2 == 0:
        stdout.write(str(i) + '\n')