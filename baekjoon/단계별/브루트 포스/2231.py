# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

N = int(input())
print_num = 0

for i in range(1, N+1):                 # 숫자1부터 주어진 숫자까지
    div_num = list(map(int, str(i)))    # 각 숫자를 문자로 바꾸고 모든 경우의 각 자리수 배열    
    sum_num = i + sum(div_num)          # 분해합 = 자기자신(생성자) + 각 자리수의합
    if(sum_num == N):
        print_num = i
        break

print(print_num)


