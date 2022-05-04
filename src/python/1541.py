from sys import stdin, stdout
a = list(map(str, stdin.readline().strip().split('-')))
sum_val = 0
for i in a[0].split('+'):
    sum_val += int(i)
for j in range(1, len(a)):
    m = list(map(int, a[j].split('+')))
    sum_val -= sum(m)
print(sum_val)