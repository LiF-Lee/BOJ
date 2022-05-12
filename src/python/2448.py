from sys import stdin, stdout

def star(n):
    default = [
        '*',
        '* *',
        '*****',
    ]
    for _ in range(n):
        d = []
        for i in range(len(default)):
            d.append(default[i] + ' ' * len(default[-(i+1)]) + default[i])
        default.extend(d)
    len_star = len(default) - 1
    for j in range(len_star, -1, -1):
        print(' ' * j + default[len_star - j] + ' ' * j)

D = {
    '3': 0,
    '6': 1,
    '12': 2,
    '24': 3,
    '48': 4,
    '96': 5,
    '192': 6,
    '384': 7,
    '768': 8,
    '1536': 9,
    '3072': 10,
}

N = D[stdin.readline().rstrip()]
star(N)