# 피보나치 수를 K로 나눈 나머지는 항상 주기를 가지게 되는데, 이를 피사노 주기(Pisano Period)라고 한다
# 주기의 길이가 P 이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같다.
# M = 10k 일 때, k > 2 라면, 주기는 항상 15 × 10k-1 이다.
# 출처 : https://www.acmicpc.net/blog/view/28

from sys import stdin, stdout
n = int(stdin.readline())

MOD = 1_000_000
P = 15 * (MOD // 10)

DP = [0 for _ in range(n + 2 if n < P else P + 2)]
DP[1] = 1

for i in range(2, n + 1 if n < P else P + 1):
    DP[i] = (DP[i - 1] + DP[i - 2]) % 1000000

print(DP[n % P])