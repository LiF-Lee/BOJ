from sys import stdin, stdout
from collections import deque
n, m = map(int, stdin.readline().split())
MAP_MAX_distance = 0
MAP = [list(stdin.readline().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if MAP[i][j] == 'L':
            MAP_distance = [[-1] * m for _ in range(n)]
            MAP_deque = deque([(i, j)])
            MAP_distance[i][j] = 0
            while MAP_deque:
                x, y = MAP_deque.popleft()
                for r, c in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
                    if 0 <= r < n and 0 <= c < m and MAP[r][c] == 'L' and MAP_distance[r][c] == -1:
                        MAP_deque.append((r, c))
                        MAP_distance[r][c] = MAP_distance[x][y] + 1 
                        MAP_MAX_distance = max(MAP_MAX_distance, MAP_distance[r][c])
print(MAP_MAX_distance)