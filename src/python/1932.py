from sys import stdin, stdout
n = int(stdin.readline())
t = [list(map(int, stdin.readline().split())) for _ in range(n)]
d = [[0] * i for i in range(1, n + 1)]
d[0] = t[0]
for i in range(1, n):
    for j in range(i + 1):
        d[i][j] = max(d[i - 1][j - 1] + t[i][j] if j - 1 >= 0 else 0, d[i - 1][j] + t[i][j] if j < i else 0)
print(max(d[-1]))