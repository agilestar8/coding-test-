board = [[0,0,0,0,0], # 0
         [0,0,1,0,3], # 1
         [0,2,5,0,1], # 2
         [4,2,4,4,2], # 3
         [3,5,1,3,1]] # 4
        # 0 1 2 3 4

moves = [1,5,3,5,1,2,1,4]
basket = []
cnt = 0

for i in moves:
    for j in range(len(board)):
        if board[j][i-1] == 0:
            pass
        else:
            basket.append(board[j][i-1])
            board[j][i-1] = 0
            break

    if len(basket)>1 and basket[-1] == basket[-2]:
        basket.pop()
        basket.pop()
        cnt+=2

print(cnt)








