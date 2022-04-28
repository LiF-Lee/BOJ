import sys
a = int(sys.stdin.readline())
l = []
for i in range(a):
    l.append(int(sys.stdin.readline()))
print(*sorted(l), sep='\n')