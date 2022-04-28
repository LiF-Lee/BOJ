from sys import stdin, stdout
a = int(stdin.readline())
l = [stdin.readline().split() for _ in range(a)]
l.sort(key=lambda x: int(x[0]))
for i in range(a):
    stdout.write("%s %s\n" % (l[i][0], l[i][1]))