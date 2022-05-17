from sys import stdin, stdout
from itertools import combinations_with_replacement
M, N = map(int, stdin.readline().split())
L = list(map(int, stdin.readline().split()))
L.sort()

for i in combinations_with_replacement(L, N):
    print(' '.join(map(str, i)))