from sys import stdin, stdout
txt = stdin.readline().rstrip()
bomb_txt = stdin.readline().rstrip()
len_bomb_txt = len(bomb_txt)
stack = []

for char in txt:
    stack.append(char)
    if char == bomb_txt[-1]:
        if ''.join(stack[-len_bomb_txt:]) == bomb_txt:
            del stack[-len_bomb_txt:]

print('FRULA' if len(stack) == 0 else ''.join(stack))