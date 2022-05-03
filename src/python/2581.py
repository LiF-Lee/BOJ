from sys import stdin, stdout

def prime(x1, x2):
    L = []
    for i in range(x1, x2 + 1):
        if i <= 1:
            continue
        hit = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                hit += 1
        if hit == 1:
            L.append(i)
    return L

a = prime(int(stdin.readline()), int(stdin.readline()))
if len(a) == 0:
    print(-1)
else:
    print(sum(a), a[0], sep='\n')