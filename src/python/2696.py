from sys import stdin, stdout
import heapq
N = int(stdin.readline())
for _ in range(N):
    n = int(stdin.readline())
    L, R, nums, Res = [], [], [], []
    for i in range(n // 10 + 1):
        nums.extend(list(map(int, stdin.readline().split())))
    for idx, num in enumerate(nums):
        if len(L) == len(R):
            heapq.heappush(L, num * -1)
        else:
            heapq.heappush(R, num)
        if len(L) >= 1 and len(R) >= 1 and L[0] * -1 > R[0]:
            L_val = heapq.heappop(L) * -1
            R_val = heapq.heappop(R)
            heapq.heappush(L, R_val * -1)
            heapq.heappush(R, L_val)
        if (idx + 1) % 2 == 1:
            if len(L) == len(R):
                Res.append(min(L[0] * -1, R[0]))
            else:
                Res.append(L[0] * -1)
    print(len(Res))
    l = 0
    for i in Res:
        l += 1
        print(i, end=' ')
        if l % 10 == 0:
            print()