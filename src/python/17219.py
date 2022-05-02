from sys import stdin, stdout
N, M = map(int, stdin.readline().split())
L = {}
for _ in range(N):
    site = stdin.readline().strip().split()
    L[site[0]] = site[1]
for _ in range(M):
    site = stdin.readline().strip()
    stdout.write(L[site] + '\n')