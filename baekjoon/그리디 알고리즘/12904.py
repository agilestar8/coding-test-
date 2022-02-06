import sys
input = sys.stdin.readline

# 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 
# 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.
# 1.문자열의 뒤에 A를 추가한다.
# 2.문자열을 뒤집고 뒤에 B를 추가한다.
# 주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 

s = list(input().rstrip())
t = list(input().rstrip())

# S -> T 는 경우의수가 너무 많음
# 역으로 T -> S가 되는지 해본다

while len(s) != len(t): # 글자수 같아질때까지
    
    if t[-1] == 'A':    # A추가했다면 제거
        t.pop()
    
    elif t[-1] == 'B':  # B를 추가했다면 제거 후, 뒤집기
        t.pop()
        t = t[::-1]

if s == t:  # 연산 후 같다면
    print(1)
else:
    print(0)



