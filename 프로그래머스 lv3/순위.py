from collections import defaultdict
def solution(n, results):
    answer = 0
    win = defaultdict(set)    # 이긴 애들
    lose = defaultdict(set)   # 진 애들
    
    for winner,loser in results:        # 결과에서 이기고 진 애들 그래프화
        win[loser].add(winner)
        lose[winner].add(loser)

    for i in range(1,n+1):         
        # i한테 진 애들은 i를 이긴 애들한테도 진 것
        for winner in win[i]:                    
            lose[winner].update(lose[i])
        # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
        for loser in lose[i]:                     
            win[loser].update(win[i])
    
    for i in range(1,n+1):
        # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
        if len(win[i]) + len(lose[i]) == n-1:   
            answer += 1

    return answer