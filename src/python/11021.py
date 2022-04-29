from sys import stdin, stdout
list = []
T = int(stdin.readline())
for _ in range(T):
    a, b = map(int, stdin.readline().split())
    list.append(a + b)
for idx, val in enumerate(list):
    stdout.write(f"Case #{idx + 1}: {val}\n")