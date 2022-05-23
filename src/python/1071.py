from sys import stdin, stdout
N = int(stdin.readline())
L = list(map(int, stdin.readline().split()))
L.sort()
print(L)