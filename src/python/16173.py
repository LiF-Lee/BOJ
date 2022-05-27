from sys import stdin, stdout
from collections import deque
N = int(stdin.readline())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, stdin.readline().split())))
V = [[0] * N for _ in range(N)]
V[0][0] = 1
Q = deque([(0, 0)])
FOUND = False
while Q:
    x, y = Q.popleft()
    if x == N - 1 and y == N - 1:
        FOUND = True
        break
    for dx, dy in ((x, y + MAP[x][y]), (x + MAP[x][y], y)):
        if 0 <= dx < N and 0 <= dy < N and V[dx][dy] == 0:
            V[dx][dy] = V[x][y] + 1
            Q.append((dx, dy))
stdout.write('HaruHaru' if FOUND else 'Hing')