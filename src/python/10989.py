a = int(input())
l = []
for _ in range(a):
    l.append(input())
l.sort()
print('\n'.join(l))