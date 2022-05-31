from sys import stdin, stdout
N, M = map(int, stdin.readline().split())
L = [list(map(int, stdin.readline().split())) for _ in range(N)]
PREFIX_SUM = [[0] * N for _ in range(N)]
PREFIX_SUM[0][0] = L[0][0]
for i in range(1, N * N):
    PREFIX_SUM[i // N][i % N] = L[i // N][i % N] + (PREFIX_SUM[i // N][i % N - 1] if i % N > 0 else 0)
Q = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    Q.append((x1 - 1, y1 - 1, x2 - 1, y2 - 1))
    s = 0
    for x in range(x1, x2 + 1):
        s += PREFIX_SUM[x][y2] - (PREFIX_SUM[x][y1 - 1] if y1 > 0 else 0)
    print(s)