a = input()
n = 0
for i in range(len(a)):
    n += int(a[i])
    if a[i] == '0':
        n += 9
print(n)