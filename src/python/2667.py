from sys import stdin, stdout
from collections import deque
N = int(stdin.readline())
apart_map = [[i for i in stdin.readline().rstrip()] for _ in range(N)]
apart_map_visit = [[0 for _ in range(N)] for _ in range(N)]
Q = deque()
apart = 0
for i in range(N):
    for j in range(N):
        if apart_map[i][j] == '1' and apart_map_visit[i][j] == 0:
            apart += 1
            apart_map_visit[i][j] = apart
            Q.append((i, j))
            while Q:
                x, y = Q.popleft()
                for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= p[0] < N and 0 <= p[1] < N:
                        if apart_map_visit[p[0]][p[1]] == 0 and apart_map[p[0]][p[1]] == '1':
                            Q.append((p[0], p[1]))
                            apart_map_visit[p[0]][p[1]] = apart             
result_map = []
sort_result_map = []
for k in range(N):
    for l in range(N):
        if apart_map_visit[k][l] != 0:
            result_map.append(apart_map_visit[k][l])
for o in range(apart):
    sort_result_map.append(result_map.count(o + 1))
sort_result_map.sort()
print(apart)
for c in sort_result_map:
    print(c)