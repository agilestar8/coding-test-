n = int(input())
rank = [1]*n
big = []

for i in range(n):
    x,y = map(int,input().split())
    big.append((x,y))

for i in range(n):
    for j in range(n):
        if big[i][0] < big[j][0] and big[i][1] < big[j][1]:
            rank[i] += 1

for i in rank:
    print(i) 
