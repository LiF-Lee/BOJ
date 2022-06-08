from sys import stdin, stdout
n = int(stdin.readline())

DP = [0 for _ in range(n + 2)]
DP[1] = 1

for i in range(2, n + 1):
    DP[i] = DP[i - 1] + DP[i - 2]

print(DP[n])