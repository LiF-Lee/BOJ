from sys import stdin, stdout
for i in range(int(stdin.readline())):
    cmd1 = list(stdin.readline().strip().replace('RR', ''))
    list_len = int(stdin.readline())
    list_val = list(stdin.readline().rstrip()[1:-1].split(','))
    error = False
    del_right = True
    l, r = 0, 0
    for j in cmd1:
        if j == 'R':
            del_right = not del_right
        else:
            if del_right:
                l += 1
            else:
                r += 1
                
    if l + r <= list_len:
        if del_right:
            stdout.write(f"[{','.join(list_val[l:list_len-r])}]\n")
        else:
            list_val.reverse()
            stdout.write(f"[{','.join(list_val[r:list_len-l])}]\n")
    else:
        stdout.write('error\n')