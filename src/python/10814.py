import sys
a = int(sys.stdin.readline())
l = [sys.stdin.readline().split() for _ in range(a)]
l.sort(key=lambda x: int(x[0]))
for i in range(a):
    sys.stdout.write("%s %s\n" % (l[i][0], l[i][1]))