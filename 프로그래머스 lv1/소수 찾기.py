# 에라토스테네스의 체 간단구현

def solution(n):
    num = set(range(2,n+1))     # 2부터 주어진 수 까지의 set배열

    for i in range(2,n+1):      # i는 2부터 주어진 수까지 돌면서
        if i in num:            # i가 num배열에 있으면
            num -= set(range(2*i,n+1,i))    # num배열에서 i다음부터의 i배수들을 모두 제거
                                            # ** set은 -연산으로 원소제거 가능

    return len(num) # 남은 배열은 소수만 남게된다
