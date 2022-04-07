def solution(n, k, cmd):
    answer = ['O']*n
    # print(answer)
    
    # 링크드 리스트 - 현재번호:[앞번호,뒷번호]
    linked_list = {i: [i-1, i+1] for i in range(n)}
    # print(linked_list)
    
    stack = []
    idx = k # 현재 칸 idx 

    for i in cmd:
        # 1. 제거
        if i[0] == "C":     
            prev, next = linked_list[idx] # 앞,뒤 번호중에서
            stack.append([prev,next,idx]) # 제거하기전에 저장해두기(복구용)
            answer[idx] = 'X' # 제거했으므로 원본에서 변경체크
            
            if prev == -1: # prev(앞 노드)가 -1이면, (맨위 행이면)
                linked_list[next][0] = prev # 맨위를 지워서, 2번째가 맨위가되니 걔의 앞노드는 없다(= -1)
            elif next == n: # 맨뒤 행이면
                linked_list[prev][1] = next # (= n)
            else:
                linked_list[prev][1] = next # idx+1
                linked_list[next][0] = prev # idx-1
                
            if next == n: # next(뒷 노드)가 n이면, 맨아래 행이므로
                idx = linked_list[idx][0] # 제거시, 인덱스를 1칸 올려줌
            else: # 그외는 현재칸은 아래번호로 
                idx = linked_list[idx][1]
            
        # 2. 복구                
        elif i[0] == "Z": 
            prev,next,rnode = stack.pop()
            answer[rnode] = "O"
            
            if prev == -1: # 맨윗행 복구면, 그 아래행만 갱신
                linked_list[next][0] = rnode
            elif next == n: # 맨아래 복구면, 그 위에만 갱신
                linked_list[prev][1] = rnode
            else:
                linked_list[prev][1] = rnode
                linked_list[next][0] = rnode
                

        else:
            request,num = i.split()
            num = int(num)
            if request == "U":
                for _ in range(num): # 주어진 횟수만큼 
                    idx = linked_list[idx][0] # 앞에 연결된 인덱스로 갱신

            elif request == "D":
                for _ in range(num):
                    idx = linked_list[idx][1] # 뒤에 연결된 인덱스로 갱신
                    
    
    return "".join(answer)