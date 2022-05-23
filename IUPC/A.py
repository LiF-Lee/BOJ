from sys import stdin, stdout
N = int(stdin.readline())
s = stdin.readline().rstrip()
ok = False
for i in ['r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt', 't', 'tt', 'd', 'w', 'c', 'z', 'x', 'v', 'g']:
    if s.endswith(i):
        ok = True
        break
if ok:
    print(1)
else:
    print(0)