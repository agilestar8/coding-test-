import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    num.append(input().rstrip())

alphabet = [0 for _ in range(26)]

for i in num:
    length = len(i) # 글자 길이 len(i)
    for j in range(length): # 글자의 각 문자 i[j]
        alphabet[ord(i[j])-65] += 10 ** (length - j - 1) # 맨 앞문자부터 자릿수를 부여
                                                         # ex) GCF -> G, 3글자의 첫문자 이므로 10**2, C는 10**1, F는 10**0
              
alphabet.sort(reverse=True) # 높은 자릿수 부터
print(alphabet)
result = 0
cnt = 9

for i in alphabet:
    result += cnt*i     # 9씩 부여
    cnt -= 1

print(result)

        
         
    
    

