m, n = map(int,input().split())

arr = [True]*n
end = int(n**0.5)

for i in range(2, end+1):               # 2부터 최대 약수 개수까지
    if arr[i]:                          # 가장 작은 배수 단위일 때 ex) 2
        for j in range(2*i, n, i):      # 다음 배수부터 배수단위로 끝까지 돌아서 ex) 4,6,8 ... n
            arr[j] = False              # 배열에서 제거, 즉 2의 배수는 2만 남는 방식

answer = [i for i in range(2,n) if arr[i] == True and i >= 2]
for i in answer:
    print(i)
