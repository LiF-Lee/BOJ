from sys import stdin, stdout
from collections import deque
M, N = map(int, stdin.readline().split())
list = deque([i for i in range(M, N + 1)])
for j in [2, 3, 5, 7]:
    for k in range(len(list)):
        if list[k] == 0:
            continue
        if list[k] not in [2, 3, 5, 7] and list[k] % j == 0:
            list[k] = 0
res = set(list)
for v in res:
    if v == 0 or v == 1:
        continue
    stdout.write(f"{v}\n")