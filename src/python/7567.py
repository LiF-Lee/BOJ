from sys import stdin, stdout
a = stdin.readline().rstrip()
c, s = -1, 0
for i in a:
    if i == '(' and c == 0:
        s += 5
    elif i == ')' and c == 1:
        s += 5
    else:
        s += 10
        c = 0 if i == '(' else 1
print(s)