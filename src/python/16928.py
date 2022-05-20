from sys import stdin, stdout
from collections import deque
N, M = map(int, stdin.readline().split())
D = {}
for _ in range(N + M):
    x, y = map(int, stdin.readline().split())
    D[x] = y
MAX = 100
visit = [-1 for _ in range(MAX + 1)]
visit[1] = 0
Q = deque([1])
while Q:
    x = Q.popleft()
    if x == MAX:
        print(visit[x])
        break
    for i in range(x, x + 7):
        if 1 <= i <= MAX and visit[i] == -1:
            visit[i] = visit[x] + 1
            if i in D:
                if visit[D[i]] == -1:
                    visit[D[i]] = visit[x] + 1
                    Q.append(D[i])
            else:
                Q.append(i)