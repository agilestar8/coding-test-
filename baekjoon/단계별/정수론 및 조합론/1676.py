from math import factorial

n = int(input())
x = factorial(n)
answer = 0

# answer 1 : 0의 갯수 세기
while True: 
    if x % 10 == 0:
        x = x//10 
        answer += 1
    else:
        break
print(answer)
    
    
# answer 2 : 10을 만드는 5의 개수 세기
while True: 
    if x%5 == 0:
        answer+=1
        x = x//5
    else:
        break

print(answer)    