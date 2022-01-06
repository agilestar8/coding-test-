# 점화식 a i = max(a i-1,(a i-2 + k))

n = 4
arr = list(map(int, input().split())) # 1 3 1 5 입력

# 0. d는 컨테이너 개수에 따른 정답 값을 저장할 배열
d = [0] * 100

# 1. 첫번째와 두번째는 지정해줌
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

# 2. 세번째부터는 점화식따라서 적용
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + arr[i]) # 맨끝 이전꺼 까지 터는 것 or 전전거까지 털고 +맨 뒤칸 터는 것 중 큰 것

print(d[n-1])

print(d[:4])
