from sys import stdin, stdout
from collections import deque

N, K = map(int, stdin.readline().split())

MAX = 100_000
L = deque([0 for _ in range(MAX + 1)])
Q = deque([N])

count = 0
shortest = -1

while Q:
    x = Q.popleft()
    for i in [x - 1, x + 1, x * 2]:
        if 0 <= i <= MAX:
            if L[i] == 0 or L[i] < shortest:
                if i == K:
                    if shortest == -1:
                        count += 1
                        shortest = L[x]
                        print('F', L[i], i, K)
                    elif L[i] == shortest:
                        count += 1
                        print(L[i], i, K)
                else:
                    Q.append(i)
                    L[i] = L[x] + 1
                    print('A', i, Q)
            elif shortest != -1 and L[i] > shortest:
                print(count)
                exit(0)
    print('----------')