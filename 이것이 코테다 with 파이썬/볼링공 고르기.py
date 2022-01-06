n, m = map(int, input().split())
balls = list(map(int, input().split()))

cnt = 0
# for i in range(n):
#     for j in range(i,n):
#         if balls[i] != balls[j]:
#             # print(i,j)
#             cnt += 1
#
# print(cnt)

arr = [0]*11
for i in balls:
    # 각 무게에 해당하는 볼링공 개수 카운트
    arr[i] += 1

for i in range(1, m+1): # 각 무게에 대해 1~m
    n = n - arr[i]      # 무게가 i인 공의 개수만큼 경우의 수 빼기
    cnt += arr[i] * n   # 즉, 경우의수 = 공 개수 x 경우의 수

print(cnt)

# ex1
# 5 3
# 1 3 2 3 2

# ex2
# 8 5
# 1 5 4 3 2 4 5 2