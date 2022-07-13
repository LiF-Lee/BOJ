for _ in range(int(input())):
    A, B = input().split()
    BA, BB = int(A, 2), int(B, 2)
    print(str(bin(BA + BB)).replace('0b', ''))
