a = int(input())
b = []
r = ''

for i in range(a):
    b.append(input())

for i in range(len(b[0])):
    m = 0
    l = b[0][i]
    for j in range(a):
        if b[j][i] == l:
            m += 1
    if m != a:
        r += '?'
    else:
        r += l
        
print(r)