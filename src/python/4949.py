while True:
    L = []
    a = input()
    if a == '.':
        break
    ok = True
    for i in a:
        if i == '[' or i == '(':
            L.append(i)
        elif i == ']' or i == ')':
            if len(L) == 0:
                ok = False
                break
            if L[-1] == '[' and i == ']':
                L.pop()
            elif L[-1] == '(' and i == ')':
                L.pop()
            else:
                ok = False
                break
    if ok and len(L) == 0:
        print('yes')
    else:
        print('no')