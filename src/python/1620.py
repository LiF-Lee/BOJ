from sys import stdin, stdout
N, M = map(int, stdin.readline().split())
L = {}
for i in range(N):
    pokemon = stdin.readline().strip()
    L[pokemon] = str(i + 1)
L_v = { v:k for k,v in L.items() }
for _ in range(M):
    pokemon = stdin.readline().strip()
    if pokemon in L:
        stdout.write(L[pokemon] + '\n')
    else:
        stdout.write(L_v[pokemon] + '\n')