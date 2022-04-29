from sys import stdin, stdout
from collections import deque
a = int(stdin.readline())
que = deque([i for i in range(1, a + 1)])
while len(que) > 1:
    que.popleft()
    que.append(que.popleft())
print(que[0])
