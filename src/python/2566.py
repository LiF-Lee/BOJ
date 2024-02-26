import heapq
m=[]
for i in range(9):
    a=list(map(int, input().split()))
    b=max(a)
    heapq.heappush(m,(-b,i+1,a.index(b)+1))
c=heapq.heappop(m)
print(f"{-c[0]}\n{c[1]} {c[2]}")