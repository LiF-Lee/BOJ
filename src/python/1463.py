from sys import stdin, stdout
from collections import deque

N = int(stdin.readline())
MAX = 1_000_000
L = deque([0 for _ in range(MAX + 1)])
Q = deque([N])

while Q:
    x = Q.popleft()
    if x == 1:
        stdout.write(f"{L[x]}")
        break
    check = [x - 1]
    for j in [2, 3]:
        if x % j == 0:
            check.append(int(x / j))
    for i in check:
        if 0 <= i <= MAX and L[i] == 0:
            Q.append(i)
            L[i] = L[x] + 1