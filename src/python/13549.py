from sys import stdin, stdout
from collections import deque

N, K = map(int, stdin.readline().split())

MAX = 100_000
L = deque([0 for _ in range(MAX + 1)])
Q = deque([N])

while L:
    R = Q.popleft()
    if R == K:
        if L[R] == -1:
            stdout.write('0')
        else:
            stdout.write(F"{L[R]}")
        break
    for i in [2 * R]:
        if 0 <= i and i <= MAX and L[i] == 0:
            if L[R] == 0:
                L[i] = -1
            else:
                L[i] = L[R]
            Q.append(i)
    for i in [R - 1, R + 1]:
        if 0 <= i and i <= MAX and L[i] == 0:
            if L[R] == -1:
                L[i] = 0 + 1
            else:
                L[i] = L[R] + 1
            Q.append(i)