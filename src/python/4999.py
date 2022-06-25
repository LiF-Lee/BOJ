from sys import stdin, stdout
A = stdin.readline().rstrip()
B = stdin.readline().rstrip()

stdout.write('go' if B in A else 'no')