K = list(map(int, input().split()))
A = list(map(int, input().split()))
H = list(map(int, input().split()))
print(H[0]*H[1]*H[2]*(K[0]*K[1]+A[0]*A[1]))