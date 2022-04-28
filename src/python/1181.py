a = int(input())
l = []
for _ in range(a):
    l.append(input())
l = sorted(list(set(l)))

def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[len(l) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in l:
        if len(num) < len(pivot):
            lesser_arr.append(num)
        elif len(num) > len(pivot):
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

print('\n'.join(quick_sort(l)))