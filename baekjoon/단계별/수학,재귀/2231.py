# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

# 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자

n = int(input())
ans = 0
for i in range(1,n):
    
    a = list(map(int,str(i)))
    b = i + sum(a)

    if b == n:
        ans = i
        break;

print(ans)
