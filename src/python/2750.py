from sys import stdin, stdout
N = int(stdin.readline())
L = [int(stdin.readline()) for i in range(N)]
L.sort()
print(*L, sep='\n')