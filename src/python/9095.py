from sys import stdin, stdout
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    Q = deque([n])
    sv = 0
    while Q:
        s = Q.popleft()
        if s == 0:
            sv += 1
            continue
        for i in [s - 1, s - 2, s - 3]:
            if i >= 0:
                Q.append(i)
    print(sv)