from sys import stdin, stdout

def square(N):
    current = 1
    default = [
        ['*', '*', '*'],
        ['*', ' ', '*'],
        ['*', '*', '*'],
    ]
    if N == 3:
        return default
    while 3 ** current < N:
        current += 1
        x = 3 ** current
        c = [[]] * 3 ** current
        for i in range(x // 3):
            c[i] = default[i] * 3
            c[x - i - 1] = default[i] * 3
            c[x - i - 1 - x // 3] = default[i] + [' '] * (x // 3) + default[i]
        default = c
    return default

N = int(stdin.readline())
S = square(N)
for i in range(N):
    stdout.write(f"{''.join(S[i])}\n")