from sys import stdin, stdout
a = stdin.readline().rstrip()
s = 0
for i in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    s += a.count(i)
    a = a.replace(i, ' ')
for j in a.split():
    s += len(j)
print(s)