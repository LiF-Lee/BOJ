from sys import stdin, stdout
a = int(stdin.readline()) - 1
if a == 0:
    print(1)
    exit()
loop = 0
current = 0
while True:
    loop += 1
    current += loop * 6
    if a <= current:
        break
print(loop + 1)