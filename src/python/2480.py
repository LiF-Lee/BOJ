from sys import stdin, stdout
a, b, c = map(int, stdin.readline().split())
if a == b and b == c:
    stdout.write(f"{10000 + a * 1000}")
elif a != b and b != c and a != c:
    stdout.write(f"{max(a, b, c) * 100}")
else: 
    stdout.write(f"{1000 + sorted([a, b, c])[1] * 100}")