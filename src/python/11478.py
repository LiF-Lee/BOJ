from sys import stdin, stdout
S = stdin.readline().rstrip()
L = []
for i in range(1, len(S) + 1):
    for j in range(len(S) - i + 1):
        L.append(S[j:j + i])
print(len(set(L)))