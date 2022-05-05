from sys import stdin, stdout
bit_flag = 0
for _ in range(int(stdin.readline())):
    cmd = stdin.readline().strip().split()
    if cmd[0] == 'add':
        bit_flag |= 1 << int(cmd[1])
    elif cmd[0] == 'remove':
        bit_flag &= ~(1 << int(cmd[1]))
    elif cmd[0] == 'check':
        stdout.write(f"{1 if bit_flag & (1 << int(cmd[1])) else 0}\n")
    elif cmd[0] == 'toggle':
        bit_flag ^= 1 << int(cmd[1])
    elif cmd[0] == 'all':
        bit_flag = 0xFFFFFFFF
    elif cmd[0] == 'empty':
        bit_flag = 0