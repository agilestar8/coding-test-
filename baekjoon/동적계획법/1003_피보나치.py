import sys
input = sys.stdin.readline    

t = int(input())
for _ in range(t):

    n = int(input())

    # 피보나치 : 0 1 1 2 3 5 8 ...    
    zero = [1,0] # n번째에서의 0의 개수
    one = [0,1]  # n번째에서의 1의 개수
    for i in range(2,n+1):
        zero.append(zero[i-1] +zero[i-2])
        one.append(one[i-1]+one[i-2])
    
    print(zero[n], one[n])
    # print(zero, one)