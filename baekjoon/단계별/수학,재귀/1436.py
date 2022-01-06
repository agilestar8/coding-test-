# 첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.

n = int(input())

init = 666

if n == 1:
    print(666)

else:
    while(True):

        if n == 0:
            break
        
        init += 1

        if "666" in str(init):
            n -= 1        
    
    print(init)


