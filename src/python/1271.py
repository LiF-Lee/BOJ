from sys import stdin, stdout
a, b = map(int, stdin.readline().split())
print(a // b, a % b, sep='\n')