def solution(name):
    answer = 0
    n = len(name)

    # 위아래 이동횟수
    for i in name:
        answer += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
        # A에서 거리 vs Z에서 거리 중 작은 것

    # 좌우 이동횟수
    move = n - 1
    for idx in range(n):
        next_idx = idx + 1  # 다음문자의 인덱스
        
        # 커서가 끝이아니고, 커서에 A가 있으면 
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1   # 이동할 칸 수 증가
            
        distance = min(idx, n - next_idx)   # 오른쪽
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer