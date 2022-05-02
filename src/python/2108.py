from collections import deque
from sys import stdin, stdout
from collections import deque
import heapq
import math

def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

a = int(stdin.readline())
L = deque()

for _ in range(a):
    L.append(int(stdin.readline()))
L = heap_sort(L)
Dic = {}
Dic_list = deque(L)
for i in Dic_list:
    if i not in Dic:
        Dic[i] = 1
    else:
        Dic[i] += 1
A = round(sum(L) / a)
B = L[math.ceil(a / 2) - 1]

c = max(Dic, key=Dic.get)
r = max(deque([Dic[h] for h in Dic]))
v = deque()
for j in Dic:
    if Dic[j] == r:
        v.append(j)
C = v[1] if len(v) >= 2 else v[0]
D = L[-1] - L[0]

print(A, B, C, D , sep='\n')