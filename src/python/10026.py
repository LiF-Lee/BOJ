from sys import stdin, stdout
from collections import deque
N = int(stdin.readline())
rgb_map = [[i for i in stdin.readline().rstrip()] for _ in range(N)]
rgb_map_visit = [[0 for _ in range(N)] for _ in range(N)]
rgb_map_rg_weakness_visit = [[0 for _ in range(N)] for _ in range(N)]

normal_area = 0
rg_weakness_area = 0

Q = deque()
Q_rg_weakness = deque()

for i in range(N):
    for j in range(N):
        rgb = [rgb_map[i][j]]
        if rgb_map_visit[i][j] == 0:
            normal_area += 1
            Q.append((i, j))
            rgb_map_visit[i][j] = normal_area
            while Q:
                x, y = Q.popleft()
                for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= p[0] < N and 0 <= p[1] < N:
                        if rgb_map_visit[p[0]][p[1]] == 0 and rgb_map[p[0]][p[1]] == rgb[0]:
                            Q.append((p[0], p[1]))
                            rgb_map_visit[p[0]][p[1]] = normal_area
        if rgb_map_rg_weakness_visit[i][j] == 0:
            rg_weakness_area += 1
            Q_rg_weakness.append((i, j))
            rgb_map_rg_weakness_visit[i][j] = rg_weakness_area
            if rgb[0] == 'R':
                rgb.append('G')
            elif rgb[0] == 'G':
                rgb.append('R')
            while Q_rg_weakness:
                x, y = Q_rg_weakness.popleft()
                for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= p[0] < N and 0 <= p[1] < N:                        
                        if rgb_map_rg_weakness_visit[p[0]][p[1]] == 0 and rgb_map[p[0]][p[1]] in rgb:
                            Q_rg_weakness.append((p[0], p[1]))
                            rgb_map_rg_weakness_visit[p[0]][p[1]] = rg_weakness_area
    
print(normal_area, rg_weakness_area)