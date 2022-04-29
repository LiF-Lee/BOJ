from sys import stdin, stdout
n = int(stdin.readline())
data = [int(stdin.readline()) for _ in range(n)][::-1]
r_sum = 0
d_count = 0
for i in range(n):
    if data[i] == 0:
        d_count += 1
        continue
    if d_count > 0:
        d_count -= 1
        continue
    r_sum += data[i]
stdout.write("%d" % r_sum)