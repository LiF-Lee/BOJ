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
        return 1
    elif array[mid] > target:
        return Binary_Search(array, target, start, mid - 1)
    else:
        return Binary_Search(array, target, mid + 1, end)

for i in l:
    stdout.write(f"{Binary_Search(N, i, 0, a - 1)} ")