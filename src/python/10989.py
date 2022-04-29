from sys import stdin, stdout
a = int(stdin.readline())
l = [0] * 10001

for _ in range(a):
    l[int(stdin.readline())] += 1

for idx, val in enumerate(l):
    if val == 0:
        continue
    for _ in range(val):
        stdout.write("%d\n" % idx)