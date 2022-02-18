from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    # 던전의 모든 경우에서 검사
    cases = list(permutations(dungeons,n)) 
    
    answer = 0
    for i in cases:
        cnt = 0
        hp = k
        for mc,uc in i:
           if hp >= mc:
               hp -= uc 
               cnt += 1
           else:
               break

        answer = max(cnt,answer)

    return answer