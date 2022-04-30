from sys import stdin, stdout
a = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
if a == 1:
    stdout.write(f"{l[0]**2}")
else:
    stdout.write(f"{min(l) * max(l)}")