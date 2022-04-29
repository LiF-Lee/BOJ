from sys import stdin, stdout
while True:
    a, b, c = map(int, stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 + b**2 == c**2:
        stdout.write("right\n")
    elif a**2 + c**2 == b**2:
        stdout.write("right\n")
    elif b**2 + c**2 == a**2:
        stdout.write("right\n")
    else:
        stdout.write("wrong\n")