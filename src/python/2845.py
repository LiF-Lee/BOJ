l, p = map(int, input().split())
v = list(map(int, input().split()))
for i in range(5):
    print(v[i] - (l * p), end=" ")