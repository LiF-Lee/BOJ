from sys import stdin, stdout
from collections import deque
N = int(stdin.readline())
L = deque()
for _ in range(N):
    cmd = stdin.readline().rstrip()
    if cmd == 'front':
        if len(L) == 0:
            print(-1)
        else:
            print(L[0])
    elif cmd == 'back':
        if len(L) == 0:
            print(-1)
        else:
            print(L[-1])
    elif cmd == 'size':
        print(len(L))
    elif cmd == 'empty':
        if len(L) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'pop':
        if len(L) == 0:
            print(-1)
        else:
            print(L.popleft())
    else:
        L.append(int(cmd.split()[1]))