from sys import stdin, stdout
N = int(stdin.readline())
DP = [[0] * 100 for _ in range(N + 1)]
HP = list(map(int, stdin.readline().rstrip().split()))
HAPPY = list(map(int, stdin.readline().rstrip().split()))

for i in range(1, N + 1):
    _HP, _HAPPY = HP[i - 1], HAPPY[i - 1]
    for j in range(1, 100):
        DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - _HP] + _HAPPY) if j - _HP >= 0 else DP[i - 1][j]

stdout.write(str(DP[N][99]))