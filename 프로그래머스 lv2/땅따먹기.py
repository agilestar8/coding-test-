land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

for i in range(1, len(land)): # 1 2
    for j in range(len(land[0])): # 0 1 2 3
        land[i][j] = max(land[i-1][:j] + land[i-1][j+1:]) + land[i][j]
        # 자신의 열를 제외한 윗줄 배열을 구성한 후 현재 위치와 합한 것중 제일 큰거 추출

print(max(land[-1]))

