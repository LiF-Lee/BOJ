from sys import stdin, stdout
a = int(stdin.readline())
for _ in range(a):
    L = list(map(int, stdin.readline().split()))
    v_count = L.pop(0)
    v_sum = sum(L)
    v_avg = v_sum / v_count
    v_avg_count = 0
    for i in range(v_count):
        if L[i] > v_avg:
            v_avg_count += 1
    v_avg_count_per = v_avg_count / v_count * 100
    stdout.write(f"{v_avg_count_per:.3f}%\n")