from itertools import combinations

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

case = list(combinations(range(1,n+1),n//2))
print(case)

min_gap = 1e9
for i in range(len(case)//2):
    team1 = case[i]                
    team2 = case[-1-i]
    
    sum1 = 0
    sum2 = 0
    
    for j in range(n//2):
        member = team1[j]
        for k in team1:
            sum1 += graph[member-1][k-1]
            
    
    for j in range(n//2):
        member = team2[j]
        for k in team2:
            sum2 += graph[member-1][k-1]
            
    min_gap = min(min_gap, abs(sum1-sum2))
            
print(min_gap)

