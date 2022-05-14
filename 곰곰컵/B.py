from sys import stdin, stdout
N = int(stdin.readline())

chat = []
count = 0

for _ in range(N):
    A = stdin.readline().rstrip()
    if A == 'ENTER':
        count += len(list(set(chat)))
        chat = []
    else:
        chat.append(A)

count += len(list(set(chat)))
print(count)