from sys import stdin, stdout
import heapq
L, R = [], []
for i in range(int(stdin.readline())):
    s = int(stdin.readline().rstrip())
    if s == 0:
        if len(L) == 0:
            R.append(0)
            continue
        R.append(heapq.heappop(L)[1])
    else:
        heapq.heappush(L, (abs(s), s))
print(*R, sep='\n')