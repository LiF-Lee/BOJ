from sys import stdin, stdout
from collections import deque

N, K = map(int, stdin.readline().split())

MAX = 100_000
L = deque([[-1, 0] for _ in range(MAX + 1)])
Q = deque([N])

L[N][0] = 0
L[N][1] = 1

while Q:
    x = Q.popleft()
    for i in [x - 1, x + 1, x * 2]:
        if 0 <= i <= MAX:
            if L[i][0] == -1:
                L[i][0] = L[x][0] + 1
                L[i][1] += L[x][1]
                Q.append(i)
            elif L[i][0] == L[x][0] + 1:
                L[i][1] += L[x][1]

print(L[K][0])
print(L[K][1])