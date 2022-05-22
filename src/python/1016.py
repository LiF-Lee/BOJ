from sys import stdin, stdout
min_val, max_val = map(int, stdin.readline().split())
L = [1 for _ in range(max_val - min_val + 1)]
i = 2
while i**2 <= max_val:
    square_num = i**2
    remain = 0 if min_val % square_num == 0 else 1
    mul = min_val // i**2 + remain
    while square_num * mul <= max_val:
        L[square_num * mul - min_val] = 0
        mul += 1
    i += 1
print(sum(L))