a = list(map(int, input().split()))
if sum(a) in [0, 3]:
    print('*')
else:
    print(['A','B','C'][a.index(a[0] ^ a[1] ^ a[2])])