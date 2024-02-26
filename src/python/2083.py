while True:
    i = input().split()
    n, a, w = i[0], int(i[1]), int(i[2])
    if n == "#" and a + w == 0:
        break
    print(n, "Senior" if (a > 17 or w >= 80) else "Junior")    