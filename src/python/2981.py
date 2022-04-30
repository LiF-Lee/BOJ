from sys import stdin, stdout
a = int(stdin.readline())
L = [0] * a
for i in range(a):
    L[i] = int(stdin.readline())
L.sort()
r_list = []
for j in range(2, L[1] + 1):
    M = L[0] % j
    alive = True
    for k in range(a - 1, -1, -1):
        if L[k] % j != M:
            alive = False
            break
    if alive:
        r_list.append(j)
for l in r_list:
    stdout.write(f"{str(l)} ")