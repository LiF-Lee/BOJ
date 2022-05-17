from sys import stdin, stdout
from itertools import permutations
M, N = map(int, stdin.readline().split())
L = [int(val + str(idx)) for idx, val in enumerate(stdin.readline().split())]
L.sort()

r = []

for i in permutations(L, N):
    v = ''
    for j in i:
        v += str(j)[0]
    r.append(int(v))

aL = list(set(r))
aL.sort()

for j in aL:
    a = list(str(j))
    print(' '.join(a))