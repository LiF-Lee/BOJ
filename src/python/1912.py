from sys import stdin, stdout
n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
DP = [0 for _ in range(n)] # DP[n] = L[0]...L[n] 까지의 합
DP[0] = L[0]
max_val, min_val = DP[0], 0
for i in range(1, n):
    DP[i] = DP[i - 1] + L[i]
    min_val = min(min_val, DP[i - 1])
    max_val = max(DP[i] - min_val, L[i], max_val)
# print(DP)
print(max_val)