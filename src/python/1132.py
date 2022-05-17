from sys import stdin, stdout
N = int(stdin.readline())

L, D, M, A, R = [], {}, {}, [], 0

for _ in range(N):
    a = stdin.readline().rstrip()
    L.append(a)
    A.append(a[0])
for i in L:
    v = 1
    for j in range(len(i) - 1, -1, -1):
        if i[j] not in D: D[i[j]] = v
        else: D[i[j]] += v
        v *= 10
sorted_dict = sorted(D.items(), key=lambda x: x[1], reverse=True)
for i in range(9, 9 - len(sorted_dict), -1): M[sorted_dict[9 - i][0]] = i
if len(M) == 10 and sorted_dict[-1][0] in A:
    for i in range(len(sorted_dict) - 1, -1, -1):
        if sorted_dict[i][0] not in A:
            for j in range(i + 1, len(sorted_dict)):
                M[sorted_dict[j][0]] += 1
            M[sorted_dict[i][0]] = 0
            break
for i in L:
    for j in i:
        i = i.replace(j, str(M[j]))
    R += int(i)
print(R)