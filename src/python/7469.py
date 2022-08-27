from sys import stdin, stdout
import heapq
n, m = map(int, stdin.readline().rstrip().split())
L = list(map(int, stdin.readline().rstrip().split()))
h, s, sorted_h = [], [], []
for i in range(n):
    heapq.heappush(h, (L[i], i))
w = 0
while h:
    v, o = heapq.heappop(h)
    heapq.heappush(s, (o, v, w))
    w += 1
while s:
    sorted_h.append(heapq.heappop(s))
for _ in range(m):
    _h = []
    i, j, k = map(int, stdin.readline().rstrip().split())
    for _, v, w in sorted_h[i-1:j]:
        heapq.heappush(_h, (w, v))
    for _ in range(k - 1):
        heapq.heappop(_h)
    stdout.write(f"{heapq.heappop(_h)[1]}\n")