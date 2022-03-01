from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff = 0
    max_comb_cnt = {}


    # 화살 n개를 쏘는 조합, 중복허용 combinations_with_replacement
    for comb in combinations_with_replacement(range(11), n):
        cnt = Counter(comb) # 맞춘점수 당 화살갯수 세기
        
        score1, score2 = 0, 0
        for i in range(1, 11):
            if info[10-i] < cnt[i]: # b가 더 맞췄으면
                score1 += i         # b점수 +
            elif info[10-i] > 0:    # a가 더 맞췄으면
                score2 += i         # a점수 +
                
        diff = score1 - score2      # 점수차이 계산
        if diff > max_diff:
            max_comb_cnt = cnt      # 현재 화살 쏜 위치, 저장    
            max_diff = diff         # 최대점수차이 업데이트
            
    if max_diff > 0:
        answer = [0]*11
        for n in max_comb_cnt: # 점수차이 최대였던 경우에서
            answer[10-n] = max_comb_cnt[n] # 
            
        return answer 
    else:
        return [-1]
    