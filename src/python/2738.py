a, b = map(int, input().split())
L = []
for _ in range(a * 2):
    L.append(list(map(int, input().split())))
for i in range(a):
    for j in range(b):
        print(L[i][j] + L[i + a][j], end=' ')
    print()
