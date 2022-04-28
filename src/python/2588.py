import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline()

for i in range(3):
    print(a * int(b[2-i]))
print(a * int(b))