from sys import stdin, stdout
N = int(stdin.readline())
works = map(int, stdin.readline().split())
week = [0 for _ in range(7)]

# 0: Sun ... 6: Sat
week[1] = 1

for i in works:
    work_end = set()
    for j in range(7):
        if week[j] == 1 and week[(j + i) % 7] == 0:
            work_end.add((j + i) % 7)
    for k in work_end:
        week[k] = 1

print('YES' if week[5] == 1 else 'NO')