from sys import stdin, stdout
n = int(stdin.readline())
data = [int(stdin.readline()) for _ in range(n)]
index_n = 0
for i in range(n):
    print('-', index_n)
    if data[i] == 0:
        data[index_n] = 0
        index_n -= 1
        if (data[index_n] == 0):
            for j in range(index_n):
                if data[index_n - j] != 0:
                    index_n -= j
                    break
        continue
    index_n = i
s_result = 0
for k in range(n):
    s_result += data[k]
stdout.write("%s" % s_result)