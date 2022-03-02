def solution(n, costs):
    answer = 0
    root = [-1 for _ in range(n+1)]
    
    def union(a,b): # 연결 하기
        a = find(a)
        b = find(b)
        if a!=b:
            root[b] = a
        
    def find(a): # 루트 찾기
        if root[a] < 0:
            return a
        else:
            root[a] = find(root[a]) # 재귀해서 맨위(루트) 찾기
            return root[a]
        
    costs.sort(key = lambda x : x[2]) # 비용 적은 순으로 정렬
    for a,b,c in costs:
        if find(a) != find(b): # 루트가 다르면(다른 그룹이면)
            union(a,b)         # 연결
            answer += c        # MST갱신하면서
                
    return answer