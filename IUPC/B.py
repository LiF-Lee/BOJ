from sys import stdin, stdout
S, M = [], []
D = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}
for _ in range(20):
    _, s, m = map(str, stdin.readline().rstrip().split())
    if m == 'P':
        continue
    S.append(float(s))
    M.append(float(s) * D[m])
print(sum(M) / sum(S))