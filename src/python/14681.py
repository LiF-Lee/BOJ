from sys import stdin, stdout
x, y = int(stdin.readline()) > 0, int(stdin.readline()) > 0

if x and y:
    print(1)
elif not x and y:
    print(2)
elif not x and not y:
    print(3)
elif x and not y:
    print(4)