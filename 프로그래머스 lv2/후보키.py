from itertools import combinations

def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])  

    # 키 후보의 모든 조합
    arr=[]
    for i in range(1,n_col+1):
        arr.extend(combinations(range(n_col),i))

    # 유일성
    unique=[]
    for i in arr: # 모든 조합중에서
        tmp = [tuple([item[key] for key in i]) for item in relation] # 
        if len(set(tmp))==n_row:
            unique.append(i)

    # 최소성
    answer=set(unique[:])
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])
                
    return len(answer)


