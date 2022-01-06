n,m,k = map(int,input().split())
data = list(map(int,input().split()))

total = 0
data.sort()
big1 = data[n-1]
big2 = data[n-2]

# 1번째 큰 수 반복횟수 = k번, 전체 반복횟수 = m/(k+1)번
# 2번째 큰 수 반복횟수 = m % (K+1)
count = int(k * m/(k+1)) + m%(k+1)
total = count * big1 + (m-count)*big2
print(total)






