from sys import stdin, stdout
from itertools import combinations
M, N = map(int, stdin.readline().split())

comb = list(combinations([i for i in range(1, M + 1)], N))

for i in comb:
    print(' '.join(map(str, i)))