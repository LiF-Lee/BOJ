from sys import stdin, stdout
import math

i = int(stdin.readline())
while True:
    if i == 1:
        continue
    if i == 2:
        stdout.write('2')
        break
    prime = True
    for j in range(2, math.ceil(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        if str(i)[0] == str(i)[-1]:
            if str(i) == str(i)[::-1]:
                stdout.write(f"{i}")
                break
    i += 1