n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(input()))

error = []
for i in range(n-7):
    for j in range(m-7):
        WB_error = 0
        BW_error = 0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2 == 0: # 합짝수 칸
                    # WB
                    if board[x][y] != 'W':
                        WB_error += 1
                    # BW
                    if board[x][y] != "B":
                        BW_error += 1

                else: # 합홀수 칸
                    # WB
                    if board[x][y] != "B":
                        WB_error += 1
                    # BW
                    if board[x][y] != "W":
                        BW_error += 1
        error.append(WB_error)
        error.append(BW_error)

print(min(error))

