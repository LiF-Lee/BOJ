from lib2to3.pgen2.token import EQUAL
from sys import stdin, stdout
T = int(stdin.readline())
L = []
for _ in range(T):
    L.append(stdin.readline().strip())

for i in L:
    if i.startswith(')') != i.endswith('('):
        stdout.write('NO\n')
        continue
    if i.count('(') != i.count(')'):
        stdout.write('NO\n')
        continue
    while i.count('()') > 0: 
        i = i.replace('()', '')
    if i == '': 
        stdout.write('YES\n')
    else: 
        stdout.write('NO\n')