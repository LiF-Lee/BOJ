from sys import stdin, stdout
N = int(stdin.readline())
L = [0 for _ in range(1001)]
s = stdin.readline().strip().split()
for i in s:
    L[int(i)] += 1
S = [0]
for j in range(1001):
    if L[j] > 0:
        for k in range(L[j]):
            S.append(j + S[-1])
print(sum(S))