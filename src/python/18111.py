import sys
N, M, B = map(int, sys.stdin.readline().split())
l = []
for _ in range(N):
    l.append(list(map(int, sys.stdin.readline().split())))
print(l)

'''
3 4 1
64 64 66 64
64 64 64 64
64 64 64 63
'''