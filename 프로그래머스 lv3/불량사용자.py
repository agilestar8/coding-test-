from itertools import permutations
   
def check(uid_case,bid_list):
    for i in range(len(bid_list)): 
        if len(uid_case[i]) != len(bid_list[i]): # 1. 길이 체크
            return False
        
        for j in range(len(bid_list[i])): # 2. *이외의 문자 같은 지 체크
            if bid_list[i][j] != '*' and bid_list[i][j] != uid_case[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    
    # 가능한 user_id의 경우의 수
    cases = list(permutations(user_id, len(banned_id)))
    ban_case = []
    
    for i in cases:
        if not check(i,banned_id):
            continue
        else:
            can_case = set(i)
            if can_case not in ban_case:
                ban_case.append(can_case)
    
    return len(ban_case)   