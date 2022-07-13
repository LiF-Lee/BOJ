from sys import stdin, stdout
A, B = [], []

A_row, A_column = map(int, stdin.readline().split())
for i in range(A_row):
    A.append(list(map(int, stdin.readline().split())))

B_row, B_column = map(int, stdin.readline().split())
for i in range(B_row):
    B.append(list(map(int, stdin.readline().split())))

for row in range(A_row):
    for column in range(B_column):
        v = 0
        for i in range(B_row):
            v += A[row][i] * B[i][column]
        print(v, end=' ')
    print()