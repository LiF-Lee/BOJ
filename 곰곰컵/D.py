from sys import stdin, stdout
N = int(stdin.readline())
today = 2
for i in list(map(int, stdin.readline().split())):
    today += i
    if today % 7 == 6:
        break
if today % 7 == 6:
    print('YES')
else:
    print('NO')