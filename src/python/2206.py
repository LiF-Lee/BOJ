from sys import stdin, stdout
from collections import deque
n, m = map(int, stdin.readline().split())
MAP = [list(stdin.readline().rstrip()) for _ in range(n)]
MAP_visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
MAP_visit[0][0][0] = 1
MAP_deque = deque([(0, 0, 0)])
MAP_MIN_distance = -1
while MAP_deque:
    x, y, breakable = MAP_deque.popleft()
    if x == n - 1 and y == m - 1:
        MAP_MIN_distance = MAP_visit[x][y][breakable]
        break
    for r, c in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
        if 0 <= r < n and 0 <= c < m:
            if MAP[r][c] == '1' and breakable == 0:
                MAP_visit[r][c][1] = MAP_visit[x][y][0] + 1
                MAP_deque.append((r, c, 1))
            elif MAP[r][c] == '0' and MAP_visit[r][c][breakable] == 0:
                MAP_visit[r][c][breakable] = MAP_visit[x][y][breakable] + 1
                MAP_deque.append((r, c, breakable))
stdout.write(f"{MAP_MIN_distance}")