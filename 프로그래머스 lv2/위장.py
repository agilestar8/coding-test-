clothes = [["yellowhat", "headgear"], 
           ["bluesunglasses", "eyewear"], 
           ["green_turban", "headgear"]]

from collections import Counter
from functools import reduce
dict = {}
# case1) 각각 옷의 종류를 세기
def solution(clothes):
    dic = {}
    for cloth,kind in clothes:
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1
    cnt = 1
    # a,b와 c,d,f가 있다면
    # ac,ad,af + bc,bd,bf + a,b,d,c,f + x = 12가지 경우 = (2종류+1)*(3종류+1)
    for i in dic.values():
        cnt *= i+1  # (종류+1)을 전부 곱하기
    
    return cnt-1    # 아무것도 안입었을때까지 포함한 것이므로 제외


# case2) Counter로 세기 (위와 같음)
# dict = Counter([kind for cloth, kind in clothes])
# answer = reduce(lambda x,y : x*(y+1), dict.values(),1)-1
# print(answer)



