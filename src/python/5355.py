for _ in range(int(input())):
    n, *a = input().split()
    n = float(n)
    for i in a:
        if i == '@':
            n *= 3
        elif i == '%':
            n += 5
        else:
            n -= 7
    print(f"{n:.2f}")