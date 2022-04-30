from sys import stdin, stdout
a = int(stdin.readline())
result = []
for i in range(a - 1, 0, -1):
    sum_val = i
    for j in list(str(i)):
        sum_val += int(j)
    if sum_val == a:
        result.append(i)
if len(result) == 0:
    stdout.write('0')
else:
    stdout.write(str(min(result)))