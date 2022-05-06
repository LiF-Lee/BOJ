from sys import stdin, stdout
from collections import deque
a, b = map(int, stdin.readline().split())
L = list(map(int, stdin.readline().split()))
prefix_sum = deque([0])

sum_val = 0
for i in L:
    sum_val += i
    prefix_sum.append(sum_val)

for j in range(b):
    i, j = map(int, stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i - 1])