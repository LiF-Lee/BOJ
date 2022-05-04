from sys import stdin, stdout
from functools import cache
a, b, c = map(int, stdin.readline().split())

@cache
def power(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (power(a, b//2, c) ** 2) % c
    else: 
        return ((power(a, b//2, c) ** 2) * a) % c

print(power(a, b, c))