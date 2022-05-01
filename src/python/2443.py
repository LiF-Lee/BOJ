a = int(input())
for i in range(a * 2 - 1, 0, -2):
    print(" " * int((a * 2 - 1 - i) / 2) + "*" * i)