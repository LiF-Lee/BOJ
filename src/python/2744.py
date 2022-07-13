for i in input():
    print(chr(ord(i) - 32 if ord(i) >= 97 else ord(i) + 32), end='')