print("index\t\telement")
s = 0
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            s += 1
            print(f"{(i, j, k)}\t{s}")

            