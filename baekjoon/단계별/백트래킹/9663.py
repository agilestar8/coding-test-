import sys
input = sys.stdin.readline

n = int(input())

col = [False]*n                 # 열 체크
p_diagonal = [False]*(2*n-1)    # 양 대각선 체크
n_diagonal = [False]*(2*n-1)    # 음 대각선 체크
answer = 0

def dfs(i):
    global answer
    if i == n:      # 모든 행 돌았으면
        answer += 1
        return
    
    for j in range(n):
        if (not col[j] and not p_diagonal[i+j] and not n_diagonal[i-j+n-1]): # 열,두 대각선에 다른 퀸이 없으면
            col[j] = True   # 해당 자리에 퀸을 놓는다
            p_diagonal[i+j] = True
            n_diagonal[i-j+n-1] = True
            dfs(i+1)    # 다음 행에도 같은 원리 실행
            
            col[j] = False  # 백트래킹
            p_diagonal[i+j] = False
            n_diagonal[i-j+n-1] = False

dfs(0)
print(answer)