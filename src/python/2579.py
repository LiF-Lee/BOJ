from sys import stdin, stdout
n = int(stdin.readline())
L = [int(stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(n)]
dp[0] = L[0]
if n > 1:
    dp[1] = L[0] + L[1]
if n > 2:
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + L[i], dp[i - 3] + L[i - 1] + L[i])
print(dp[n - 1])