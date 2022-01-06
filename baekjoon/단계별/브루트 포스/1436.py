# 종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다. 
# 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.
# 숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오. 

n = int(input())
init = 666
series = 0

while True:
    if "666" in str(init):
        series += 1

    if n == series:
        break

    init += 1

print(init)