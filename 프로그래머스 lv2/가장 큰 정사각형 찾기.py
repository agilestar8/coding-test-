board = [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,0]]

for i in range(1, len(board)):
    for j in range(1, len(board[0])):
        if board[i][j] >= 1:
            board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1

answer = 0
for i in board:
    if answer < max(i):
        answer = max(i)

for i in range(4):
    for j in range(4):
        print(board[i][j], end = " ")
    print()

