from sys import stdin, stdout
from itertools import permutations
M, N = map(int, stdin.readline().split())

for i in permutations([i for i in range(1, M + 1)], N):
    print(' '.join(map(str, i)))