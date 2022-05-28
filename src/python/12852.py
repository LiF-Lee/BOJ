from sys import stdin, stdout
from collections import deque

N = int(stdin.readline())

MAX = N
L = deque([-1 for _ in range(MAX + 1)])
M = deque([-1 for _ in range(MAX + 1)])
Q = deque([N])

L[N] = 0

while Q:
    x = Q.popleft()
    if x == N:
        stdout.write(f"{L[x]}\n")
        c = x
        r = []
        for _ in range(L[x] + 1):
            r.append(str(c))
            c = M[c]
        stdout.write(f"{' '.join(r[::-1])}\n")
        break
    for i in [x - 1, x / 2, x / 3]:
        if int(i) == i and 0 <= i <= MAX and L[i] == -1:
            M[i] = x
            Q.append(i)
            L[i] = L[x] + 1