from sys import stdin, stdout

def x(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return (n - 1) ^ n
    elif n % 4 == 2:
        return (n - 2) ^ (n - 1) ^ n
    elif n % 4 == 3:
        return 0

for i in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    stdout.write(f"{x(a - 1) ^ x(b)}\n")