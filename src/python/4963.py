from sys import stdin, stdout
from collections import deque
while True:
    island_count = 0
    column, row = map(int, stdin.readline().split())
    if row == 0 and column == 0:
        break
    island = [input().split() for _ in range(row)]
    visit_island = [[0] * column for _ in range(row)]
    deque_island = deque()
    for i in range(row):
        for j in range(column):
            if island[i][j] == '1' and visit_island[i][j] == 0:
                island_count += 1
                visit_island[i][j] = 1
                deque_island.append((i, j))
                while deque_island:
                    x, y = deque_island.popleft()
                    for r, c in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]:
                        if 0 <= r < row and 0 <= c < column and island[r][c] == '1' and visit_island[r][c] == 0:
                            visit_island[r][c] = 1
                            deque_island.append((r, c))
    stdout.write(f"{island_count}\n")