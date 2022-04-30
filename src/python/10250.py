from sys import stdin, stdout
a = int(stdin.readline())
for _ in range(a):
    H, W, N = map(int, stdin.readline().split())
    m, n = N % H, N // H + 1
    if m == 0:
        m = H
        n -= 1
    stdout.write(f"{m * 100 + n}\n")