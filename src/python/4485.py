from sys import stdin, stdout
from collections import deque
while True:
    n = int(input())
    if n == 0:
        break
    _map = [list(map(int, stdin.readline().split())) for _ in range(n)]
    _map_d = [[0] * n for _ in range(n)]
    q = deque()
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        