N = 5
# direction = input().split()
direction = ["R", 'R', 'R', 'U', 'D', 'D']

x,y = 1,1

for i in direction:
    if i == "R":
        if y >= N:
            continue
        else:
            y += 1
    elif i == "L":
        if y <= 1:
            continue
        else:
            y -= 1
    elif i == "U":
        if x <= 1:
            continue
        else:
            x -= 1
    elif i == "D":
        if x >= N:
            continue
        else:
            x += 1

print(x,y)

# if 벗어나면 무시

