S = input()
if S == S[::-1]:
    print(len(S))
else:
    for i in range(1, len(S)):
        if S[i:] == S[:i-1:-1]:
            print(len(S) + i)
            break