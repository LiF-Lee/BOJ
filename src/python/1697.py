from sys import stdin, stdout
from collections import deque

N, K = map(int, stdin.readline().split())

MAX = 100_000
L = deque([0 for _ in range(MAX + 1)]) # 몇 번쨰 방문인지 확인하는 배열
Q = deque([N]) # 방문할 노드를 저장하는 큐

while L:
    R = Q.popleft()
    if R == K:
        stdout.write(F"{L[R]}")
        break
    for i in [R - 1, R + 1, R * 2]:
        if 0 <= i and i <= MAX and L[i] == 0: # 방문하지 않은 노드일때
            L[i] = L[R] + 1
            Q.append(i)