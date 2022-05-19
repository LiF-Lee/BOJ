from sys import stdin, stdout
from collections import deque
F, S, G, U, D = map(int, stdin.readline().split())
max_floor = F
visit = [-1 for _ in range(max_floor + 1)]
Q = deque([S])
visit[S] = 0

min_press = -1

while Q:
    x = Q.popleft()
    if x == G:
        min_press = visit[x]
        break
    for i in [x + U, x - D]:
        if 1 <= i <= max_floor and visit[i] == -1:
            visit[i] = visit[x] + 1
            Q.append(i)

if min_press == -1:
    print('use the stairs')
else:
    print(min_press)