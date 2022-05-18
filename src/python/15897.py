from sys import stdin, stdout
n = int(stdin.readline())
L = [0 for _ in range(n + 1)]
sv = 0
for i in range(1, n + 1):
    for j in range(1, n + 1, i):
        L[j] += 1
        sv += 1
print(sv)