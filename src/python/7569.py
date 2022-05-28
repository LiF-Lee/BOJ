from sys import stdin, stdout
from collections import deque
M, N, H = map(int, stdin.readline().split())
MAP = []
Q = deque()
for k in range(H):
    _map = []
    for i in range(N):
        __map = []
        m = list(map(int, stdin.readline().split()))
        for j in range(len(m)):
            __map.append(m[j])
            if m[j] == 1:
                Q.append((i, j, k))
        _map.append(__map)
    MAP.append(_map)
while Q:
    x, y, h = Q.popleft()
    for dx, dy, dh in [(x - 1, y, h), (x + 1, y, h), (x, y - 1, h), (x, y + 1, h), (x, y, h - 1), (x, y, h + 1)]:
        if 0 <= dx < N and 0 <= dy < M and 0 <= dh <= H - 1 and MAP[dh][dx][dy] == 0:
            MAP[dh][dx][dy] = MAP[h][x][y] + 1
            Q.append((dx, dy, dh))
r = 0
for i in MAP:
    for j in i:
        if 0 in j:
            r = 0
            break
        r = max(r, max(j))
    if r == 0:
        break
print(r - 1)