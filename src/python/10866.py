from sys import stdin, stdout
from collections import deque
N = int(stdin.readline())
que = deque()
res = deque()

while N > 0:
    N -= 1
    cmd = stdin.readline().strip()
    if cmd.startswith('push_front'):
        que.appendleft(int(cmd.split()[1]))
        continue
    elif cmd.startswith('push_back'):
        que.append(int(cmd.split()[1]))
        continue
    elif cmd == 'pop_front':
        if len(que) == 0:
            res.append(f"{-1}")
        else:
            res.append(f"{que.popleft()}")
        continue
    elif cmd == 'pop_back':
        if len(que) == 0:
            res.append(f"{-1}")
        else:
            res.append(f"{que.pop()}")
        continue
    elif cmd == 'size':
        res.append(f"{len(que)}")
        continue
    elif cmd == 'empty':
        if len(que) == 0:
            res.append(f"{1}")
        else:
            res.append(f"{0}")
        continue
    elif cmd == 'front':
        if len(que) == 0:
            res.append(f"{-1}")
        else:
            res.append(f"{que[0]}")
        continue
    elif cmd == 'back':
        if len(que) == 0:
            res.append(f"{-1}")
        else:
            res.append(f"{que[-1]}")
        continue

stdout.write('\n'.join(res))