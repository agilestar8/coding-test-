n = 26
d = [0] * 30001

for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[n])

# 백준 1로 만들기
# n = int(input())
# memo = [0 for _ in range(n+1)]
# for i in range(2, n + 1):
#     memo[i] = memo[i-1] + 1 # 1은 2에서 1을 빼면 완성
# 
#     if i % 3 == 0: # 3의 배수면
#         memo[i] = min(memo[i], memo[i // 3] + 1)
# 
#     if i % 2 == 0: # 2의 배수면
#         memo[i] = min(memo[i], memo[i // 2] + 1)
# 
# print(memo[n])