a = int(input())
b = list(map(int, input().split()))
max_s = max(b)

c = 0
for i in b:
    c += i / max_s * 100
print(c / a)