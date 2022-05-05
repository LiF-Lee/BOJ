from sys import stdin, stdout
from collections import deque
a = int(stdin.readline())
target = deque([int(stdin.readline()) for _ in range(a)])
current = deque()
result = deque()

count = 0
status = True
for i in range(a):
    while count < target[i]:
      count += 1
      current.append(count)
      result.append('+')
    if current[-1] == target[i]:
        current.pop()
        result.append('-')
    else:
        status = False
        break
    
if status:
    print('\n'.join(result))
else:
    print('NO')
