import sys
input = sys.stdin.readline

name = list(map(str, input().strip()))
answer = ''
center = ''
name_count = [0 for _ in range(26)]
odd = 0

for word in name:
    name_count[ord(word)-65] += 1   # 문자들 개수 세기

for i in range(26):
    if name_count[i] % 2 == 1:      # 홀수인 문자면
        odd += 1
        center = chr(i+65)          # 홀수개 문자는 중간에 기록
    answer += chr(i+65) * (name_count[i] // 2)  # 짝수개 문자는 절반만 사전순 입력

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer + center + answer[::-1])
        