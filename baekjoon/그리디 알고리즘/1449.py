import sys
input = sys.stdin.readline

n,l = map(int,input().split())
hole = list(map(int,input().split()))
cnt = 1

hole.sort()
# 시작위치: 첫구멍 기준, 테이프 간격만큼 증가
start = hole[0]     # 테이프의 시작
end = hole[0] + l   # 테이프의 끝

for i in hole:
    if start <= i < end:    # 구멍위치가 테이프 사이면
         continue           # 테이프 안붙여도됨, 테이프 더 붙이는 작업무시 (continue)
    
    else:                   # 구멍이 테이프의 끝을 넘어가면 
        cnt += 1            # 테이프 추가
        start = i           # 다음 테이프 시작위치
        end = i + l
        
print(cnt)