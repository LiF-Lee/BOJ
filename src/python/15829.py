from sys import stdin, stdout
L = stdin.readline()
char_list = stdin.readline().strip()
Hash = 0
for i, val in enumerate(char_list):
    Hash += (ord(val) - 96) * (31 ** i)
stdout.write(f"{Hash % 1234567891}")