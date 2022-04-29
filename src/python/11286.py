from ast import Lambda
from sys import stdin, stdout
N = int(stdin.readline())
L = []
for _ in range(N):
    R = int(stdin.readline())
    if R != 0:
        L.append(R)
        continue
    if len(L) != 0:
        L.sort(key=lambda x: abs(x))
        txt = L[0]
        if txt > 0:
            txt = '-' + str(txt)
        else:
            txt = str(abs(txt))
        stdout.write(f"{txt}\n")
        L.remove(L[0])
    else:
        stdout.write(f"{0}\n")