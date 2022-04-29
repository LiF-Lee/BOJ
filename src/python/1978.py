from sys import stdin, stdout
n = int(stdin.readline())
numbers = map(int, stdin.readline().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num):
            if num % i == 0:
                error += 1
        if error == 0:
            sosu += 1
print(sosu)