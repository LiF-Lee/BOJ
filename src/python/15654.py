from sys import stdin, stdout
from itertools import product
M, N = map(int, stdin.readline().split())
L = list(map(int, stdin.readline().split()))
L.sort()

for i in product(L, repeat=N):
    if len(i) == len(set(i)):
        print(' '.join(i))