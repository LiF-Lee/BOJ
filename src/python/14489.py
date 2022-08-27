a, b = map(int, input().split())
c = int(input()) * 2
print(a + b if c > a + b else a + b - c)