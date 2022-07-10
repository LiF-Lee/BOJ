from sys import stdin, stdout
K = int(stdin.readline())
for X in range(1, K + 1):
    Scores = list(map(int, stdin.readline().split()))
    StudentCount = Scores.pop(0)
    Scores.sort(reverse=True)
    LargestGap = [-1 for _ in range(StudentCount - 1)]
    LargestGap[0] = Scores[0] - Scores[1]
    for i in range(1, StudentCount - 1):
        LargestGap[i] = max(LargestGap[i - 1], Scores[i] - Scores[i + 1])
    stdout.write(f"Class {X}\n")
    stdout.write(f"Max {Scores[0]}, Min {Scores[-1]}, Largest gap {LargestGap[-1]}\n")