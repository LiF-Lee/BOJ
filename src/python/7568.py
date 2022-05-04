from sys import stdin, stdout
a = int(stdin.readline())
L = []
for j in range(a):
    L.append(list(map(int, stdin.readline().split())))

for i in range(a):
    rank = 1
    for j in range(a):
        if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            rank += 1
    print(rank, end=' ')