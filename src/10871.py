a, x = map(int, input().split())
A = list(map(int, input().split()))
r_A = []

for i in range(a):
    if A[i] < x:
        r_A.append(A[i])

print(' '.join(map(str, r_A)))