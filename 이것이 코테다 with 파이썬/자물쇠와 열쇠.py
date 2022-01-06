# key 90도 회전하는 함수
def rotate_key(key):
    n = len(key)    # 행 길이
    m = len(key[0]) # 열 길이
    result = [[0]*n for _ in range(m)] # 빈 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]

    return result

# 자물쇠부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key,lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 크기를 기존 3배로 변환
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4방향 확인할 것
    for i in range(4):
        key = rotate_key(key) # 회전 시킴
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 열쇠가 정확히 들어갔는지 검사
                if check(new_lock) == True:
                    return True
                
                # 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))