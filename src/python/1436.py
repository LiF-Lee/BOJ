from sys import stdin, stdout
a = int(stdin.readline())
hit = 0
current = 666
while True:
    if '666' in str(current):
        hit += 1
        if hit == a:
            print(current)
            break
    current += 1