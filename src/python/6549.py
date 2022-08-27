from sys import stdin, stdout

def f(L):
    return
    
while True:
    n, *h = map(int, stdin.readline().rstrip().split())
    if n == 0:
        break
    MAX = max(n, *h)
    for i in range(1, n - 1):
        print(i)
        
    print(n, h, MAX)
