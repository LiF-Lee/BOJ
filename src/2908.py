n, m = list(map(str, input().split()))

n = int(n[::-1])
m = int(m[::-1])

print(n if n > m else m)