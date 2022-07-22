from sys import stdin, stdout
from collections import deque
WALL, ROAD, TARGET = 0, 1, 2
n, m = map(int, stdin.readline().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
MAP_distance = [[-1] * m for _ in range(n)]
MAP_deque = deque()
for i in range(n):
    for j in range(m):
        if MAP[i][j] == WALL:
            MAP_distance[i][j] = 0
        elif MAP[i][j] == TARGET:
            MAP_distance[i][j] = 0
            for r, c in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                if 0 <= r < n and 0 <= c < m and MAP[r][c] == ROAD:
                    MAP_distance[r][c] = 1
                    MAP_deque.append((r, c))
while MAP_deque:
    x, y = MAP_deque.popleft()
    for r, c in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
        if 0 <= r < n and 0 <= c < m and MAP_distance[r][c] == -1:
            MAP_distance[r][c] = MAP_distance[x][y] + 1
            MAP_deque.append((r, c))
for i in range(n):
    for j in range(m):
        stdout.write(f"{MAP_distance[i][j]} ")
    stdout.write('\n')