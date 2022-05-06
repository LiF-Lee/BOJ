from sys import stdin, stdout
import heapq

def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

for _ in range(int(stdin.readline())):
    L = []
    a = int(stdin.readline())
    con = True
    for i in range(a):
        cmd = stdin.readline().rstrip().split()
        if con == False:
            continue
        if cmd[0] == 'I':
            heapq.heappush(L, int(cmd[1]))
        else:
            if len(L) == 0:
                con = False
                continue
            if cmd[1] == '-1':
                heapq.heappop(L)
            else:
                L = heap_sort(L)
                L.pop()
    if con == False:
        stdout.write('EMPTY\n')
    else:
        L = heap_sort(L)
        print(L[-1], L[0])