from sys import stdin, stdout
from collections import deque
T = int(stdin.readline())

for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]
    farm_visit = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        y, x = map(int, stdin.readline().split())
        farm[x][y] = 1
    Q = deque()
    farm_count = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and farm_visit[i][j] == 0:
                farm_count += 1
                Q.append((i, j))
                farm_visit[i][j] = farm_count
                while Q:
                    x, y = Q.popleft()
                    for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if 0 <= p[0] < N and 0 <= p[1] < M:
                            if farm_visit[p[0]][p[1]] == 0 and farm[p[0]][p[1]] == 1:
                                Q.append((p[0], p[1]))
                                farm_visit[p[0]][p[1]] = farm_count
    print(farm_count)
