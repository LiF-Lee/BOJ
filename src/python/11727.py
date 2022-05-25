from sys import stdin, stdout
L = [0, 1, 3]
n = int(stdin.readline())
for i in range(3, n + 1):
    L.append(L[i - 2] * 2 + L[i - 1])
print(L[n] % 10007)