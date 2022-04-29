from sys import stdin, stdout
a = int(stdin.readline())
L = []
for _ in range(a):
    b, c = map(int, stdin.readline().split())
    L.append([b, c])
L.sort(key=lambda x: x[1])
L.sort(key=lambda x: x[0])
for i in range(a):
    stdout.write(f"{L[i][0]} {L[i][1]}\n")