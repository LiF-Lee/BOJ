from sys import stdin, stdout
T = int(stdin.readline())
for _ in range(T):
    k, n = int(stdin.readline()), int(stdin.readline())
    L = [[i for i in range(1, n + 1)]]
    sum_val = sum(L[0])
    for i in range(1, k + 1):
        L.append([])
        for j in range(n):
            L[i].append(sum(L[i - 1][:j + 1]))
            sum_val += sum(L[i])
    print(L[-1][-1])