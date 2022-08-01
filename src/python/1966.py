from sys import stdin, stdout
from collections import deque
import heapq
t = int(stdin.readline())
for _ in range(t):
    q = deque()
    priority = []
    n, m = map(int, stdin.readline().split())
    for idx, val in enumerate(map(int, stdin.readline().split())):
        q.append((idx, val))
        heapq.heappush(priority, (-val, val))
    c = 1
    while q:
        idx, val = q.popleft()
        if idx == m and val == priority[0][1]:
            stdout.write(f"{c}\n")
            break
        elif val == priority[0][1]:
            c += 1
            heapq.heappop(priority)
        else:
            q.append((idx, val))