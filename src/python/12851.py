from sys import stdin, stdout
from collections import deque

N, K = map(int, stdin.readline().split())

MAX = 100_000
L = deque([-1 for _ in range(MAX + 1)])
M = deque([-1 for _ in range(MAX + 1)])
Q = deque([N])

L[N] = 0

while Q:
    x = Q.popleft()
    if x == K:
        stdout.write(f"{L[x]}\n")
        c = x
        r = []
        for _ in range(L[x] + 1):
            r.append(str(c))
            c = M[c]
        stdout.write(f"{' '.join(r[::-1])}")
        break
    for i in [x - 1, x + 1, x * 2]:
        if 0 <= i <= MAX and L[i] == -1:
            M[i] = x
            Q.append(i)
            L[i] = L[x] + 1