from sys import stdin, stdout
t = stdin.readline().rstrip()
P = stdin.readline().rstrip()

def KMP_Search(txt, pat):
    M, N = len(pat), len(txt)
    lps = [0] * M
    k, l, i, j = 1, 0, 0, 0
    while k < M:
        if pat[k] == pat[l]:
            l += 1
            lps[k] = l
            k += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[k] = 0
                k += 1
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:
            return 1
    return 0
T = []
for i in range(len(t)):
    if t[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        T.append(t[i])
KMP_Result = KMP_Search(''.join(T), P)
print(KMP_Result)