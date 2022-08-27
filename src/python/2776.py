from sys import stdin, stdout
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    n = { i : 0 for i in stdin.readline().rstrip().split() }
    M = int(stdin.readline())
    m = [i for i in stdin.readline().rstrip().split()]
    for i in m:
        stdout.write(f"{'1' if i in n else '0'}\n")