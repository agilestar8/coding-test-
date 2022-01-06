N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3] # 현재 도전중인 스테이지

dic = {}
n = len(stages)

for i in range(1, N + 1): # 1~N stage 돌면서
    if stages.count(i) == 0: # 해당 stage에 도전하는 사람 = 실패인원이 0이면
        dic[i] = 0
    else:
        f_rate = stages.count(i)/n # 실패율 = 도전중인인원/도전했던인원
        dic[i] = f_rate
        n -= stages.count(i) # 현재 stage 도전 중인 사람은 다음 라운드에는 도전 못하니까 제외

a = sorted(dic ,key=lambda x : dic[x], reverse = True)
print(a)
