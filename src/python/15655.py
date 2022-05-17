from sys import stdin, stdout
from itertools import combinations
M, N = map(int, stdin.readline().split())
L = list(map(int, stdin.readline().split()))
L.sort()

for i in combinations(L, N):
    print(' '.join(map(str, i)))