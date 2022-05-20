from sys import stdin, stdout
N = [int(i) for i in stdin.readline().rstrip()]
N.sort(reverse=True)
print(*N, sep='')