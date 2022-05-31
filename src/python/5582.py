from sys import stdin, stdout
str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()
DP = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
MAX = 0
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
            MAX = max(MAX, DP[i][j])
print(MAX)