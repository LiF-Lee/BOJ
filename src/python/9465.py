from sys import stdin, stdout
T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    L = [[], []]
    DP = [[0] * n, [0] * n]
    L[0] = list(map(int, stdin.readline().split()))
    L[1] = list(map(int, stdin.readline().split()))
    DP[0][0] = L[0][0]
    DP[1][0] = L[1][0]
    DP[0][1] = DP[1][0] + L[0][1]
    DP[1][1] = DP[0][0] + L[1][1]
    for i in range(2, n):
        DP[0][i] = max(DP[1][i - 1], DP[1][i - 2]) + L[0][i]
        DP[1][i] = max(DP[0][i - 1], DP[0][i - 2]) + L[1][i]
    print(max(DP[0][n - 1], DP[1][n - 1]))