from sys import stdin, stdout
N = int(stdin.readline())
for _ in range(N):
    L = stdin.readline().rstrip()
    print(L[0], L[-1], sep='')