from sys import stdin, stdout
from collections import deque
M, N = map(int, stdin.readline().split())
MAP = []
Q = deque()
for i in range(N):
    _map = []
    m = list(map(int, stdin.readline().split()))
    for j in range(len(m)):
        _map.append(m[j])
        if m[j] == 1:
            Q.append((i, j))
    MAP.append(_map)
while Q:
    x, y = Q.popleft()
    for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= dx < N and 0 <= dy < M and MAP[dx][dy] == 0:
            MAP[dx][dy] = MAP[x][y] + 1
            Q.append((dx, dy))
r = 0
for i in MAP:
    if 0 in i:
        r = 0
        break
    r = max(r, max(i))
print(r - 1)