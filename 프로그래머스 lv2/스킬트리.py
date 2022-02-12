def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        pre_skill = list(skill)
        
        for i in tree:
            if i in pre_skill:
                if pre_skill[0] == i:   # 현재스킬이 선행스킬이면
                    pre_skill.pop(0)
                else:
                    break   # 이번 스킬트리는 불가능
        
        else:               
            answer += 1     # for문이 break에 안걸리고 정상적으로 나왔다면