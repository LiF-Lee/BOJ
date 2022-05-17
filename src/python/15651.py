from sys import stdin, stdout
from itertools import product
M, N = map(int, stdin.readline().split())

for i in product([i for i in range(1, M + 1)], repeat=N):
    print(' '.join(map(str, i)))