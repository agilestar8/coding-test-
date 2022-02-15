def solution(dirs):
    x,y = 0,0
    arr = set()
    
    # a->b 와 a->b은 중복이 당연하지만,
    # a->b 와 b->a도 같은 길을 지난 것이므로, 중복 취급해야함 
    
    for i in dirs:
        if i == "U" and y < 5:
            arr.add(((x,y),(x,y+1))) # (현재좌표 -> 이동할좌표) 저장
            y += 1 # 실시간 좌표수정
        elif i == "D" and -5 < y:
            arr.add(((x,y-1),(x,y))) # U과 D이 같다면 중복취급해야함
            y -= 1
        elif i == "L" and -5 < x:
            arr.add(((x-1,y),(x,y)))
            x -= 1    
        elif i == "R" and x < 5:
            arr.add(((x,y),(x+1,y)))
            x += 1
            
    return len(arr)
    