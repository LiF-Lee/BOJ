from sys import stdin, stdout
from collections import deque
N, M = map(int, stdin.readline().split())
MAP = [list(stdin.readline().rstrip()) for _ in range(M)]
visit = [[False] * N for _ in range(M)]
d = {'W': 0, 'B': 0}
for i in range(M):
    for j in range(N):
        if not visit[i][j]:
            count = 1
            q = deque()
            q.append((i, j))
            visit[i][j] = True
            while q:
                x, y = q.popleft()
                for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= dx < M and 0 <= dy < N and MAP[x][y] == MAP[dx][dy] and not visit[dx][dy]:
                        count += 1
                        q.append((dx, dy))
                        visit[dx][dy] = True
            d[MAP[i][j]] += count ** 2
print(d['W'], d['B'])