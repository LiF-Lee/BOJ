from sys import stdin, stdout
N = int(stdin.readline())
M = int(stdin.readline())
S = stdin.readline().strip()

sum_val, current, count = 0, 0, 0

while current < M - 1:
    if S[current:current + 3] == 'IOI':
        count += 1
        current += 2
        if count == N:
            count -= 1
            sum_val += 1
    else:
        count = 0
        current += 1

print(sum_val)