from sys import stdin, stdout
N = int(stdin.readline())
A, B = map(int, stdin.readline().split())

print(min(N, A//2 + B))