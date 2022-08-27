y, m, d = map(int, input().split())
_y, _m, _d = map(int, input().split())
print(_y-y if _m > m or (_m >= m and _d >= d) else _y-y-1, _y-y+1, _y-y, sep="\n")