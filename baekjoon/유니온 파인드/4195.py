import sys
input = sys.stdin.readline

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        root[x] = y             # x는 y의 친구
        number[y] += number[x]  # 이제 x의 친구들도 모두 y의 친구
            
def find(x):
    if x == root[x]:
        return x
    else:
        root[x] = find(root[x])
        return root[x]
        
t = int(input())
for _ in range(t):

    n = int(input())

    root = {}   # 친구관계
    number = {} # 각 사람의 친구숫자

    for _ in range(n):
        a, b = map(str,input().split())
        # 두 사람의 이름을 입력받은 후 아직 딕셔너리에 없는 이름이라면 추가해준다.

        if a not in root:   # root 초기화
            root[a] = a     # root[a] = a로 초기화해서 root에 넣기
            number[a] = 1   
            
        if b not in root:
            root[b] = b
            number[b] = 1
            
        union(a,b)              # a와 b의 루트 합치기 = 친구관계
        print(number[find(a)])  # a는 몇번째 친구? = 젤 높은 번호의 친구
    
    print(root)
    print(number)
