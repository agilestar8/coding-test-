from itertools import combinations

n,m = map(int,input().split())
chicken, house = [],[]

for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i,j))
        elif data[j] == 2:
            chicken.append((i,j))

combination = list(combinations(chicken, m))  # 치킨집 중에서 m개 선택하는 모든 경우

def get_sum(candidate):
    result = 0
    for x,y in house: # 모든 집에 대해
        temp = 1e9
        for a,b in candidate:   # 선택된 m개 치킨집에 대해
            temp = min(temp, abs(x-a)+abs(y-b))     # 치킨 거리구하고 그 중 제일 작은 거를 저장해서 더하기
        result += temp
    return result

result = 1e9
for i in combination:
    result = min(result, get_sum(i))

print(result)

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2















