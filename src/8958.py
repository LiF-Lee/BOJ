a = int(input())
for i in range(a):
    current = 1
    score = 0
    ox = input()
    for j in range(len(ox)):
        if ox[j] == 'O':
            score += current
            current += 1
        else:
            current = 1
    print(score)