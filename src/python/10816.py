from sys import stdin, stdout

a = int(stdin.readline())
N = sorted(map(int, stdin.readline().split()))
M = int(stdin.readline())
l = list(map(int, stdin.readline().split()))

def Binary_Search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return array[start:end+1].count(target)
    elif array[mid] > target:
        return Binary_Search(array, target, start, mid - 1)
    else:
        return Binary_Search(array, target, mid + 1, end)

n_dic = {}
for n in N:
    if n not in n_dic:
        n_dic[n] = Binary_Search(N, n, 0, a - 1)

for i in l:
    if i in n_dic:
        stdout.write("%d " % n_dic[i])
        continue
    stdout.write("%d " % 0)