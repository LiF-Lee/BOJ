from sys import stdin, stdout
a, b = stdin.readline().rstrip(), stdin.readline().rstrip()
D = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
L = [[-1] * i for i in range(len(a) * 2, 1, -1)]

for i in range(len(a) + len(b)):
    if i % 2 == 0:
        L[0][i] = D[ord(a[i // 2]) - 65]
    else:
        L[0][i] = D[ord(b[i // 2]) - 65]
for i in range(1, len(L)):
    for j in range(len(L[i])):
        L[i][j] = (L[i - 1][j] + L[i - 1][j + 1]) % 10
print(f"{L[-1][0]}{L[-1][1]}")