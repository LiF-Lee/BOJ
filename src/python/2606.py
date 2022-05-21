from sys import stdin, stdout
from collections import deque
MAX = int(stdin.readline())
N = int(stdin.readline())
visit = [-1 for _ in range(MAX + 1)]
D = {i + 1: [] for i in range(MAX)}
Q = deque([1])
visit[1] = 0
for _ in range(N):
    a, b = map(int, stdin.readline().split())
    D[a].append(b)
    D[b].append(a)
while Q:
    cur = Q.popleft()
    for next in D[cur]:
        if visit[next] == -1:
            visit[next] = 1
            Q.append(next)
print(visit.count(1))