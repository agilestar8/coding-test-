import re

p = re.compile('[a-z]+')
# a~z의 문자열이 반복되는 표현을 찾기

# match - 일치하는지 확인
m = p.match('python') 
print(m)

m = p.match('33 python') 
print(m)

# search - 일치하는 부분 찾아서 리턴
m = p.search('33 python')
print(m)


# findall - 
m = p.findall("life is too short")
print(m)
for i in m:
    print(i)
    
# sub - 해당하는 문자열 치환하기    
