from sys import stdin, stdout   
while True:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        stdout.write('factor\n')
    elif a % b == 0:
        stdout.write('multiple\n')
    else:
        stdout.write('neither\n')