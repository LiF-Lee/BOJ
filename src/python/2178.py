from sys import stdin, stdout
from collections import deque
N, M = map(int, stdin.readline().split())
target = (N - 1, M - 1)
maze_map = [[i for i in stdin.readline().rstrip()] for _ in range(N)]
maze_map_visit = [[0 for _ in range(M)] for _ in range(N)]
maze_map_visit[0][0] = 1
Q = deque([(0, 0)])

while Q:
    x, y = Q.popleft()
    if (x, y) == target:
        stdout.write(f"{maze_map_visit[x][y]}")
        break
    for i in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= i[0] < N and 0 <= i[1] < M:
            if maze_map_visit[i[0]][i[1]] == 0 and maze_map[i[0]][i[1]] == '1':
                Q.append((i[0], i[1]))
                maze_map_visit[i[0]][i[1]] = maze_map_visit[x][y] + 1