from sys import stdin, stdout
a = int(stdin.readline())
L = [stdin.readline().rstrip().split() for _ in range(a)]
cut_list = []
result = []

for i in L:
    ok = False
    found = ()
    for j in range(len(i)):
        if i[j][0].lower() not in cut_list:
            ok = True
            found = (j, 0, i[j][0])
            cut_list.append(i[j][0].lower())
            break
    if not ok:
        for j_idx, j_val in enumerate(i):
            for idx, val in enumerate(j_val):
                if val.lower() not in cut_list:
                    ok = True
                    found = (j_idx, idx, val)
                    cut_list.append(val.lower())
                    break
            if ok:
                break
    dl = i[:]
    if not ok:
        result.append(' '.join(dl))
        continue
    txt = []
    for l in range(len(dl[found[0]])):
        if l == found[1]:
            txt.append(f"[{found[2]}]")
        else:
            txt.append(dl[found[0]][l])
    dl[found[0]] = ''.join(txt)
    result.append(' '.join(dl))
print(*result, sep='\n')