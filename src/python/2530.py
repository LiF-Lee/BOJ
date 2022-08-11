h, m, s = map(int, input().split())
t = int(input())
s = s+t
m = m+s//60
h = h+m//60
print(h%24, m%60, s%60)