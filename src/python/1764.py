from sys import stdin, stdout
a, b = map(int, stdin.readline().split())
D = {}
for _ in range(a):
    D[stdin.readline().rstrip()] = 1
for _ in range(b):
    c = stdin.readline().rstrip()
    if c in D:
        D[c] = 2
sum_val = 0
result_list = []
for k in D:
    if D[k] == 2:
        sum_val += 1
        result_list.append(k)
result_list.sort()
print(sum_val)
print('\n'.join(result_list))