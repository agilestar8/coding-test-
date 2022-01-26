import sys
input = sys.stdin.readline

a = input()
b = input()
cnt = 0
idx = 0

while idx <= len(a) - len(b):    
    if a[idx:idx+len(b)] == b:
        cnt += 1
        idx += len(b)
    else:
        idx += 1
    
print(cnt)

# 방법2, 문자열에서 개수 세는 함수 str.count()
# import sys
# s = sys.stdin.readline().strip("\n")
# search = sys.stdin.readline().strip("\n")
# count = s.count(search)
# print(count)