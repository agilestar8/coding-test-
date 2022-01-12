import sys
sys.setrecursionlimit(10 ** 9)
input =sys.stdin.readline

# 이진검색트리는 왼쪽보다 오른쪽이 항상커야함
def postorder(left,right):
    
    if left > right:    # 왼쪽이 크면 종료
        return
    else:
        mid = right + 1 # 첫 기준점, left : 0, right = 9
        for i in range(left+1, right+1):    # 0제외, 1~9까지
            if arr[left] < arr[i]:          # arr[0]보다 arr[i]가 크면, 
                mid = i                     # i가 기준점, 업데이트
                break
        
        postorder(left+1, mid-1)    # 왼쪽   후위순회, 1 ~ i까지 순회
        postorder(mid,right)        # 오른쪽 후위순회, i ~ 8까지 순회
        print(arr[left])
                    
arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

postorder(0,len(arr)-1) # 맨왼쪽과 맨끝 인덱스를 주고 시작
