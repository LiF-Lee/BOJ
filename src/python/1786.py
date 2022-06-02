from sys import stdin, stdout
T = stdin.readline().rstrip()
P = stdin.readline().rstrip()

def KMP_Search(txt, pat):
    M, N = len(pat), len(txt)
    lps = [0] * M
    k, l, i, j = 1, 0, 0, 0
    R = []
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
            R.append(i - j)
            j = lps[j - 1]
    return R

KMP_Result = KMP_Search(T, P)
print(len(KMP_Result))
for i in KMP_Result:
    print(i + 1, end=' ')