from sys import stdin, stdout
import heapq
N = int(stdin.readline())
L, R = [], []
for _ in range(N):
    num = int(stdin.readline())
    if len(L) == len(R):
        heapq.heappush(L, num * -1)
    else:
        heapq.heappush(R, num)
    if len(L) >= 1 and len(R) >= 1 and L[0] * -1 > R[0]:
        L_val = heapq.heappop(L) * -1
        R_val = heapq.heappop(R)
        heapq.heappush(L, R_val * -1)
        heapq.heappush(R, L_val)
    if len(L) == len(R):
        print(min(L[0] * -1, R[0]))
    else:
        print(L[0] * -1)