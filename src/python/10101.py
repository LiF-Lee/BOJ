a = [int(input()) for _ in range(3)]
if a[0] + a[1] + a[2] != 180:
    print('Error')
elif a[0] == a[1] == a[2]:
    print('Equilateral')
elif a[0] != a[1] and a[1] != a[2] and a[0] != a[2]:
    print('Scalene')
else:
    print('Isosceles')