from sys import stdin, stdout
T = int(stdin.readline())
L = [[1,0], [0,1]]
a = [int(stdin.readline()) for _ in range(T)]

for i in range(2, max(a) + 1):
    L.append([L[i - 1][1], L[i - 1][0] + L[i - 1][1]])
for i in a:
    print(L[i][0], L[i][1])