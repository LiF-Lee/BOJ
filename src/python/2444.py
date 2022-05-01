a = int(input())
for i in range(1, a * 2, 2):
    print(" " * int((a * 2 - i) / 2) + "*" * i)
for i in range(a * 2 - 3, 0, -2):
    print(" " * int((a * 2 - i) / 2) + "*" * i)