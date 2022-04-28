a = input()

current = 97
for i in range(26):
    try:
        print(a.index(chr(current)), end=' ')
    except:
        print(-1, end=' ')
    current += 1