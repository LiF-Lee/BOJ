from sys import stdin, stdout
N = int(stdin.readline())

for i in range(N // 5, -1, -1):
    a = N - (5 * i)
    if a % 3 == 0:
        print(i + a // 3)
        break
    elif i == 0:
        print(-1)
        break