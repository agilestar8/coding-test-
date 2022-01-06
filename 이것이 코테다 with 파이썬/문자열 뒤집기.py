s = input()
to_zero_cnt = 0
to_one_cnt = 0

if s[0] == "1":
    to_zero_cnt += 1
else:
    to_one_cnt += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            to_zero_cnt += 1
        else:
            to_one_cnt += 1

print(min(to_zero_cnt,to_one_cnt))

