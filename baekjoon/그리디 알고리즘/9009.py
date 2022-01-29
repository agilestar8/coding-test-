import sys
input = sys.stdin.readline

# t = int(input())
# for _ in range(t):

n = int(input())

fivo = [0,1]
for i in range(2,50):
    fivo.append(fivo[i-1] + fivo[i-2])

answer = []
while n:
    for i in range(len(fivo)):
        if n >= fivo[i]:    
            temp = fivo[i] 
            
    n = n - temp
    answer.append(temp)
       
answer.sort()   
for i in answer:
    print(i, end = " ")
            
    






