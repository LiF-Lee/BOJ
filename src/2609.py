a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

r_gcd = gcd(a, b)
print(r_gcd)
print(int(a * b / r_gcd))