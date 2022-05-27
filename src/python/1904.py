from sys import stdin, stdout
N = int(stdin.readline())
DP = [0, 1, 2]
for i in range(3, N+1):
    DP.append((DP[i-1] + DP[i-2]) % 15746)
print(DP[N])