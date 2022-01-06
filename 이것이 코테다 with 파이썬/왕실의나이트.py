input = "a1"

x = int(input[1])
y = ord(input[0])-96

cnt = 0
move = [(-1,2),(1,2),(-1,-2),(1,-2),(-2,1),(-2,-1),(2,-1),(2,1)]

for i in move:
    nx = x + i[0]
    ny = y + i[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    cnt += 1

print(cnt)
