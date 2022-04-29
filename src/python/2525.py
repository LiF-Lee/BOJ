from sys import stdin, stdout
h, m = map(int, stdin.readline().split())
c = int(stdin.readline())
stdout.write(f"{(h + (m + c) // 60) % 24} {(m + c) % 60}")