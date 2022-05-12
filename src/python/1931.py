from sys import stdin, stdout
N = int(stdin.readline())
L = []
for _ in range(N):
    L.append(list(map(int, stdin.readline().strip().split())))
L.sort(key=lambda x: (x[1], x[0]))
S = [L[0]]
for i in range(1, N):
    if L[i][0] >= S[-1][1]:
        S.append(L[i])
print(len(S))