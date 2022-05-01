from sys import stdin, stdout
from collections import deque
import math
M, N = map(int, stdin.readline().split())
for i in range(M, N + 1):
    if i < 2:
        continue
    if i == 2:
        stdout.write(f"{i}\n")
        continue
    prime = True
    for j in range(2, math.ceil(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        stdout.write(f"{i}\n")