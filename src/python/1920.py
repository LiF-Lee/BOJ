from sys import stdin, stdout

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

n = int(stdin.readline())
N = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
M = list(map(int, stdin.readline().split()))

N.sort()
for j in M:
    stdout.write(f"{Binary_Search(N, j, 0, n - 1)}\n")