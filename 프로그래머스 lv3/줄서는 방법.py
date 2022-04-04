import math

def solution(n, k):
    answer = []
    numberList = [i for i in range(1, n+1)]
    while (n != 0):
        temp = math.factorial(n) // n 
        index = k // temp # 앞의 자리 수 결정할 인덱스
        k = k % temp      # 남은 경우의 수 줄이기
        if k == 0:
            answer.append(numberList.pop(index-1))
        else :
             answer.append(numberList.pop(index))

        n -= 1
    
    return answer