y, x = map(int, input().split())
chess = []
chess_white = []
chess_black = []

for _ in range(y):
    chess.append(input())

for i in range(y):
    temp_w = ''
    temp_b = ''
    target = 'W' if i % 2 == 0 else 'B'
    for j in range(x):
        if chess[i][j] == target:
            temp_w += '0'
            temp_b += '1'
        else:
            temp_w += '1'
            temp_b += '0'
        target = 'B' if target == 'W' else 'W'
    chess_white.append(temp_w)
    chess_black.append(temp_b)
    
min_list = []

for i in range(x - 7):
    for j in range(y - 7):
        w_sum = 0
        b_sum = 0
        for k in range(8):
            w_line = chess_white[j + k][i:i + 8]
            b_line = chess_black[j + k][i:i + 8]
            w_sum += w_line.count('1')
            b_sum += b_line.count('1')
        min_list.append(w_sum)
        min_list.append(b_sum)

print(min(min_list))