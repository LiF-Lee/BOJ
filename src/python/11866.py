from sys import stdin, stdout
from collections import deque
n, k = map(int, stdin.readline().split())
que = deque()
for i in range(1,n+1):
    que.append(i)
stdout.write('<')
while que:
    for i in range(k - 1):
        que.append(que[0])
        que.popleft()
    stdout.write(str(que.popleft()))
    if que:
        stdout.write(', ')
stdout.write('>')