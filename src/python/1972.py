from sys import stdin, stdout
import heapq
L = []
for i in range(int(stdin.readline())):
    a = int(stdin.readline())
    if a == 0:
        if len(L) == 0:
            print(0)
            continue
        print(heapq.heappop(L))
    else:
        heapq.heappush(L, a)