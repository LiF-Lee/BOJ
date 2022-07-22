from sys import stdin, stdout
from collections import deque
for _ in range(int(stdin.readline())):
    sheep_count = 0
    row, column = map(int, stdin.readline().split())
    sheep = [list(input()) for _ in range(row)]
    visit_sheep = [[0] * column for _ in range(row)]
    deque_sheep = deque()
    for i in range(row):
        for j in range(column):
            if sheep[i][j] == '#' and visit_sheep[i][j] == 0:
                sheep_count += 1
                visit_sheep[i][j] = 1
                deque_sheep.append((i, j))
                while deque_sheep:
                    x, y = deque_sheep.popleft()
                    for r, c in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
                        if 0 <= r < row and 0 <= c < column and sheep[r][c] == '#' and visit_sheep[r][c] == 0:
                            visit_sheep[r][c] = 1
                            deque_sheep.append((r, c))
    stdout.write(f"{sheep_count}\n")