from sys import stdin, stdout
target = int(stdin.readline())
btn_count = int(stdin.readline())
press_count = abs(target - 100)
if btn_count == 0:
    stdout.write(f"{min(press_count, len(str(target)))}")
    exit()
btn_list = list(map(str, stdin.readline().split()))
if btn_count == 10 or target == 100:
    stdout.write(f"{press_count}")
    exit()
min_val, max_val = 0, 1000001
for i in range(min_val, max_val):
    if any(ext in str(i) for ext in btn_list):
        continue
    press_count = min(press_count, len(str(i)) + abs(target - i))
stdout.write(str(press_count))