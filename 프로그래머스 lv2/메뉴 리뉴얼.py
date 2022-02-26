from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course: # 2,3,4 ...
        arr = []
        dic = {}
        # 모든 조합 구해서
        for i in orders:
            arr += combinations(sorted(i), c)
        
        # 메뉴조합 개수를 센다
        for j in arr:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
        
        # 최소2번 이상 시킨적 있어야함, 그 중 최대값 구하기
        m = 2
        for i,v in dic.items():  
            if m <= v:
                m = v
        
        # 최대로 시킨 c개의 단품요리 조합이 정답
        for i,v in dic.items():  
            if m == v:
                answer.append("".join(i))
                
    print(answer)
    return sorted(answer)