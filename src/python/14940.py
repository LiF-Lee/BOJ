from sys import stdin, stdout
from collections import deque
n, m = map(int, stdin.readline().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
MAP_distance = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if MAP[i][j] == 0:
            MAP_distance[i][j] = 0
            continue
        MAP_visit = [[0] * m for _ in range(n)]
        MAP_deque = deque([(i, j)])
        while MAP_deque:
            x, y = MAP_deque.popleft()
            if MAP[x][y] == 2:
                MAP_distance[i][j] = MAP_visit[x][y]
                break
            for r, c in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
                if 0 <= r < n and 0 <= c < m and MAP[r][c] != 0 and MAP_visit[r][c] == 0:
                    MAP_visit[r][c] = MAP_visit[x][y] + 1
                    MAP_deque.append((r, c))
for k in range(n):
    for l in range(m):
        stdout.write(f"{MAP_distance[k][l]} ")
    stdout.write('\n')