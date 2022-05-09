from sys import stdin, stdout
L = [int(stdin.readline()) for _ in range(4)]
R = sum(L)
print(R // 60, R % 60, sep='\n')