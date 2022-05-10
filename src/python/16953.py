from sys import stdin, stdout
from collections import deque
A, B = map(int, stdin.readline().split())

max_num = B
Q = deque([(A, 1)])
res = -1

while Q:
    x, cnt = Q.popleft()
    if x == B:
        res = cnt
        break
    for p in [x * 2, x * 10 + 1]:
        if 0 <= p <= max_num:
            Q.append((p, cnt + 1))

print(res)