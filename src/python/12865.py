n, k = map(int, input().split())

thing = [[0,0]]
d = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n + 1):
    weight = thing[i][0]
    value = thing[i][1]
    for j in range(1, k + 1):
        if j - weight >= 0:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - weight] + value)
        else:
            d[i][j] = d[i - 1][j]

print(d[n][k])